from zeno.api.core.config import Settings
from zeno.api.core.utils import LOG

from fastapi import HTTPException, status
from passlib.context import CryptContext
import secrets, hashlib
from datetime import datetime, timedelta, timezone
import jwt


pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto",
    argon2__time_cost=4,
    argon2__memory_cost=65536,
    argon2__parallelism=4,

)

settings = Settings()


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)


def create_reset_token() -> str:
    token = secrets.token_urlsafe(64)
    return token


def get_token_hash(token:str)-> str:
    token_hash = hashlib.sha256(token.encode()).hexdigest()
    return token_hash


def verify_token_hash(token:str, db_hash: str):
    try:
        token_hash = get_token_hash(token)
        LOG.info(f"token hash {token_hash} db_hash {db_hash}")
        return token_hash == db_hash
    except Exception as e:
        LOG.info(f"token verification failed with error {e}")


def create_access_token(data: dict):
    to_encode = data.copy()
    iat = datetime.now(timezone.utc)
    expire = iat + timedelta(
        days=settings.jwt_refresh_exp)
    to_encode.update({"exp": expire,
                    "iat":iat})
    token = jwt.encode(
        to_encode,
        settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm
    )
    return token


def create_refresh_token(data: dict):
    to_encode = data.copy()
    # Refresh tokens typically last longer, e.g., 7 days
    iat = datetime.now(timezone.utc)
    expire = iat + timedelta(
        days=settings.jwt_refresh_exp)
    to_encode.update({
        "exp": expire,
        "iat": iat,
        "token_type": "refresh"  # Adding token type for additional security
    })
    token = jwt.encode(
        to_encode,
        settings.jwt_refresh_secret_key,
        algorithm=settings.jwt_algorithm
    )
    LOG.info("user refresh token created...")
    return token


def verify_access_token(token: str):
    """get user from jwt data"""
    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=settings.jwt_algorithm
        )
        return payload['sub']
    except jwt.ExpiredSignatureError as e:
        LOG.info(f"Access token  has expired:{str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Access token has expired",
        ) from e
    except jwt.PyJWTError as e:
        LOG.info(f"Access token validation failed with error :{str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Access token has expired",
        ) from e


def verify_refresh_token(token: str):
    try:
        payload = jwt.decode(
            token,
            settings.jwt_refresh_secret_key,
            algorithms=[settings.jwt_algorithm]
        )
        if payload.get("token_type") != "refresh":
            raise ValueError("Invalid token type")
        return payload["sub"]
    except jwt.ExpiredSignatureError as e:
        LOG.info(f"refresh token validation failed with error :{str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token has expired") from e
    except jwt.PyJWTError as e:
        LOG.info(f"Refresh token validation failed with error :{str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token") from e

