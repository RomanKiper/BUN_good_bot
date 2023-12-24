from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_list_media = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="slivki.by",
            url="https://www.slivki.by"
        ),
        InlineKeyboardButton(
            text="Telegram",
            url="https://t.me/slivki_by"
        )
    ],
    [
        InlineKeyboardButton(
            text="Insta slivkiby",
            url="https://www.instagram.com/slivkiby/"
        ),
        InlineKeyboardButton(
            text="TikTok",
            url="https://www.tiktok.com/@slivkiby"
        )
    ],
    [
        InlineKeyboardButton(
            text="Insta Giperspros",
            url="https://www.instagram.com/giperspros/"
        ),
        InlineKeyboardButton(
            text="Slivki_beauty",
            url="https://www.instagram.com/slivkiby_beauty/"
        )
    ],
])

inline_link_download_app = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Скачать приложение SLIVKI.BY",
            url="https://www.slivki.by/prilozhenie-skidok"
        )
    ],
    [
        InlineKeyboardButton(
            text="Назад в меню",
            callback_data="main_menu"
        )
    ]
])
