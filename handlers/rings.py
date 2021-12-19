from time import sleep
from aiogram.types import Message
from aiogram.utils.exceptions import Throttled

from loader import bot, dp


@dp.message_handler(text=['⏳ Расписание звонков ⏳'])
async def rings(message: Message):
    # реализация антифлуда в виде блоков try/except/else
    try:
        await dp.throttle(rate=3, key='rings')
    except Throttled:
        return
    else:
        if message.text == '⏳ Расписание звонков ⏳':
            # проверка на наличие изменений
            with open('../rings_changes.txt', 'r') as file:
                photo_id = file.read()
                if photo_id == '':
                    await bot.send_photo(message.chat.id, open('img/monday_friday.jpeg', 'rb'), 'Понедельник-пятница.')
                    sleep(.10)
                    await bot.send_photo(message.chat.id, open('img/saturday.jpeg', 'rb'), 'Суббота.')
                else:
                    await bot.send_photo(message.chat.id, photo_id, '<i>Расписание звонков изменено.</i>')
