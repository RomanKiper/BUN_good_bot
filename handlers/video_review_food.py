from aiogram import Router, F, types, Bot
from aiogram.types import Message, InputMediaVideo, InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon import LEXICON_btn_reviews

router = Router()

video_food1 = LEXICON_btn_reviews['video_food1']
video_food2 = LEXICON_btn_reviews['video_food2']



video_ids = [video_food1, video_food2]

caption_dict = {
    video_food1: LEXICON_btn_reviews['video_food_info1'],
    video_food2: LEXICON_btn_reviews['video_food_info2'],
}

current_video_index = 0

button_next = InlineKeyboardButton(
    text='ВПЕРЕД',
    callback_data='next_video_food')
button_prev = InlineKeyboardButton(
    text='НАЗАД',
    callback_data='prev_video_food')
button_back_to_preview_menu = InlineKeyboardButton(
    text='Назад в меню',
    callback_data='reviews')
keyboard_prev_next: list[list[InlineKeyboardButton]] = [
    [button_prev, button_next],
    [button_back_to_preview_menu]
]
markup_prev_next_bilding = InlineKeyboardMarkup(inline_keyboard=keyboard_prev_next)


@router.callback_query(F.data == 'review_food')
async def on_start(message: Message, bot: Bot):
    await bot.send_video(chat_id=message.from_user.id,
                         video=video_ids[current_video_index],
                         caption=caption_dict[video_ids[current_video_index]],
                         reply_markup=markup_prev_next_bilding)


@router.callback_query(lambda callback_query: callback_query.data == 'next_video_food')
async def on_next_video(callback: types.CallbackQuery, bot: Bot):
    global current_video_index
    current_video_index = (current_video_index + 1) % len(video_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaVideo(
                                     media=video_ids[current_video_index],
                                     caption=caption_dict[video_ids[current_video_index]],
                                 ),
                                 reply_markup=markup_prev_next_bilding)


@router.callback_query(lambda callback_query: callback_query.data == 'prev_video_food')
async def on_prev_video(callback: types.CallbackQuery, bot: Bot):
    global current_video_index
    current_video_index = (current_video_index - 1) % len(video_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaVideo(
                                     media=video_ids[current_video_index],
                                     caption=caption_dict[video_ids[current_video_index]],
                                 ),
                                 reply_markup=markup_prev_next_bilding)
