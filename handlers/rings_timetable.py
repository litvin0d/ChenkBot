import os
from aiogram.types import Message
from aiogram.utils.exceptions import Throttled

from loader import bot, dp
from data.config import RINGS_PATH, RINGS_CHANGES_PATH


@dp.message_handler(text=['⏳ Расписание звонков ⏳'])
async def rings_timetable(message: Message):
    # anti-flood implementation in form of try/except/else
    try:
        await dp.throttle(rate=3, key='rings')
    except Throttled:
        return
    else:
        if message.text == '⏳ Расписание звонков ⏳':
            # checking for rings_changes.txt file
            if not os.path.isfile(RINGS_CHANGES_PATH):
                open(RINGS_CHANGES_PATH, 'w').close()

            # checking for changes
            with open(RINGS_CHANGES_PATH, 'r') as file:
                photo_id = file.read()
                if photo_id == '':
                    msg = await bot.send_photo(message.chat.id, open(RINGS_PATH, 'rb'), 'Крутилин лох.')
                    await msg.edit_caption('')
                else:
                    await bot.send_photo(message.chat.id, photo_id, '<i>Расписание звонков изменено.</i>')
