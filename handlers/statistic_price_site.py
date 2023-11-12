from aiogram import Router, F, types, Bot
from aiogram.types import Message, InputMediaPhoto
from keyboards.inline.inline_price_kb_builder import markup_prev_next
from lexicon.lexicon import LEXICON_PRICE


router = Router()

photo_podlojka1 = LEXICON_PRICE['photo_podlojka1']
photo_podlojka2 = LEXICON_PRICE['photo_podlojka2']

# Список ID фотографий
photo_ids = [photo_podlojka1, photo_podlojka2]

caption_dict = {
    photo_podlojka1: LEXICON_PRICE['podlojka_info'],
    photo_podlojka2: LEXICON_PRICE['podlojka_info'],
}

current_photo_index = 0


@router.callback_query(F.data == 'site_slivki')
async def on_start(message: Message, bot: Bot):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo_ids[current_photo_index],
                         caption=caption_dict[photo_ids[current_photo_index]],
                         reply_markup=markup_prev_next)


# Обработчик инлайн кнопки "Следующее фото"
@router.callback_query(lambda callback_query: callback_query.data == 'next_photo')
async def on_next_photo(callback: types.CallbackQuery, bot: Bot):
    global current_photo_index
    current_photo_index = (current_photo_index + 1) % len(photo_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaPhoto(
                                     media=photo_ids[current_photo_index],
                                     caption=caption_dict[photo_ids[current_photo_index]],
                                 ),
                                 reply_markup=markup_prev_next)


# Обработчик инлайн кнопки "Предыдущее фото"
@router.callback_query(lambda callback_query: callback_query.data == 'prev_photo')
async def on_prev_photo(callback: types.CallbackQuery, bot: Bot):
    global current_photo_index
    current_photo_index = (current_photo_index - 1) % len(photo_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaPhoto(
                                     media=photo_ids[current_photo_index],
                                     caption=caption_dict[photo_ids[current_photo_index]],
                                 ),
                                 reply_markup=markup_prev_next)
