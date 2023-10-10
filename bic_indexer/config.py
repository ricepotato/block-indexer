import pydantic
import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    kas_access_key_id: str = pydantic.Field(default=None, env="KAS_ACCESS_KEY_ID")
    kas_secret_key_id: str = pydantic.Field(default=None, env="KAS_SECRET_KEY_ID")
