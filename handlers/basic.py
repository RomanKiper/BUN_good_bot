from aiogram import Router, F, types, Bot
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from lexicon.lexicon import LEXICON_RU
from keyboards.inline.inline_main_second_menu import create_inline_kb_main_menu, create_inline_kb_second_menu
from keyboards.inline.inline_employee import inline_kb_employee
from aiogram.types import ContentType

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer_sticker("CAACAgIAAxkBAAEKq3ZlQ_rDGclAu2sg_OVA3KU0xmNaLwACNhYAAnJroEul2k1dhz9kKTME")
    await message.answer(text=f"{message.from_user.first_name}, {LEXICON_RU['/start']}")
    await message.delete()


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
    await message.delete()


@router.message(Command(commands='main_menu'))
async def get_main_menu(message: Message):
    keyboard = create_inline_kb_main_menu(2, 'btn_main_menu_1', 'btn_main_menu_2', 'btn_main_menu_3', 'btn_main_menu_4',
                                          'btn_main_menu_5', 'btn_contract_links', 'manager', 'download_app')
    await message.answer(
        text='В данном блоке вы можете получить базовую инфрмацию о работе с компанией.'
             'Или же можете обратиться для консультации к личному менеджеру 🤓.',
        reply_markup=keyboard
    )
    await message.delete()


@router.callback_query(F.data == "btn_main_menu_1")
async def get_second_menu(callback: types.CallbackQuery):
    keyboard = create_inline_kb_second_menu(2, 'site_slivki_advertising', 'site_slivki_promotion', 'instagram_sl', 'telegram_sl', 'tiktok_sl',
                                            'app_advertising', 'others_media', 'regions_sl')
    await callback.message.answer(text='В данном разделе ты получишь цены, статистику и примеры размещения рекламы.',
                                  reply_markup=keyboard)
    await callback.message.delete()


@router.message(Command(commands='employee'))
async def get_main_menu(message: Message):
    await message.answer(
        text='Вы попали в зону ограниченных прав бота BUN_bot❌. Это означает, что у вас права работника компании.'
             ' Пользуйтесь возможнстями бота и пишите ваши рекомендации по усовершенствованию бота.',
        reply_markup=inline_kb_employee
    )
    await message.delete()


@router.message(Command(commands='description'))
async def get_description(message: Message):
    await message.answer(text=LEXICON_RU['/description'])
    await message.delete()


@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
        photo_id = message.photo[0].file_id
        await message.answer(f"ID фотографии: {photo_id}")
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
