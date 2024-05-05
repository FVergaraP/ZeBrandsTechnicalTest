from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    jwt_secret_key: str
    jwt_algorithm: str
    jwt_access_token_expire_minutes: int = 30
    sqlalchemy_database_url: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
