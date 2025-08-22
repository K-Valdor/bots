from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from .settings import settings
from . import __version__
import asyncpg

router = Router()

@router.message(Command("health"))
async def health(message: Message):
    db_ok = True
    try:
        conn = await asyncpg.connect(settings.postgres_dsn)
        await conn.execute("SELECT 1;")
        await conn.close()
    except Exception:
        db_ok = False
    status = "ok" if db_ok else "ok (db=unavailable)"
    await message.answer(f"health: {status}")

@router.message(Command("version"))
async def version(message: Message):
    await message.answer(f"version: {__version__}")
