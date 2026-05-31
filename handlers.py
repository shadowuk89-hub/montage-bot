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
            "👨‍💻 Про мене\n\n"
            "Я професійно займаюся монтажем відео понад 8 років.\n"
            "Створюю динамічний та сучасний відеоконтент для різних платформ.\n\n"
            "📌 Що я вмію:\n"
            "• Відео для YouTube\n"
            "• TikTok відео\n"
            "• YouTube Shorts\n"
            "• Instagram Reels\n"
            "• Рекламні ролики\n"
            "• Слайд-шоу\n"
            "• Інтерв’ю\n\n"
            "🎬 Додатково:\n"
            "• підбір музики\n"
            "• кольорокорекція\n"
            "• мультикамерний монтаж\n"
            "• обробка звуку, шумоприглушення\n"
            "• відео/аудіо ефекти\n"
            "• графіка, плашки, інфографіка\n"
            "• кейінг, ротоскопінг\n\n"
            "🛠 Обробка відео (покращення матеріалу):\n"
            "• clean-up (видалення об'єктів)\n"
            "• трекінг руху\n"
            "• заміна тексту у відео\n"
            "• приховування логотипів / даних\n"
            "• стабілізація відео\n"
            "• додавання 2D/3D об'єктів\n"
            "• чистка та покращення аудіо\n"
            "• розділення музики і голосу\n\n"
            "Якщо все зрозуміло і ти готовий замовити монтаж — натисни кнопку нижче 👇",
            reply_markup=about_kb()
        )


    elif data == CB_WORKS:
        await call.message.edit_text("📁 Приклади робіт:", reply_markup=works_kb())


    elif data == CB_ORDER:
        await call.message.edit_text(
            "📩 Як замовити монтаж:\n\n"
            "• надішли вихідні матеріали\n"
            "• опиши задачу\n"
            "• додай приклади стилю\n\n"
            "Після цього я зв’яжусь з тобою 👇",
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
