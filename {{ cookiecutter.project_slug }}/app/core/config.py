from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "{{ cookiecutter.project_name }}"
    APP_VERSION: str = "{{ cookiecutter.version }}"
    ENVIRONMENT: str = "development"
    DATABASE_URL: str = { % if cookiecutter.database == "postgres" %}"postgresql+asyncpg://user:password@localhost:5432/{{ cookiecutter.project_slug }}"
    { % else %}"sqlite+aiosqlite:///db.sqlite3"
    { % endif %}
    { % if cookiecutter.use_redis == "yes" %}
    REDIS_URL: str = "redis://localhost:6379/0"
    { % endif %}

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()