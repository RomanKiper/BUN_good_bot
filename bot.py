import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from keyboards.main_meny import set_main_menu
from handlers import basic, list_links, second_level, connection_manager, fsm_file, \
    statistic_price_telegram, statistic_price_site, statistic_price_insta, statistic_price_action, \
    statistic_price_app, employee, blogers, statistic_price_tiktok, faq_hendler, video_review_main, \
    video_review_bilding, video_review_car, video_review_electronics, video_review_food

from db.database_sqlite3 import db_start

logger = logging.getLogger(__name__)


# async def on_startup(_):
#     await db_start()


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

    await set_main_menu(bot)

    # Регистриуем роутеры в диспетчере
    dp.include_router(statistic_price_telegram.router)
    dp.include_router(statistic_price_tiktok.router)
    dp.include_router(faq_hendler.router)
    dp.include_router(employee.router)
    dp.include_router(video_review_main.router)
    dp.include_router(video_review_bilding.router)
    dp.include_router(video_review_electronics.router)
    dp.include_router(video_review_car.router)
    dp.include_router(video_review_food.router)
    dp.include_router(blogers.router)
    dp.include_router(statistic_price_app.router)
    dp.include_router(statistic_price_insta.router)
    dp.include_router(statistic_price_site.router)
    dp.include_router(statistic_price_action.router)
    dp.include_router(fsm_file.router)
    dp.include_router(connection_manager.router)
    dp.include_router(second_level.router)
    dp.include_router(list_links.router)
    dp.include_router(basic.router)


    await bot.send_message(config.tg_bot.id_admin, text="Bun_bot запущен!")
    await bot.delete_webhook(drop_pending_updates=True)
    await db_start()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
