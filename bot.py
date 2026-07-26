import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN
from handlers import start_router, download_router, admin_router

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(download_router)
    dp.include_router(admin_router)

    print("🚀 Abu Janat Downloader Started...")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
