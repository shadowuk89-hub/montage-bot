from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards import (
    main_menu_kb,
    about_kb,
    works_kb,
    order_kb,
    prices_kb,
    category_kb,
    videos_kb,
    showreel_kb,
    parse_category_callback,

    CB_MAIN,
    CB_ABOUT,
    CB_WORKS,
    CB_ORDER,
    CB_PRICES,
    CB_VERTICAL,
    CB_HORIZONTAL,
    CB_SHOWREEL,
)

router = Router()


# ---------------- START ----------------
@router.message(Command("start"))
async def start(message: Message):
    await message.answer("👋 Головне меню:", reply_markup=main_menu_kb())


# ---------------- CALLBACKS ----------------
@router.callback_query()
async def handler(call: CallbackQuery):
    data = call.data

    if data == CB_MAIN:
        await call.message.edit_text("👋 Головне меню:", reply_markup=main_menu_kb())

    elif data == CB_ABOUT:
        await call.message.edit_text(
            "👨‍💻 Про мене:\n\n"
            "Я займаюсь професійним монтажем відео, AI обробкою, sound design та motion graphics.",
            reply_markup=about_kb()
        )

    elif data == CB_WORKS:
        await call.message.edit_text("📁 Приклади робіт:", reply_markup=works_kb())

    elif data == CB_ORDER:
        await call.message.edit_text(
            "📩 Як замовити монтаж:\n\n"
            "• надайте вихідні матеріали\n"
            "• опишіть задачу\n"
            "• прикріпіть приклади\n\n"
            "Я зв’яжусь з вами після цього 👇",
            reply_markup=order_kb()
        )

    elif data == CB_PRICES:
        await call.message.edit_text(
            "💰 Ціни:\n\n"
            "• Shorts (простий) — від 400 грн\n"
            "• Горизонтальне відео — від 2$ за хвилину\n",
            reply_markup=prices_kb()
        )

    elif data == CB_VERTICAL:
        await call.message.edit_text("📱 Вертикальні відео:", reply_markup=category_kb("vertical"))

    elif data == CB_HORIZONTAL:
        await call.message.edit_text("📺 Горизонтальні відео:", reply_markup=category_kb("horizontal"))

    elif data == CB_SHOWREEL:
        await call.message.edit_text("🎬 Шоурил:", reply_markup=showreel_kb())

    # category videos
    parsed = parse_category_callback(data)
    if parsed:
        section, key = parsed
        await call.message.edit_text(
            "📁 Відео:",
            reply_markup=videos_kb(section, key)
        )

    await call.answer()