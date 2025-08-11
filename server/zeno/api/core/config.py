from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

print(Path(__file__).resolve().parent / ".env")

class Settings(BaseSettings):
    env: str = Field(...,
                     alias="ENVIRONMENT")
    host: str = Field(
        ...,
        alias="HOST"
    )
    port: int = Field(...,
    alias="PORT"
    )
    use_alembic: bool = Field(
        default=False)
    database_url: str = Field(...,
                              alias="DATABASE_URL",
                                      )
    cors_origin: str = Field(...,
                             alias="CORS_ORIGINS",
                             )
    google_client_id: str = Field(...,
                                  alias="GOOGLE_CLIENT_ID",
                                  )
    google_client_secret: str = Field(...,
                                      alias="GOOGLE_CLIENT_SECRET",
                                      )
    gemini_api_key: str = Field(...,
                                alias="GEMINI_API_KEY",
                                )
    gemini_model: str = Field(...,
                              alias="GEMINI_MODEL",
                              )
    jwt_secret_key: str = Field(...,
                                alias="JWT_SECRET_KEY")
    jwt_refresh_secret_key: str = Field(...,
                                        alias="JWT_REFRESH_SECRET_KEY")
    jwt_algorithm: str = Field(...,
                               alias="JWT_ALGORITHM")
    jwt_expiration: int = Field(...,
                                alias="JWT_EXP")
    jwt_refresh_exp: int = Field(...,
                                 alias="JWT_REFRESH_EXP")
    reset_tok_exp: int = Field(...,
                                alias="RESET_TOK_EXP")
    
    # Email settings
    smtp_server: str = Field(default="smtp.gmail.com",
                             alias="SMTP_SERVER")
    smtp_port: int = Field(default=587,
                           alias="SMTP_PORT")
    smtp_username: str = Field(default="",
                               alias="SMTP_USERNAME")
    smtp_password: str = Field(default="",
                               alias="SMTP_PASSWORD")
    email_from: str = Field(default="noreply@zeno.com",
                            alias="EMAIL_FROM")
    frontend_url: str = Field(default="http://localhost:3000",
                              alias="FRONTEND_URL")

    class Config:
        env_file = Path(__file__).resolve().parent / ".env"
    
        env_file_encoding = "utf-8"

    @property
    def is_development(self) -> bool:
        return self.env == "development"

    @property
    def is_production(self) -> bool:
        return self.env == "production"
