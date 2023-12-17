from aiogram import Router, F, types, Bot
from aiogram.types import Message, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from lexicon.lexicon import LEXICON_PRICE, LEXICON_btn_main_menu

router = Router()

bloger1 = LEXICON_PRICE['bloger1']
bloger2 = LEXICON_PRICE['bloger2']
bloger3 = LEXICON_PRICE['bloger3']
bloger4 = LEXICON_PRICE['bloger4']
bloger5 = LEXICON_PRICE['bloger5']
bloger6 = LEXICON_PRICE['bloger6']
bloger7 = LEXICON_PRICE['bloger7']


# Список ID фотографий
photo_ids = [bloger1, bloger2, bloger3, bloger4, bloger5, bloger6, bloger7 ]

caption_dict = {
    bloger1: LEXICON_PRICE['bloger_info'],
    bloger2: LEXICON_PRICE['bloger_info1'],
    bloger3: LEXICON_PRICE['bloger_info2'],
    bloger4: LEXICON_PRICE['bloger_info3'],
    bloger5: LEXICON_PRICE['bloger_info4'],
    bloger6: LEXICON_PRICE['bloger_info5'],
    bloger7: LEXICON_PRICE['bloger_info6'],
}

current_photo_index = 0

button_next = InlineKeyboardButton(
    text='ВПЕРЕД',
    callback_data='next_photo_bloger')
button_prev = InlineKeyboardButton(
    text='НАЗАД',
    callback_data='prev_photo_bloger')
button_back_to_preview_menu = InlineKeyboardButton(
    text='Назад в меню',
    callback_data='btn_main_menu_1')
keyboard_prev_next: list[list[InlineKeyboardButton]] = [
    [button_prev, button_next],
    [button_back_to_preview_menu]
]
markup_prev_next_bloger = InlineKeyboardMarkup(inline_keyboard=keyboard_prev_next)


@router.callback_query(F.data == 'btn_main_menu_2')
# async def on_start(message: Message, bot: Bot):
async def on_start(message: Message, bot: Bot):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo_ids[current_photo_index],
                         caption=caption_dict[photo_ids[current_photo_index]],
                         reply_markup=markup_prev_next_bloger)


# Обработчик инлайн кнопки "Следующее фото"
@router.callback_query(lambda callback_query: callback_query.data == 'next_photo_bloger')
async def on_next_photo(callback: types.CallbackQuery, bot: Bot):
    global current_photo_index
    current_photo_index = (current_photo_index + 1) % len(photo_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaPhoto(
                                     media=photo_ids[current_photo_index],
                                     caption=caption_dict[photo_ids[current_photo_index]],
                                 ),
                                 reply_markup=markup_prev_next_bloger)


# Обработчик инлайн кнопки "Предыдущее фото"
@router.callback_query(lambda callback_query: callback_query.data == 'prev_photo_bloger')
async def on_prev_photo(callback: types.CallbackQuery, bot: Bot):
    global current_photo_index
    current_photo_index = (current_photo_index - 1) % len(photo_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaPhoto(
                                     media=photo_ids[current_photo_index],
                                     caption=caption_dict[photo_ids[current_photo_index]],
                                 ),
                                 reply_markup=markup_prev_next_bloger)
