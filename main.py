import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from handlers import router

TOKEN = os.getenv("TOKEN")


async def main():
    logging.basicConfig(level=logging.INFO)

    if not TOKEN:
        raise ValueError("TOKEN is missing in environment variables")

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
