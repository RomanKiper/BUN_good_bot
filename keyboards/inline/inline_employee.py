from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_kb_employee = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Полезные ссылки",
            callback_data='useful_links'
        )
    ],
    [
        InlineKeyboardButton(
            text="Рабочие таблицы",
            callback_data='tables_links'
        )
    ],
    [
        InlineKeyboardButton(
            text="Школа",
            callback_data='school'
        )
    ],
    [
        InlineKeyboardButton(
            text="Обновления",
            callback_data='improvements'
        )
    ],

])
