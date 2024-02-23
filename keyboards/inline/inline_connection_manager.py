from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

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


def get_inline_connection_kb_manager_second():
    buttons_con = [
        # [
        #     types.InlineKeyboardButton(text="Связаться с менеджером🤓",
        #                                callback_data="manager"),
        # ],
        [
            types.InlineKeyboardButton(text="Назад в меню",
                                       callback_data="main_menu"),
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons_con)
    return keyboard


# Блок для связи с мененеджерм. Отключил.
#
# def get_inline_connection_manager():
#     buttons_con = [
#         [
#             types.InlineKeyboardButton(text="Позвонить", callback_data="connect1"),
#             types.InlineKeyboardButton(text="Написать в TG", callback_data="connect2")
#         ],
#         [types.InlineKeyboardButton(text="Свяжитесь со мной", callback_data="connect3")]
#     ]
#     keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons_con)
#     return keyboard


