from datetime import datetime, timedelta
import random
import string
import os
import base64

from passlib.context import CryptContext
import jwt

from dotenv import load_dotenv

load_dotenv()

ALGORITHM = os.getenv("JWT_ALGORITHM")


pwd_context = CryptContext(
    schemes=['argon2'],
    deprecated='auto',
    argon2_time_cost=4,
    argon2_memory_cost=65536,
    argon2_parallelism=4,
)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
    return pwd_context.hash(password)

