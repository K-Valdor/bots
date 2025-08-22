from dataclasses import dataclass
import os
@dataclass
class Settings:
    bot_token: str = os.getenv("BOT_TOKEN", "")
    app_version: str = os.getenv("APP_VERSION", "0.0.0")
    postgres_dsn: str = os.getenv("POSTGRES_DSN", "postgresql://bot:bot@db:5432/bot")
settings = Settings()
