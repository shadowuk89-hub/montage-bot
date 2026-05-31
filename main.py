import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from handlers import router

from aiohttp import web

TOKEN = os.getenv("BOT_TOKEN")


async def main():
    logging.basicConfig(level=logging.INFO)

    print("Starting bot...")

    if not TOKEN:
        raise ValueError("BOT_TOKEN is missing")

    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    # fake web server for Render (to keep service alive)
    app = web.Application()
    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "0.0.0.0", 10000)
    await site.start()

    print("Bot started + port opened")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
