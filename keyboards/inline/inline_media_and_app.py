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
            text="Instagram slivki.by",
            url="https://www.instagram.com/slivkiby/"
        ),
        InlineKeyboardButton(
            text="TikTok",
            url="https://www.tiktok.com/@slivkiby"
        )

    ],
])

inline_link_download_app = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Скачать приложение SLIVKI.BY",
            url="https://www.slivki.by/prilozhenie-skidok"
        )
    ]
])
