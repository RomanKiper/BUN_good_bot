from aiogram import Bot, Dispatcher
from handlers.basic import get_start, get_hello
from aiogram.types import Message, ContentType
import asyncio
import logging
from settings import settings
from aiogram import F
from aiogram.filters import Command
from utils.commands import set_commands
import json


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text="Бот запущен!")


async def stop_bot(bot: Bot):
    await bot.send_message(1006569664, text="Бот остановлен!")


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s -[%(levelname)s] - %(name)s - "
                                "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    bot = Bot(token=settings.bots.bot_token, parse_mode="HTML")
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.startup.register(stop_bot)
    dp.message.register(get_start, Command(commands=['start']))
    dp.message.register(get_hello, F.text == "Привет")
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())