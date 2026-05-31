from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from data import HORIZONTAL, SHOWREEL_URL, VERTICAL


# ---------------- CALLBACKS ----------------
CB_MAIN = "main"

CB_ABOUT = "about"
CB_WORKS = "works"
CB_PRICES = "prices"
CB_ORDER = "order"

CB_VERTICAL = "vertical"
CB_HORIZONTAL = "horizontal"
CB_SHOWREEL = "showreel"

CONTACT_URL = "https://t.me/MN_videomaker"

BACK = "◀️ Назад"


# ---------------- BACK BUTTON ----------------
def back_main():
    return InlineKeyboardButton(text=BACK, callback_data=CB_MAIN)


def back_row():
    return [back_main()]


# ---------------- MAIN MENU ----------------
def main_menu_kb():
    builder = InlineKeyboardBuilder()

    builder.row(InlineKeyboardButton(text="👨‍💻 Про мене", callback_data=CB_ABOUT))
    builder.row(InlineKeyboardButton(text="📁 Приклади робіт", callback_data=CB_WORKS))
    builder.row(InlineKeyboardButton(text="💰 Ціни", callback_data=CB_PRICES))
    builder.row(InlineKeyboardButton(text="📩 Як замовити монтаж", callback_data=CB_ORDER))

    return builder.as_markup()


# ---------------- ABOUT ----------------
def about_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💬 Замовити монтаж", callback_data=CB_ORDER)],
            [InlineKeyboardButton(text="📁 Приклади робіт", callback_data=CB_WORKS)],
            back_row()
        ]
    )


# ---------------- WORKS ----------------
def works_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📱 Вертикальні відео", callback_data=CB_VERTICAL)],
            [InlineKeyboardButton(text="📺 Горизонтальні відео", callback_data=CB_HORIZONTAL)],
            [InlineKeyboardButton(text="🎬 Шоурил", callback_data=CB_SHOWREEL)],
            back_row()
        ]
    )


# ---------------- ORDER ----------------
def order_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📩 Написати мені", url=CONTACT_URL)],
            back_row()
        ]
    )


# ---------------- PRICES ----------------
def prices_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📩 Написати мені", url=CONTACT_URL)],
            back_row()
        ]
    )


# ---------------- SHOWREEL ----------------
def showreel_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="▶️ Дивитись шоурил", url=str(SHOWREEL_URL))],
            back_row()
        ]
    )


# ---------------- CATEGORY DATA ----------------
def _categories(section: str):
    return VERTICAL if section == "vertical" else HORIZONTAL


def parse_category_callback(data: str):
    parts = data.split(":")
    if len(parts) != 2:
        return None
    return parts[0], parts[1]


def category_kb(section: str):
    categories = _categories(section)

    rows = [
        [InlineKeyboardButton(text=cat["title"], callback_data=f"{section}:{key}")]
        for key, cat in categories.items()
    ]

    rows.append(back_row())

    return InlineKeyboardMarkup(inline_keyboard=rows)


def videos_kb(section: str, category_key: str):
    categories = _categories(section)
    videos = categories.get(category_key, {}).get("videos", [])

    rows = [
        [InlineKeyboardButton(text=v["title"], url=v["url"])]
        for v in videos if v.get("url")
    ]

    rows.append(back_row())

    return InlineKeyboardMarkup(inline_keyboard=rows)
