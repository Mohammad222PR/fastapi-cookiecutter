from pydantic_settings import BaseSettings, SettingsConfigDict
{% if cookiecutter.database == "postgres" %}
import os

pg_user = os.getenv("POSTGRES_USER", "user")
pg_password = os.getenv("POSTGRES_PASSWORD", "password")
pg_host = os.getenv("POSTGRES_HOST", "localhost")
pg_database = os.getenv("POSTGRES_DB", "{{ cookiecutter.project_name }}")
{% endif %}

class Settings(BaseSettings):
    APP_NAME: str = "{{ cookiecutter.project_name }}"
    APP_VERSION: str = "{{ cookiecutter.version }}"
    ENVIRONMENT: str = "development"
    DATABASE_URL: str = {% if cookiecutter.database == "postgres" %} f"postgresql+asyncpg://{pg_user}:{pg_password}@{pg_host}/{pg_database}"
    {% else %} "sqlite+aiosqlite:///db.sqlite3"
    {% endif %}
    {% if cookiecutter.use_redis == "yes" %}
    REDIS_URL: str = "redis://localhost:6379/0"
    {% endif %}

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()