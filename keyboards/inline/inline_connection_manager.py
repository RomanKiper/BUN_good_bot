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


def get_inline_connection_kb_manager_second():
    buttons_con = [
        [
            types.InlineKeyboardButton(text="Связаться с менеджером", callback_data="manager"),
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons_con)
    return keyboard


# Клаватура yes no
yes_news_button = InlineKeyboardButton(
    text='Да',
    callback_data='yes_news'
)
no_news_button = InlineKeyboardButton(
    text='Нет, спасибо',
    callback_data='no_news')
keyboard_yes_no: list[list[InlineKeyboardButton]] = [
    [yes_news_button, no_news_button]
]
markup_yes_no = InlineKeyboardMarkup(inline_keyboard=keyboard_yes_no)


# # Клавиатура в блоке прайсы. Для каждого прайса.
# connection_manager_button = InlineKeyboardButton(
#     text='Менедж🤓р',
#     callback_data='manager'
# )
# back_button = InlineKeyboardButton(
#     text='Назад',
#     callback_data='btn_main_menu_1')
# # Добавляем кнопки в клавиатуру в один ряд
# keyboard_yes_no: list[list[InlineKeyboardButton]] = [
#     [connection_manager_button, back_button]
# ]
# # Создаем объект инлайн-клавиатуры
# markup_con_manager_back_button = InlineKeyboardMarkup(inline_keyboard=keyboard_yes_no)
