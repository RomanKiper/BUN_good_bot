from aiogram import Router, F, types, Bot
from aiogram.types import Message, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from lexicon.lexicon import LEXICON_PRICE, LEXICON_btn_main_menu

router = Router()

insta1 = LEXICON_PRICE['insta1']
insta2 = LEXICON_PRICE['insta2']
insta3 = LEXICON_PRICE['insta3']
insta4 = LEXICON_PRICE['insta4']
insta5 = LEXICON_PRICE['insta5']
insta6 = LEXICON_PRICE['insta6']
insta7 = LEXICON_PRICE['insta7']
insta8 = LEXICON_PRICE['insta8']
insta9 = LEXICON_PRICE['insta9']
insta10 = LEXICON_PRICE['insta10']


# Список ID фотографий
photo_ids = [insta1, insta2, insta3, insta4, insta5, insta6, insta7, insta8, insta9, insta10]

caption_dict = {
    insta1: LEXICON_PRICE['insta_info'],
    insta2: LEXICON_PRICE['insta_info2'],
    insta3: LEXICON_PRICE['insta_info3'],
    insta4: LEXICON_PRICE['insta_info4'],
    insta5: LEXICON_PRICE['insta_info5'],
    insta6: LEXICON_PRICE['insta_info6'],
    insta7: LEXICON_PRICE['insta_info7'],
    insta8: LEXICON_PRICE['insta_info8'],
    insta9: LEXICON_PRICE['insta_info9'],
    insta10: LEXICON_PRICE['insta_info10'],
}

current_photo_index = 0


button_next = InlineKeyboardButton(
    text='ВПЕРЕД',
    callback_data='next_photo_insta')
button_prev = InlineKeyboardButton(
    text='НАЗАД',
    callback_data='prev_photo_insta')
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
markup_prev_next_insta = InlineKeyboardMarkup(inline_keyboard=keyboard_prev_next)


@router.callback_query(F.data == 'instagram_sl')
# async def on_start(message: Message, bot: Bot):
async def on_start(message: Message, bot: Bot):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo_ids[current_photo_index],
                         caption=caption_dict[photo_ids[current_photo_index]],
                         reply_markup=markup_prev_next_insta)


# Обработчик инлайн кнопки "Следующее фото"
@router.callback_query(lambda callback_query: callback_query.data == 'next_photo_insta')
async def on_next_photo(callback: types.CallbackQuery, bot: Bot):
    global current_photo_index
    current_photo_index = (current_photo_index + 1) % len(photo_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaPhoto(
                                     media=photo_ids[current_photo_index],
                                     caption=caption_dict[photo_ids[current_photo_index]],
                                 ),
                                 reply_markup=markup_prev_next_insta)
    


# Обработчик инлайн кнопки "Предыдущее фото"
@router.callback_query(lambda callback_query: callback_query.data == 'prev_photo_insta')
async def on_prev_photo(callback: types.CallbackQuery, bot: Bot):
    global current_photo_index
    current_photo_index = (current_photo_index - 1) % len(photo_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaPhoto(
                                     media=photo_ids[current_photo_index],
                                     caption=caption_dict[photo_ids[current_photo_index]],
                                 ),
                                 reply_markup=markup_prev_next_insta)
