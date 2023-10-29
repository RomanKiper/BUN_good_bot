from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_links_contract = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Договор оферта инстаграм",
            url="https://www.slivki.by/dogovor-oferta-instagram"
        )
    ],
    [
        InlineKeyboardButton(
            text="Публичный дог-р оказания рекл-х услуг",
            url="https://www.slivki.by/publichnyj-dogovor-okazaniya-reklamnyh-uslug-i-razmesheniya-akcij"
        )
    ]
])

inline_kb_prices_statistics = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="САЙТ slivki.by",
            callback_data='site_slivki'
        )
    ],
    [
        InlineKeyboardButton(
            text="Instagram",
            callback_data='instagram_slivki'
        )
    ],
    [
        InlineKeyboardButton(
            text="TikTok",
            callback_data='tiktok_slivki'
        )
    ],
    [
        InlineKeyboardButton(
            text="Telegram",
            callback_data='telegram_slivki'
        )
    ],
    [
        InlineKeyboardButton(
            text="Другие сети",
            callback_data='others_media'
        )
    ],
    [
        InlineKeyboardButton(
            text="Регионы",
            callback_data='regions'
        )
    ],
])


def get_inline_connection_manager():
    buttons_con = [
        [
            types.InlineKeyboardButton(text="Позвонить", callback_data="connect1"),
            types.InlineKeyboardButton(text="Написать в TG", callback_data="connect2")
        ],
        [types.InlineKeyboardButton(text="Свяжитесь со мной", callback_data="connect3")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons_con)
    return keyboard


