
from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from lexicon.lexicon import LEXICON_RU
from keyboards.inline.inline_media_and_app import inline_list_media, inline_link_download_app


router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=f"{message.from_user.first_name}, {LEXICON_RU['/start']}")


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
    await message.delete()


@router.message(Command(commands='our_media'))
async def get_list_media(message: Message):
    await message.answer(f"Наши медиа!", reply_markup=inline_list_media)
    await message.delete()


@router.message(Command(commands='description'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/description'])
    await message.delete()


@router.message(Command(commands='download_app'))
async def reply_download_app(message: Message):
    await message.answer(text="👇👇Перейди по ссылке👇👇", reply_markup=inline_link_download_app)
    await message.delete()


@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])

















