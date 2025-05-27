from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DB_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db_session():
    db = SessionLocal
    with db.begin() as begin:
        begin.execute(text('CREATE EXTENSION IF NOT EXISTS vector'))

    try:
        yield db
    finally:
        db.close()

