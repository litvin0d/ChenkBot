import logging
from aiogram import Dispatcher

from data.config import ADMINS
from utils import database
from loader import bot
from data.config import WEBHOOK_URL


# сообщение админу при запуске бота
async def on_startup(dp: Dispatcher):
    await bot.set_webhook(WEBHOOK_URL)

    for admin in ADMINS:
        await dp.bot.send_message(admin, 'Bot started! [dev]')
    await database.db_start()


async def on_shutdown(dp: Dispatcher):
    logging.warning('Shutting down...')

    for admin in ADMINS:
        await dp.bot.send_message(admin, 'Bot stopped! [dev]')

    await bot.delete_webhook()
