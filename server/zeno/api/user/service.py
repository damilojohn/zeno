from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.exc import SQLAlchemyError

from zeno.api.core.utils import LOG
from zeno.api.core.security import (get_password_hash,
                                    create_access_token,
                                    verify_access_token,
                                    verify_refresh_token,
                                    verify_password,
                                    create_refresh_token)
from zeno.api.user.schemas import (UserCreate,
                                   RegisterResponse,
                                   TokenResponse,
                                   LoginRequest)

from zeno.api.models.users import User
from zeno.api.core.db import Session, get_db_session
from zeno.api.core.config import Settings

settings = Settings()

oauth2scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(token: str = Depends(oauth2scheme),
                           session: Session = Depends(get_db_session)) -> User:
    try:
        username = verify_access_token(token)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        ) from e
    user = session.query(User).filter(
        User.username == username
    ).first()
    if user:
        return user
    else:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="Unable to get user...."
        )


async def add_new_user(
    new_user: UserCreate,
    session: Session = Depends(get_db_session)
):
    try:
        # Check if user exists
        existing_user = session.query(User).filter(
                User.username == new_user.username
        ).first()

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
        session.commit()
        session.refresh(db_user)

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

    except SQLAlchemyError as e:
        session.rollback()
        LOG.error("Database error during user creation", error=str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error creating user"
        ) from e


async def authenticate_user(user: LoginRequest,
                            session: Session = Depends(get_db_session)):
    db_user = session.query(User).filter(
        User.username == user.username
    ).first()
    if db_user:
        if not verify_password(user.password, db_user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User does not exist"
        )
    return TokenResponse(
        access_token=create_access_token(data={"username": str(db_user.username)}),
        refresh_token=create_refresh_token(data={"username":str(db_user.username)}),
        token_type="bearer"
    )


def get_refresh_token(token: str = Depends(oauth2scheme)):
    try:
        payload = verify_refresh_token(token)
        if payload:
            return TokenResponse(
                access_token = create_access_token({"username": payload}),
                refresh_token = "",
                token_type="bearer"
            )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token"
        ) from e


# async def handle_google_oauth(
#     code: str,
#     redirect_uri: str,
#     session: Session = Depends(get_db_session)
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
#         user = session.query(User).filter(User.email == email).first()
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
#             session.commit()
#             session.refresh(user)
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
#         session.rollback()
#         LOG.error("Database error during user creation", error=str(e))
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail="Error creating user"
#         )