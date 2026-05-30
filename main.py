import asyncio
import logging
import os

from aiohttp import web
from aiogram import Bot, Dispatcher

from handlers import router

TOKEN = os.getenv("8744007590:AAELB6PD01HATPbKvTu_EMUUDVZiRcKGKuc")


# ---------------- BOT ----------------
async def start_bot():
    if not TOKEN:
        raise ValueError("TOKEN is missing in environment variables")

    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)


# ---------------- WEB SERVER (ВАЖНО ДЛЯ RENDER) ----------------
async def start_web():
    app = web.Application()

    async def handle(request):
        return web.Response(text="Bot is running")

    app.router.add_get("/", handle)

    port = int(os.getenv("PORT", 10000))

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()


# ---------------- MAIN ----------------
async def main():
    logging.basicConfig(level=logging.INFO)

    await asyncio.gather(
        start_bot(),
        start_web()
    )


if __name__ == "__main__":
    asyncio.run(main())
