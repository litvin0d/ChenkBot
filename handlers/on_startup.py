from aiogram import Dispatcher

from data.config import admins
from utils import database


# сообщение админу при запуске бота
async def on_startup(dp: Dispatcher):
    for admin in admins:
        await dp.bot.send_message(admin, '[bot_start]')
    await database.db_start()
