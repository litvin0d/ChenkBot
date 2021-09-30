from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from loader import dp


@dp.message_handler(text=['🗓 Расписание пар 🗓', '🔙 Выбрать курс 🔙'])
async def list_of_years(message: Message):
    if message.text == '🗓 Расписание пар 🗓':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        first_grade = KeyboardButton('1⃣ Первый курс 1⃣')
        second_grade = KeyboardButton('2⃣ Второй курс 2⃣')
        third_grade = KeyboardButton('3⃣ Третий курс 3⃣')
        fourth_grade = KeyboardButton('4⃣ Четвёртый курс 4⃣')
        back = KeyboardButton('🔙 Назад 🔙')
        keyboard.add(first_grade, second_grade, third_grade, fourth_grade, back)
        await message.answer('На каком ты курсе?', reply_markup=keyboard)

    elif message.text == '🔙 Выбрать курс 🔙':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        first_grade = KeyboardButton('1⃣ Первый курс 1⃣')
        second_grade = KeyboardButton('2⃣ Второй курс 2⃣ ')
        third_grade = KeyboardButton('3⃣ Третий курс 3⃣')
        fourth_grade = KeyboardButton('4⃣ Четвёртый курс 4⃣')
        back = KeyboardButton('🔙 Назад 🔙')
        keyboard.add(first_grade, second_grade, third_grade, fourth_grade, back)
        await message.answer('На каком ты курсе?', reply_markup=keyboard)
