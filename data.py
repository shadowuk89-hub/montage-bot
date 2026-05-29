"""Портфоліо: категорії та відео."""

from typing import TypedDict


class Video(TypedDict):
    title: str
    url: str


class Category(TypedDict):
    title: str
    videos: list[Video]


SHOWREEL_URL: str = "https://www.youtube.com/watch?v=suhJqywZlm8"

# --- Вертикальні відео ---

VERTICAL: dict[str, Category] = {
    "ai": {
        "title": "🤖 ШІ",
        "videos": [
            {"title": "ІІ", "url": "https://www.youtube.com/shorts/itocDkVfkHo"},
        ],
    },
    "football": {
        "title": "⚽ Футбол",
        "videos": [
            {"title": "Футбол", "url": "https://www.youtube.com/shorts/02HpuCf0fGY"},
        ],
    },
    "auto": {
        "title": "🚗 Авто",
        "videos": [
            {
                "title": "Машина edit",
                "url": "https://youtube.com/shorts/JBBnTnvMLZ8",
            },
        ],
    },
    "bloggers": {
        "title": "👨‍💼 Блогери",
        "videos": [
            {
                "title": "Огляд годинника",
                "url": "https://youtube.com/shorts/VTaHJNUSpLc",
            },
            {"title": "Продажі", "url": "https://youtube.com/shorts/V1FklajQqJk"},
            {
                "title": "Маркетинг",
                "url": "https://youtube.com/shorts/HRXhMVkj5jY",
            },
            {
                "title": "Тревел vlog",
                "url": "https://www.youtube.com/shorts/Sm3y6X4dpzU",
            },
            {
                "title": "Співачка",
                "url": "https://www.youtube.com/shorts/kktz3EzlX_g",
            },
        ],
    },
}

# --- Горизонтальні відео ---

HORIZONTAL: dict[str, Category] = {
    "entertainment": {
        "title": "🎭 Розважальні відео",
        "videos": [
            {
                "title": "Шар із фольги",
                "url": "https://www.youtube.com/watch?v=hgudQksW3wQ",
            },
            {
                "title": "Гігантський спінер",
                "url": "https://www.youtube.com/watch?v=0KO2RI-FonI",
            },
            {
                "title": "Виживання",
                "url": "https://www.youtube.com/watch?v=S2A9C65QE9E",
            },
            {
                "title": "Монстри",
                "url": "https://www.youtube.com/watch?v=qlOIsJdO5TE",
            },
        ],
    },
    "real_estate": {
        "title": "🏠 Нерухомість",
        "videos": [
            {
                "title": "Нерухомість",
                "url": "https://youtu.be/9wJvrernhkw?list=PLwL5C5aCIGqLG2xGdAiOQ5ujW39qfB_uk",
            },
        ],
    },
    "auto_reviews": {
        "title": "🚘 Автоогляди",
        "videos": [
            {
                "title": "HiPhi Z",
                "url": "https://www.youtube.com/watch?v=92CFPcKBznM",
            },
            {
                "title": "FORD RANGER",
                "url": "https://www.youtube.com/watch?v=ftGMGyDcEvA",
            },
        ],
    },
    "interviews": {
        "title": "🎤 Інтерв'ю",
        "videos": [
            {
                "title": "Інтерв'ю",
                "url": "https://youtu.be/WhFjHb-2NIU",
            },
        ],
    },
    "reviews": {
        "title": "🧠 Огляди",
        "videos": [
            {
                "title": "Новий пошуковик",
                "url": "https://youtu.be/rDj25quqtpw?list=PLk2VXM1fgc0G2LvXoEDE655XU690dT96y",
            },
        ],
    },
    "crypto": {
        "title": "₿ Крипта",
        "videos": [
            {
                "title": "Крипта в масці",
                "url": "https://www.youtube.com/watch?v=kywhTJ3DSU4",
            },
            {
                "title": "ANTMINER S21 188",
                "url": "https://youtu.be/OPR9cuZ1Ysk",
            },
            {
                "title": "SMA курс",
                "url": "https://www.youtube.com/watch?v=MKT5nJNzy1I",
            },
        ],
    },
    "psychology": {
        "title": "📚 Психологія та історія",
        "videos": [
            {
                "title": "СТЕПАНІВ І ДАШКЕВИЧ: ЛЮБОВ НА ВІЙНІ",
                "url": "https://youtu.be/V1roG0MEvuY?list=PLk2VXM1fgc0G2LvXoEDE655XU690dT96y",
            },
            {
                "title": "ОЛЬГА КОБИЛЯНСЬКА",
                "url": "https://youtu.be/HbD4JQ3c7fE?list=PLk2VXM1fgc0G2LvXoEDE655XU690dT96y",
            },
        ],
    },
    "history": {
        "title": "⚔️ Історія",
        "videos": [
            {
                "title": "Суд над тваринами",
                "url": "https://youtu.be/51vEGMp-pyY?list=PLk2VXM1fgc0G2LvXoEDE655XU690dT96y",
            },
            {
                "title": "Спарта",
                "url": "https://www.youtube.com/watch?v=P1M6u7uXZJQ",
            },
        ],
    },
}
