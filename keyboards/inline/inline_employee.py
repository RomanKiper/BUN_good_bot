from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_kb_employee = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Рабочие таблицы",
            callback_data='tables_links'
        )
    ],
    [
        InlineKeyboardButton(
            text="Рабочие ссылки",
            callback_data='work_links'
        )
    ],
    [
        InlineKeyboardButton(
            text="Школа📝",
            callback_data='school'
        )
    ],
    [
        InlineKeyboardButton(
            text="Апгрейд🚀",
            callback_data='improvements'
        )
    ],

])


inline_kb_working_links = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Ссылки Insta",
            callback_data='insta_links'
        )
    ],
    [
        InlineKeyboardButton(
            text="Ссылки TikTok",
            callback_data='tiktok_links'
        )
    ],
    [
        InlineKeyboardButton(
            text="Назад в меню",
            callback_data='employee'
        )
    ],
])

inline_kb_main_employee = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Назад в меню",
            callback_data='employee'
        )
    ],
])
