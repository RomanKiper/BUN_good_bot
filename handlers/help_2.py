from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from lexicon.lexicon import LEXICON_HELP_2

router = Router()


@router.message(Command(commands='help2'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_HELP_2['/help_2'])
    await message.delete()


@router.message(Command(commands='info_promo'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_HELP_2['/info_promo'])
    await message.delete()
