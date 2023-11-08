from aiogram import Router, F, types, Bot
from aiogram.types import (CallbackQuery, InputMediaPhoto)
from aiogram.exceptions import TelegramBadRequest
from lexicon.lexicon import LEXICON_PRICE
from keyboards.inline.inline_price_kb_builder import get_markup_price
from keyboards.inline.inline_connection_manager import markup_con_manager_back_button

router = Router()


@router.callback_query(F.data == "site_slivki")
async def answer_data_syte(callback: types.CallbackQuery, bot: Bot):
    markup = get_markup_price(2, 'photo_site')
    await bot.send_photo(chat_id=callback.from_user.id,
                         photo=LEXICON_PRICE['photo_podlojka1'],
                         caption='CTR - 0.17% / CPM - 16,65 бел.руб.',
                         reply_markup=markup)
    await callback.message.answer(text=LEXICON_PRICE['podlojka_info'],reply_markup=markup_con_manager_back_button, disable_web_page_preview=True)



@router.callback_query(F.data == 'photo_site')
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = get_markup_price(2, 'photo_site')
    try:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media=LEXICON_PRICE['photo_podlojka2'],
                caption='Размещается как в десктопной так и в мобильной версиях'
            ),
            reply_markup=markup
        )
    except TelegramBadRequest:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media=LEXICON_PRICE['photo_podlojka1'],
                caption='CTR - 0.17% / CPM - 16,65 бел.руб.'
            ),
            reply_markup=markup
        )
