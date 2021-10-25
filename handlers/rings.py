from time import sleep
from aiogram.types import Message
from aiogram.utils.exceptions import Throttled

from loader import bot, dp
from utils import sql


@dp.message_handler(text=['⏳ Расписание звонков ⏳'])
async def rings(message: Message):
    # реализация антифлуда в виде блоков try/except/else
    try:
        await dp.throttle(rate=3, key='rings')
    except Throttled:
        return
    else:
        if message.text == '⏳ Расписание звонков ⏳':
            await message.answer('Важно: бот не учитывает изменения в расписании звонков.')
            sleep(0.25)
            await bot.send_photo(message.chat.id, photo=open('img/monday_friday.jpeg', 'rb'))
            sleep(0.25)
            await bot.send_photo(message.chat.id, photo=open('img/saturday.jpeg', 'rb'))

    user = [message.from_user.id, message.from_user.username, message.from_user.full_name]
    await sql.sql_add(user)
