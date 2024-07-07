from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    validate_token_url: str
    aws_access_key: str
    aws_secret_key: str
    email_sender:  str
    aws_region: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
