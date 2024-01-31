from aiogram import Router, F, types, Bot
from aiogram.types import Message, InputMediaVideo, InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon import LEXICON_btn_reviews

router = Router()

video_elect1 = LEXICON_btn_reviews['video_elect1']
video_elect2 = LEXICON_btn_reviews['video_elect2']


video_ids = [video_elect1, video_elect2 ]

caption_dict = {
    video_elect1: LEXICON_btn_reviews['video_elect_info1'],
    video_elect2: LEXICON_btn_reviews['video_elect_info2'],
}

current_video_index = 0

button_next = InlineKeyboardButton(
    text='ВПЕРЕД',
    callback_data='next_video_elect')
button_prev = InlineKeyboardButton(
    text='НАЗАД',
    callback_data='prev_video_elect')
button_back_to_preview_menu = InlineKeyboardButton(
    text='Назад в меню',
    callback_data='reviews')
keyboard_prev_next: list[list[InlineKeyboardButton]] = [
    [button_prev, button_next],
    [button_back_to_preview_menu]
]
markup_prev_next_bilding = InlineKeyboardMarkup(inline_keyboard=keyboard_prev_next)


@router.callback_query(F.data == 'review_electronics')
async def on_start(message: Message, bot: Bot):
    await bot.send_video(chat_id=message.from_user.id,
                         video=video_ids[current_video_index],
                         caption=caption_dict[video_ids[current_video_index]],
                         reply_markup=markup_prev_next_bilding)


@router.callback_query(lambda callback_query: callback_query.data == 'next_video_elect')
async def on_next_photo(callback: types.CallbackQuery, bot: Bot):
    global current_video_index
    current_video_index = (current_video_index + 1) % len(video_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaVideo(
                                     media=video_ids[current_video_index],
                                     caption=caption_dict[video_ids[current_video_index]],
                                 ),
                                 reply_markup=markup_prev_next_bilding)


@router.callback_query(lambda callback_query: callback_query.data == 'prev_video_elect')
async def on_prev_photo(callback: types.CallbackQuery, bot: Bot):
    global current_video_index
    current_video_index = (current_video_index - 1) % len(video_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaVideo(
                                     media=video_ids[current_video_index],
                                     caption=caption_dict[video_ids[current_video_index]],
                                 ),
                                 reply_markup=markup_prev_next_bilding)