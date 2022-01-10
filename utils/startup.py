import logging
from aiogram import Dispatcher

from data.config import ADMINS
from utils import database


# сообщение админу при запуске бота
async def on_startup(dp: Dispatcher):
    for admin in ADMINS:
        await dp.bot.send_message(admin, 'Bot started! [master]')
    await database.db_start()


async def on_shutdown(dp: Dispatcher):
    logging.warning('Shutting down...')

    for admin in ADMINS:
        await dp.bot.send_message(admin, 'Bot stopped! [master]')
