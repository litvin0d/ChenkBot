from aiogram.types import Message
from time import sleep
from loader import bot, dp
from aiogram.utils.exceptions import Throttled


@dp.message_handler(text=['⏳ Расписание звонков ⏳'])
async def rings(message: Message):
    try:
        await dp.throttle(rate=3, key='group')
    except Throttled:
        return
    else:
        if message.text == '⏳ Расписание звонков ⏳':
            await message.answer('Важно: бот не учитывает изменения в расписании звонков.')
            sleep(0.25)
            await bot.send_photo(message.chat.id, photo=open('img/monday_friday.jpeg', 'rb'))
            sleep(0.25)
            await bot.send_photo(message.chat.id, photo=open('img/saturday.jpeg', 'rb'))
