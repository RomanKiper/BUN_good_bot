from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command="main_menu",
            description="ГЛАВНОЕ МЕНЮ"
        ),
        BotCommand(
            command="description_bot",
            description="Описание бота ✏"
        ),
        BotCommand(
            command="our_media",
            description="Наши медиа 🌐"
        ),
        BotCommand(
            command="download_app",
            description="Скачать приложение 💾"
        ),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
