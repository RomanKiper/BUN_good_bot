from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.inline.inline_media_and_app import inline_link_download_app

router = Router()


# @router.message(Command(commands='download_app'))
@router.callback_query(F.data == 'download_app')
async def reply_download_app(callback: types.CallbackQuery):
    await callback.message.answer (text="👇👇Перейди по ссылке👇👇", reply_markup=inline_link_download_app)
    await callback.message.delete()