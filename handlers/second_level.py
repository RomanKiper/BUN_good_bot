from aiogram import Router, F, types, Bot
from aiogram.types import Message
from keyboards.inline.inline_media_and_app import inline_link_download_app
from keyboards.inline.inline_second_level import inline_links_contract, get_inline_connection_manager
from keyboards.inline.inline_connection_manager import get_inline_connection_kb_manager_second
from lexicon.lexicon import LEXICON_RU

router = Router()


@router.callback_query(F.data == 'download_app')
async def inline_download_app(callback: types.CallbackQuery):
    await callback.message.answer(text="👇👇Перейди по ссылке👇👇", reply_markup=inline_link_download_app)
    await callback.message.delete()

@router.callback_query(F.data == 'btn_main_menu_7')
async def inline_download_app(callback: types.CallbackQuery):
    await callback.message.answer(text="👇👇Сделай выбор друже 👇👇", reply_markup=get_inline_connection_manager())
    await callback.message.delete()

@router.callback_query(F.data == 'btn_main_menu_5')
async def inline_get_office_information(callback: types.CallbackQuery, bot: Bot):
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=53.9077,
                            longitude=27.549731)
    await callback.message.answer(text=LEXICON_RU['/office_adress'],
                                  reply_markup=get_inline_connection_kb_manager_second())
    await callback.message.delete()


@router.callback_query(F.data == 'btn_main_menu_3')
async def inline_get_description_slivki(callback: types.CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['/description_slivki'])
    await callback.message.delete()


@router.callback_query(F.data == 'btn_contract_links')
async def get_contract_links(callback: types.CallbackQuery):
    await callback.message.answer(text="👇👇Выбери договор👇👇", reply_markup=inline_links_contract)
