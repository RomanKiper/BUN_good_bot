import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from sqlalchemy import URL

import db.user

from config_data.config import Config, load_config
from keyboards.main_meny import set_main_menu
from db import create_async_engine, get_session_maker
from handlers import basic, list_links, second_level, connection_manager, fsm_file, \
    statistic_price_telegram, statistic_price_site, statistic_price_insta


logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token,
              parse_mode='HTML')
    dp = Dispatcher()
    # dp.message.middleware(Registration_check)
    # dp.callback_query.middleware(Registration_check)

    await set_main_menu(bot)

    postger_url = URL.create(
        "postgresql+asyncpg",
        username=os.getenv("DATABASE_USERNAME"),
        password=os.getenv("DATABASE_PASSWORD"),
        host=os.getenv("DATABASE_HOST"),
        port=os.getenv("DATABASE_PORT"),
        database=os.getenv("DATABASE_NAME")
    )

    print(postger_url)

    async_engine = create_async_engine(postger_url)
    session_maker = get_session_maker(async_engine)
    # Делегирвано alembic
    # await proceed_schemas(async_engine, BaseModel.metadata)

    # Регистриуем роутеры в диспетчере
    dp.include_router(statistic_price_telegram.router)
    dp.include_router(statistic_price_insta.router)
    dp.include_router(statistic_price_site.router)
    dp.include_router(fsm_file.router)
    dp.include_router(connection_manager.router)
    dp.include_router(second_level.router)
    dp.include_router(list_links.router)
    dp.include_router(basic.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, session_maker=session_maker)


if __name__ == '__main__':
    asyncio.run(main())
