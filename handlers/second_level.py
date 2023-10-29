from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.inline.inline_media_and_app import inline_link_download_app
from keyboards.inline.inline_second_level import inline_links_contract, get_inline_connection_manager
from lexicon.lexicon import LEXICON_RU

router = Router()


@router.callback_query(F.data == 'download_app')
async def inline_download_app(callback: types.CallbackQuery):
    await callback.message.answer(text="👇👇Перейди по ссылке👇👇", reply_markup=inline_link_download_app)


@router.callback_query(F.data == 'btn_main_menu_7')
async def inline_download_app(callback: types.CallbackQuery):
    await callback.message.answer(text="👇👇Сделай выбор друже 👇👇", reply_markup=get_inline_connection_manager())


@router.callback_query(F.data == 'btn_main_menu_3')
async def inline_get_description_slivki(callback: types.CallbackQuery):
    await callback.message.answer(text=LEXICON_RU['/description_slivki'])


@router.callback_query(F.data == 'btn_contract_links')
async def get_contract_links(callback: types.CallbackQuery):
    await callback.message.answer(text="👇👇Выбери договор👇👇", reply_markup=inline_links_contract)
