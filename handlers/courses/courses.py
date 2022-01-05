from aiogram.types import Message

from loader import dp
from keyboards import courses


@dp.message_handler(text=['🗓 Расписание пар 🗓', '🔙 Выбрать курс 🔙'])
async def list_of_courses(message: Message):
    if message.text == '🗓 Расписание пар 🗓':
        await message.answer('На каком ты курсе?', reply_markup=courses)
