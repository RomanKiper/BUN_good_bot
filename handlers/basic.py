from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from lexicon.lexicon import LEXICON_RU
from keyboards.inline.inline_main_menu import create_inline_kb_main_menu
from keyboards.inline.inline_employee import inline_kb_employee


router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=f"{message.from_user.first_name}, {LEXICON_RU['/start']}")


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
    await message.delete()



@router.message(Command(commands='main_menu'))
async def get_main_menu(message: Message):
    keyboard = create_inline_kb_main_menu(2, 'btn_main_menu_1', 'btn_main_menu_2', 'btn_main_menu_3', 'btn_main_menu_4',
                                'btn_main_menu_5', 'btn_main_menu_6', 'btn_main_menu_7', 'download_app')
    await message.answer(
        text='В данном блоке вы можете получить базовую инфрмацию о работе с компанией.'
             'Или же можете обратиться для консультации к личному менеджеру 🤓.',
        reply_markup=keyboard
    )
    await message.delete()

    #vkj;zlxkcv


@router.message(Command(commands='employee'))
async def get_main_menu(message: Message):
    await message.answer(
        text='Вы попали в зону ограниченных прав бота BUN_bot. Это означает, что у вас права работника компании. Пользуйтесь возможнстями бота и пишите ваши рекомендации по усовершенствованию бота.',
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
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
