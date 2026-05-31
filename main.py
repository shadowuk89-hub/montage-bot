import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from handlers import router

TOKEN = os.getenv("BOT_TOKEN")


async def main():
    logging.basicConfig(level=logging.INFO)

    print("Starting bot...")

    if not TOKEN:
        raise ValueError("BOT_TOKEN is missing")

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    print("Polling started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
