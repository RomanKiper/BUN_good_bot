from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU

router = Router()


@router.message(Command(commands='insta_links'))
async def process_link_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/insta_links']
    )
    await message.delete()


@router.message(Command(commands='tiktok_links'))
async def process_link_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/tiktok_links']
    )
    await message.delete()



@router.message(Command(commands='tglink'))
async def process_tglink_command(message: Message):
    await message.answer(
        text='<a href="https://web.telegram.org/k/#@slivki_by">telegram.org/k/#@slivki_by</a>'
    )