from aiogram import Router, F, types, Bot
from aiogram.types import Message, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from lexicon.lexicon import LEXICON_PRICE, LEXICON_btn_main_menu

router = Router()

app1 = LEXICON_PRICE['app1']
app2 = LEXICON_PRICE['app2']
app3 = LEXICON_PRICE['app3']
app4 = LEXICON_PRICE['app4']


# Список ID фотографий
photo_ids = [app1, app2, app3, app4]

caption_dict = {
    app1: LEXICON_PRICE['app_info1'],
    app2: LEXICON_PRICE['app_info2'],
    app3: LEXICON_PRICE['app_info3'],
    app4: LEXICON_PRICE['app_info4'],
}

current_photo_index = 0

button_next = InlineKeyboardButton(
    text='ВПЕРЕД',
    callback_data='next_photo_app')
button_prev = InlineKeyboardButton(
    text='НАЗАД',
    callback_data='prev_photo_app')
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
markup_prev_next_app = InlineKeyboardMarkup(inline_keyboard=keyboard_prev_next)


@router.callback_query(F.data == 'app_advertising')
# async def on_start(message: Message, bot: Bot):
async def on_start(message: Message, bot: Bot):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo_ids[current_photo_index],
                         caption=caption_dict[photo_ids[current_photo_index]],
                         reply_markup=markup_prev_next_app)


# Обработчик инлайн кнопки "Следующее фото"
@router.callback_query(lambda callback_query: callback_query.data == 'next_photo_app')
async def on_next_photo(callback: types.CallbackQuery, bot: Bot):
    global current_photo_index
    current_photo_index = (current_photo_index + 1) % len(photo_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaPhoto(
                                     media=photo_ids[current_photo_index],
                                     caption=caption_dict[photo_ids[current_photo_index]],
                                 ),
                                 reply_markup=markup_prev_next_app)


# Обработчик инлайн кнопки "Предыдущее фото"
@router.callback_query(lambda callback_query: callback_query.data == 'prev_photo_app')
async def on_prev_photo(callback: types.CallbackQuery, bot: Bot):
    global current_photo_index
    current_photo_index = (current_photo_index - 1) % len(photo_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaPhoto(
                                     media=photo_ids[current_photo_index],
                                     caption=caption_dict[photo_ids[current_photo_index]],
                                 ),
                                 reply_markup=markup_prev_next_app)
