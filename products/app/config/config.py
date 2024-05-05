from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    jwt_secret_key: str
    jwt_algorithm: str
    sqlalchemy_database_url: str
    validate_token_url: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
