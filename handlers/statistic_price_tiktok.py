from aiogram import Router, F, types, Bot
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon import LEXICON_PRICE
from lexicon.lexicon import LEXICON_btn_main_menu

router = Router()

tiktok1 = LEXICON_PRICE['tiktok1']
tiktok2 = LEXICON_PRICE['tiktok2']



text_pages = [tiktok1, tiktok2]

current_text_index = 0

button_next = InlineKeyboardButton(
    text='Далее',
    callback_data='next_page_tik')
button_prev = InlineKeyboardButton(
    text='Назад',
    callback_data='prev_page_tik')
# button_manager = InlineKeyboardButton(
#     text=LEXICON_btn_main_menu['manager'],
#     callback_data='manager')
button_back_to_preview_menu = InlineKeyboardButton(
    text='Назад в меню',
    callback_data='btn_main_menu_1')
keyboard_prev_next: list[list[InlineKeyboardButton]] = [
    [button_prev, button_next],
    [button_back_to_preview_menu]
]
markup_prev_next_tik_tik = InlineKeyboardMarkup(inline_keyboard=keyboard_prev_next)


@router.callback_query(F.data == 'tiktok_sl')
async def on_start(message: Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id,
                           text=text_pages[current_text_index],
                           reply_markup=markup_prev_next_tik_tik)


# Обработчик инлайн кнопки "Следующеая страница"
@router.callback_query(lambda callback_query: callback_query.data == 'next_page_tik')
async def on_next_photo(callback: types.CallbackQuery, bot: Bot):
    global current_text_index
    current_text_index = (current_text_index + 1) % len(text_pages)
    await bot.edit_message_text(chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id,
                                text=text_pages[current_text_index],
                                reply_markup=markup_prev_next_tik_tik,
                                disable_web_page_preview=True)


# Обработчик инлайн кнопки "Предыдущий техт"
@router.callback_query(lambda callback_query: callback_query.data == 'prev_page_tik')
async def on_prev_photo(callback: types.CallbackQuery, bot: Bot):
    global current_text_index
    current_text_index = (current_text_index - 1) % len(text_pages)
    await bot.edit_message_text(chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id,
                                text=text_pages[current_text_index],
                                reply_markup=markup_prev_next_tik_tik,
                                disable_web_page_preview=True)
