from aiogram import Router, types, Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon import LEXICON_btn_faq

router = Router()

list_faq = ["faq_1", "faq_2", "faq_3"]

button_back = InlineKeyboardButton(
    text='Другие вопросы.',
    callback_data='btn_main_menu_4')

keyboard_back_to_faq: list[list[InlineKeyboardButton]] = [
    [button_back],

]
markup_back_to_faq = InlineKeyboardMarkup(inline_keyboard=keyboard_back_to_faq)


@router.callback_query(lambda callback_query: callback_query.data == callback_query.data in list_faq)
async def get_faq_text(callback: types.CallbackQuery, bot: Bot):
    if callback.data == "faq_1":
        await bot.send_message(chat_id=callback.from_user.id,
                               text=LEXICON_btn_faq['faq_1_info'],
                               reply_markup=markup_back_to_faq)
        await callback.message.delete()
    elif callback.data == "faq_2":
        await bot.send_message(chat_id=callback.from_user.id,
                               text=LEXICON_btn_faq['faq_2_info'],
                               reply_markup=markup_back_to_faq)
        await callback.message.delete()
    elif callback.data == "faq_3":
        await bot.send_message(chat_id=callback.from_user.id,
                               text=LEXICON_btn_faq['faq_3_info'],
                               reply_markup=markup_back_to_faq)
        await callback.message.delete()
