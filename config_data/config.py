import os
from dataclasses import dataclass

from pathlib import Path

from dotenv import load_dotenv

from environs import Env


# DATABASE_URL = f'{os.getenv("DATABASE_USERNAME")}:{os.getenv("DATABASE_PASSWORD")}@{os.getenv("DATABASE_HOST")}' \
#                f':{os.getenv("DATABASE_PORT")}/{os.getenv("DATABASE_NAME")}'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'lms2',
#         'USER': 'dev',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
#
# DATABASE_URL = f'postgres:postgres@{os.getenv("DATABASE_HOST")}' \
#                f':{os.getenv("DATABASE_PORT")}/{os.getenv("DATABASE_NAME")}'
#
# print(DATABASE_URL)


@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot


# Создаем функцию, которая будет читать файл .env и возвращать
# экземпляр класса Config с заполненными полями token и admin_ids
def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_IDS')))
        )
    )