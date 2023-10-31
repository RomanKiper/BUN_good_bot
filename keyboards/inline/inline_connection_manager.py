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



# Создаем объекты инлайн-кнопок
yes_news_button = InlineKeyboardButton(
    text='Да',
    callback_data='yes_news'
)
no_news_button = InlineKeyboardButton(
    text='Нет, спасибо',
    callback_data='no_news')
# Добавляем кнопки в клавиатуру в один ряд
keyboard_yes_no: list[list[InlineKeyboardButton]] = [
    [yes_news_button, no_news_button]
]
# Создаем объект инлайн-клавиатуры
markup_yes_no = InlineKeyboardMarkup(inline_keyboard=keyboard_yes_no)

