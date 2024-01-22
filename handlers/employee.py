from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import Message
from config_data.config import load_config, Config
from keyboards.inline.inline_employee import inline_kb_employee
from keyboards.inline.inline_employee import inline_kb_working_links
from lexicon.lexicon import LEXICON_RU

router = Router()

config: Config = load_config()
lst_admin_ids = config.tg_bot.admin_ids


@router.message(Command(commands='employee'))
async def get_main_menu(message: Message):
    if message.from_user.id in lst_admin_ids:
        await message.answer(
            text='У вас права работника компании.'
                 ' Пользуйтесь возможнстями бота и пишите ваши рекомендации по усовершенствованию бота.',
            reply_markup=inline_kb_employee
        )
        await message.delete()
    else:
        await message.answer(text="Нет прав доступа. Запросите права у администатора.")
        await message.delete()


@router.callback_query(F.data=='employee')
async def get_main_menu_2(callback: types.CallbackQuery):
    if callback.message.from_user.id in lst_admin_ids:
        await callback.message.answer(
            text='У вас права работника компании.'
                 ' Пользуйтесь возможнстями бота и пишите ваши рекомендации по усовершенствованию бота.',
            reply_markup=inline_kb_employee
        )
        await callback.message.delete()
    else:
        await callback.message.answer(text="Нет прав доступа. Запросите права у администатора.")
        await callback.message.delete()


@router.callback_query(F.data == 'work_links')
async def inline_download_work_links(callback: types.CallbackQuery):
    await callback.message.answer(text="👇👇Рабочие ссылки👇👇", reply_markup=inline_kb_working_links)
    await callback.message.delete()


@router.callback_query(F.data == 'tiktok_links')
async def process_link_command(callback: types.CallbackQuery):
    await callback.message.answer(
        text=LEXICON_RU['/tiktok_links'],
        disable_web_page_preview=True
    )


@router.callback_query(F.data == 'insta_links')
async def process_link_command(callback: types.CallbackQuery):
    await callback.message.answer(
        text=LEXICON_RU['/insta_links'],
        disable_web_page_preview=True
    )

@router.callback_query(F.data == 'school')
async def get_school_document(callback: types.CallbackQuery):
    await callback.message.answer(
        text='Данный раздел находится в разработке.'
    )

@router.callback_query(F.data == 'improvements')
async def get_improvements(callback: types.CallbackQuery):
    await callback.message.answer(
        text='Данный раздел находится в разработке.'
    )