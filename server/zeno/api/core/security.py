from zeno.api.core.config import Settings
from zeno.api.core.utils import LOG

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
        return hashlib.sha256(token.encode()).hexdigest() == db_hash
    except Exception as e:
        LOG.info(f"token verification failed with error {e}")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.jwt_expiration)
    to_encode.update({"exp": expire})
    token = jwt.encode(
        to_encode,
        settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm
    )
    return token


def create_refresh_token(data: dict):
    to_encode = data.copy()
    # Refresh tokens typically last longer, e.g., 7 days
    expire = datetime.now(timezone.utc) + timedelta(
        days=settings.jwt_refresh_exp)
    to_encode.update({
        "exp": expire,
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
    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=settings.jwt_algorithm
        )
        return payload['username']
    except jwt.ExpiredSignatureError as e:
        LOG.info(f"Access token validation failed with error :{str(e)}")
        raise ValueError("Access token has expired") from e
    except jwt.PyJWTError as e:
        LOG.info(f"Access token validation failed with error :{str(e)}")
        raise ValueError("Invalid access token") from e


def verify_refresh_token(token: str):
    try:
        payload = jwt.decode(
            token,
            settings.jwt_refresh_secret_key,
            algorithms=[settings.jwt_algorithm]
        )
        if payload.get("token_type") != "refresh":
            raise ValueError("Invalid token type")
        return payload["username"]
    except jwt.ExpiredSignatureError as e:
        LOG.info(f"refresh token validation failed with error :{str(e)}")
        raise ValueError("Refresh token has expired") from e
    except jwt.PyJWTError as e:
        LOG.info(f"Refresh token validation failed with error :{str(e)}")
        raise ValueError("Invalid refresh token") from e

