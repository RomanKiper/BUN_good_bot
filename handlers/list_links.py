from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from keyboards.inline.inline_media_and_app import inline_list_media

router = Router()


@router.message(Command(commands='our_media'))
async def get_list_media(message: Message):
    await message.answer(f"Ссылки на наши медиа!", reply_markup=inline_list_media)
    await message.delete()


@router.message(Command(commands='insta_links'))
async def process_link_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/insta_links'],
        disable_web_page_preview=True
    )
    await message.delete()


@router.message(Command(commands='tiktok_links'))
async def process_link_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/tiktok_links'],
        disable_web_page_preview=True
    )
    await message.delete()


@router.message(Command(commands='tglink'))
async def process_tglink_command(message: Message):
    await message.answer(
        text='<a href="https://web.telegram.org/k/#@slivki_by">telegram.org/k/#@slivki_by</a>')
    await message.delete()