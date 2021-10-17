from aiogram.types import Message

from loader import bot, dp


@dp.message_handler(text=['⏳ Расписание звонков ⏳'])
async def bells_schedule(message: Message):
    if message.text == '⏳ Расписание звонков ⏳':
        await bot.send_photo(message.chat.id, photo=open('img/monday_friday.jpeg', 'rb'))
        await bot.send_photo(message.chat.id, photo=open('img/saturday.jpeg', 'rb'))
