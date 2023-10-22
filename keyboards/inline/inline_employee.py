from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_kb_employee = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Конструктор КП",
            callback_data='offer_maker'
        )
    ],
    [
        InlineKeyboardButton(
            text="Примеры КП",
            callback_data='examples_pdf'
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