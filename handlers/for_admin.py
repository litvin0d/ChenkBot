from aiogram import Dispatcher

from data.config import admins


# сообщение админу при начале работы бота
async def start_message(dp: Dispatcher):
    for admin in admins:
        await dp.bot.send_message(admin, '[bot_start]')
