import json

from aiogram import Bot
from aiogram.types import Message

from aiogram.types import BotCommand, BotCommandScopeDefault

async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f"Привет {message.from_user.first_name}. Рад тебя видеть!")



async def get_hello(message: Message, bot: Bot):
    await message.answer(f"И тебе привет!")
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)












