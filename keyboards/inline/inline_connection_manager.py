from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


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
