import asyncio
import logging
import os

from aiohttp import web
from aiogram import Bot, Dispatcher

from handlers import router

TOKEN = os.getenv("8744007590:AAELB6PD01HATPbKvTu_EMUUDVZiRcKGKuc")


async def health(request):
    return web.Response(text="Bot is running")


async def start_web_server():
    app = web.Application()
    app.router.add_get("/", health)

    runner = web.AppRunner(app)
    await runner.setup()

    port = int(os.getenv("PORT", 10000))

    site = web.TCPSite(
        runner,
        host="0.0.0.0",
        port=port,
    )

    await site.start()

    print(f"Web server started on port {port}")


async def start_bot():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)


async def main():
    logging.basicConfig(level=logging.INFO)

    await start_web_server()

    await start_bot()


if __name__ == "__main__":
    asyncio.run(main())
