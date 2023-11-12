from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_PRICE, LEXICON_btn_main_menu

def get_markup_price(width: int, *args, **kwargs) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON_PRICE[button] if button in LEXICON_PRICE else button,
                callback_data=button
            ))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button
            ))
    kb_builder.row(*buttons, width=width)
    return kb_builder.as_markup()

#➡⬅👉👈
#Клавиатура для statistic_price_site
button_next = InlineKeyboardButton(
    text='ВПЕРЕД',
    callback_data='next_photo')
button_prev = InlineKeyboardButton(
    text='НАЗАД',
    callback_data='prev_photo')
button_manager = InlineKeyboardButton(
    text=LEXICON_btn_main_menu['manager'],
    callback_data='manager')
button_back_to_preview_menu = InlineKeyboardButton(
    text='Назад в меню',
    callback_data='btn_main_menu_1')
keyboard_prev_next: list[list[InlineKeyboardButton]] = [
    [button_prev, button_next],
    [button_manager, button_back_to_preview_menu]
]
markup_prev_next = InlineKeyboardMarkup(inline_keyboard=keyboard_prev_next)
