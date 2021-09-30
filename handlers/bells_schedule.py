from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from loader import bot, dp


@dp.message_handler(text=['⏳ Расписание звонков ⏳', '⏳ Понедельник-пятница ⏳', '⏳ Суббота ⏳'])
async def bells_schedule(message: Message):
    if message.text == '⏳ Расписание звонков ⏳':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        monday_friday = KeyboardButton('⏳ Понедельник-пятница ⏳')
        saturday = KeyboardButton('⏳ Суббота ⏳')
        back = KeyboardButton('🔙 Назад 🔙')
        keyboard.add(monday_friday, saturday, back)
        await message.answer('Какой день недели?', reply_markup=keyboard)

    elif message.text == '⏳ Понедельник-пятница ⏳':
        await bot.send_photo(message.chat.id, photo=open('img/monday_friday.jpeg', 'rb'))

    elif message.text == '⏳ Суббота ⏳':
        await bot.send_photo(message.chat.id, photo=open('img/saturday.jpeg', 'rb'))
