import os
from aiogram.types import Message
from aiogram.utils.exceptions import Throttled

from loader import bot, dp


@dp.message_handler(text=['⏳ Расписание звонков ⏳'])
async def rings_schedule(message: Message):
    # anti-flood implementation in form of try/except/else
    try:
        await dp.throttle(rate=3, key='rings')
    except Throttled:
        return
    else:
        if message.text == '⏳ Расписание звонков ⏳':
            # checking for rings_changes.txt file
            if not os.path.isfile('data/rings_changes.txt'):
                open('data/rings_changes.txt', 'w').close()

            # checking for changes
            with open('data/rings_changes.txt', 'r') as file:
                photo_id = file.read()
                if photo_id == '':
                    await bot.send_photo(message.chat.id, open('img/monday_friday.jpeg', 'rb'), 'Понедельник-пятница.')
                    await bot.send_photo(message.chat.id, open('img/saturday.jpeg', 'rb'), 'Суббота.')
                else:
                    await bot.send_photo(message.chat.id, photo_id, '<i>Расписание звонков изменено.</i>')
