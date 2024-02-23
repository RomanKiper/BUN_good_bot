from aiogram import Router, F, types, Bot
from aiogram.types import (CallbackQuery, InputMediaPhoto)
from aiogram.exceptions import TelegramBadRequest
from lexicon.lexicon import LEXICON_PRICE
from keyboards.inline.inline_price_kb_builder import get_markup_price

router = Router()


@router.callback_query(F.data == "telegram_sl")
async def answer_data_syte(callback: types.CallbackQuery, bot: Bot):
    markup = get_markup_price(2, 'btn_main_menu_1', 'photo_telega')
    await bot.send_photo(chat_id=callback.from_user.id,
                         photo=LEXICON_PRICE['photo_telejka1'],
                         caption=LEXICON_PRICE['telejka_info'],
                         reply_markup=markup)



@router.callback_query(F.data == 'photo_telega')
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = get_markup_price(2, 'btn_main_menu_1', 'photo_telega')
    try:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media=LEXICON_PRICE['photo_tekejka2'],
                caption=LEXICON_PRICE['telejka_info']
            ),
            reply_markup=markup
        )
    except TelegramBadRequest:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media=LEXICON_PRICE['photo_telejka1'],
                caption=LEXICON_PRICE['telejka_info']
            ),
            reply_markup=markup
        )
