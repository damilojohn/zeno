import os
from dotenv import load_dotenv

from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)
CORS_ORIGIN = os.getenv("CORS_ORIGINS")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")


class Settings(BaseSettings):
    database_url: str = Field(DATABASE_URL,
                              alias="db conn string",
                                      )
    cors_origin: str = Field(CORS_ORIGIN,
                             alias="CORS_ORIGIN",
                             )
    google_client_id: str = Field(GOOGLE_CLIENT_ID,
                                  alias="GOOGLE_CLIENT_ID",
                                  )
    google_client_secret: str = Field(GOOGLE_CLIENT_SECRET,
                                      alias="GOOGLE_CLIENT_SECRET",
                                      )
    gemini_api_key: str = Field(GEMINI_API_KEY,
                                alias="GEMINI_API_KEY",
                                )
    gemini_model: str = Field(GEMINI_MODEL,
                              alias="GEMINI_MODEL",
                              )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
