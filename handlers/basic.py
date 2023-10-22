
from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from lexicon.lexicon import LEXICON_RU
from keyboards.inline.inline_1 import inline_list_media


router = Router()




@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])



@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])

@router.message(Command(commands='our_media'))
async def get_list_media(message: Message):
    await message.answer(f"Наши медиа!", reply_markup=inline_list_media)
    await message.delete()


@router.message(Command(commands='description'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/description'])


@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])

















