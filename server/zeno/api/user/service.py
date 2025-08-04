from datetime import datetime, timezone, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR

from zeno.api.core.utils import LOG
from zeno.api.core.security import (get_password_hash,
                                    create_access_token,
                                    verify_access_token,
                                    create_reset_token,
                                    verify_refresh_token,
                                    verify_token_hash,
                                    get_token_hash,
                                    verify_password,
                                    create_refresh_token)
from zeno.api.user.schemas import (UserBase, UserCreate,
                                   RegisterResponse,
                                   TokenResponse,
                                   ResetTokenResponse,
                                   LoginRequest)

from zeno.api.models.users import User, ResetTokens
from zeno.api.core.db import get_db_session
from zeno.api.core.config import Settings

settings = Settings()

oauth2scheme = OAuth2PasswordBearer(tokenUrl="/v2/auth/form-login")


async def get_current_user(token: str = Depends(oauth2scheme),
                           session: AsyncSession = Depends(get_db_session)) -> User:
    """Get current db user from JWT"""
    try:
        LOG.info("Getting User from JWT")
        username = verify_access_token(token)
    except Exception as e:
        LOG.info(f"failed with error {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        ) from e
    
    result = await session.execute(select(User).filter(User.username == username))
    user = result.scalar_one_or_none()
    
    if user:
        return user
    else:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials...."
        )


async def add_new_user(
    new_user: UserCreate,
    session: AsyncSession = Depends(get_db_session)
):
    try:
        # Check if user exists
        result = await session.execute(select(User).filter(User.username == new_user.username))
        existing_user = result.scalar_one_or_none()

        if existing_user:
            LOG.info(
                "Tried to create already existing user... Failing with 409"
            )
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this email already exists"
            )

        # Create new user
        hashed_pwd = get_password_hash(new_user.password)
        db_user = User(
            email=new_user.email,
            username=new_user.username,
            hashed_password=hashed_pwd,
        )
        # Add and commit in a transaction
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)

        # Generate tokens
        try:

            access_token = create_access_token({"username": str(db_user.username)})
            refresh_token = create_refresh_token({"username": str(db_user.username)})
        except Exception as e:
            LOG.info(f"failed with error {e}")
            raise e
        
        return RegisterResponse(
            username=new_user.username,
            is_verified=False,
            access_token=access_token,
            refresh_token=refresh_token,
            message="User created Successfully"
        )

    except HTTPException:
        raise
    except Exception as e:
        LOG.info(f"failed to create user with error {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"failed to create user with error {e}"
        )


async def authenticate_user(user: LoginRequest,
                            session: AsyncSession = Depends(get_db_session)):
    try:
        result = await session.execute(select(User).filter(User.username == user.username))
        db_user = result.scalar_one_or_none()

        if not db_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password"
            )

        if not verify_password(user.password, db_user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password"
            )

        access_token = create_access_token({"username": str(db_user.username)})
        refresh_token = create_refresh_token({"username": str(db_user.username)})

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer"
        )

    except HTTPException:
        raise
    except Exception as e:
        LOG.info(f"failed with error {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token credentials"
        ) from e


def get_refresh_token(token: str = Depends(oauth2scheme)):
    try:
        username = verify_refresh_token(token)
        access_token = create_access_token({"username": username})
        refresh_token = create_refresh_token({"username": username})

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer"
        )
    except Exception as e:
        LOG.info(f"failed with error {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token credentials"
        ) from e


async def send_reset_mail(token: str, email: str, username: str):
    """Generates password reset mail """
    from zeno.api.core.email import send_password_reset_email
    
    # Try to send email, fallback to logging if it fails
    email_sent = await send_password_reset_email(email, token, username)
    if not email_sent:
        LOG.info(f"Failed to send email, logging token instead: {token}")
    else:
        LOG.info(f"Password reset email sent successfully to {email}")


async def reset_password(email: str, db_session: AsyncSession):
    # verify user exists with mail // username
    try:
        LOG.info("Fetching user ....")
        result = await db_session.execute(select(User).filter(User.email == email))
        db_user = result.scalar_one_or_none()

        if not db_user:
            return ResetTokenResponse(
                    msg="Password Reset mail sent successfully!! (user doesn't exist)"
            )

        else:
            # generate token
            token = create_reset_token()
            hashed_token = get_token_hash(token)
            db_token = ResetTokens(
                    token_hash = hashed_token,
                    user_id = db_user.id,
                    to_expire = datetime.now(timezone.utc) + timedelta(minutes=settings.reset_tok_exp)
                    )
            db_session.add(db_token)
            await db_session.commit()

            # generate mail
            # await send_reset_mail(token, db_user.email, db_user.username)
    except Exception as e:
        LOG.info(f"password reset failed with {e}")
        raise HTTPException(
            status_code=500,
            detail=f"password reset failed with error {e}"
        )
    try:
        LOG.info("sending email to user....")
        await send_reset_mail(token, db_user.email, db_user.username)
    except Exception as e:
        LOG.info(f"failed to send email to user with error {e}...")
        raise HTTPException(
            detail="failed to send user mail",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


    return ResetTokenResponse(
            msg="Password Reset mail sent successfully!!"
    )
    


async def create_new_password(new_password,
                        user: User,
                        token: str,
                        db_session: AsyncSession):
    try:
        # verify token hash
        result = await db_session.execute(
            select(ResetTokens)
            .filter(ResetTokens.user_id == user.id)
            .order_by(ResetTokens.to_expire.desc())
        )
        db_token = result.scalar_one_or_none()
        
        if db_token:
            LOG.info("Retrieved reset_token...")
            if verify_token_hash(token, db_token.token_hash):
                LOG.info("Verified reset token")
                to_expire = db_token.to_expire
                curr_time = datetime.now(timezone.utc)
                LOG.info(f"current time: {str(curr_time)}")
                if curr_time > to_expire:
                    LOG.info("Reset token expired..")
                    raise HTTPException(
                        status_code=HTTP_400_BAD_REQUEST,
                        detail=" Reset Token expired"
                    )
                else:
                    # write new password to db
                    new_password_hsh = get_password_hash(new_password)
                    try:

                        result = await db_session.execute(select(User).filter_by(id=user.id))
                        db_user = result.scalar_one_or_none()
                        if db_user:
                            db_user.hashed_password = new_password_hsh
                            
                            # Delete all reset tokens for this user
                            await db_session.execute(
                                select(ResetTokens).filter(ResetTokens.user_id == user.id)
                            )
                            delete_result = await db_session.execute(
                                select(ResetTokens).filter(ResetTokens.user_id == user.id)
                            )
                            tokens_to_delete = delete_result.scalars().all()
                            for token_to_delete in tokens_to_delete:
                                await db_session.delete(token_to_delete)
                            
                            await db_session.commit()
                            return "Password changed successfully..."
                    except SQLAlchemyError as e:
                        LOG.info(f"DB write failed... with error {e}")
                        raise HTTPException(
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Failed to write to db with error {e}"
                        )
            else:
                LOG.info("DB Hash and token hash not equal")
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="failed to verify reset token"
                )
        else:
            LOG.info("failed to get db token")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="invalid reset token"
            )              
    except Exception as e:
        LOG.info(f"failed to create new password with error {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"failed to create new password with error {e}"
        )


# async def handle_google_oauth(
#     code: str,
#     redirect_uri: str,
#     session: AsyncSession = Depends(get_db_session)
# ):
#     try:
#         # Verify the Google OAuth token
#         idinfo = id_token.verify_oauth2_token(
#             code,
#             requests.Request(),
#             settings.google_client_id
#         )

#         if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
#             raise ValueError('Invalid issuer')

#         email = idinfo['email']
#         name = idinfo.get('name', '')

#         # Check if user exists
#         result = await session.execute(select(User).filter(User.email == email))
#         user = result.scalar_one_or_none()
#         is_new_user = False

#         if not user:
#             # Create new user
#             user = User(
#                 email=email,
#                 username=name or email.split('@')[0],
#                 auth_provider="google",
#                 is_verified=True  # Google emails are pre-verified
#             )
#             session.add(user)
#             await session.commit()
#             await session.refresh(user)
#             is_new_user = True

#         # Generate tokens
#         access_token = create_access_token({"sub": user.email})
#         refresh_token = create_refresh_token({"sub": user.email})

#         return {
#             "user": db_user,
#             "access_token": access_token,
#             "refresh_token": refresh_token,
#             "message": "User created successfully"
#         }

#     except SQLAlchemyError as e:
#         await session.rollback()
#         LOG.error("Database error during user creation", error=str(e))
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail="Error creating user"
#         )