from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    env: str = Field(...,
                     alias="ENVIRONMENT")
    use_alembic : bool = Field(
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

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
    
    @property
    def is_development(self) -> bool:
        return self.env == "development"
    
    @property
    def is_production(self) -> bool:
        return self.env == "production"
