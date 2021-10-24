from aiogram import Dispatcher

from data.config import admins


# сообщение админу при запуске бота
async def for_admin(dp: Dispatcher):
    for admin in admins:
        await dp.bot.send_message(admin, '[bot_start]')
