from pydantic import Field
from pydantic_settings import BaseSettings


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

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def is_development(self) -> bool:
        return self.env == "development"

    @property
    def is_production(self) -> bool:
        return self.env == "production"
