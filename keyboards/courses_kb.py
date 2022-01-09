from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# course selection keyboard
courses = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
first_grade = KeyboardButton('1⃣ Первый курс 1⃣')
second_grade = KeyboardButton('2⃣ Второй курс 2⃣')
third_grade = KeyboardButton('3⃣ Третий курс 3⃣')
fourth_grade = KeyboardButton('4⃣ Четвёртый курс 4⃣')
back = KeyboardButton('🔙 Назад 🔙')
courses.add(first_grade, second_grade, third_grade, fourth_grade, back)
