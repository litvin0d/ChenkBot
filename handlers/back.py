from aiogram.types import Message

from loader import dp
from data.config import admins
from keyboards import menu, menu_adm


# хэндлер кнопки назад, возвращающий главную клавиатуру
@dp.message_handler(text='🔙 Назад 🔙')
async def back(message: Message):
    if message.text == '🔙 Назад 🔙':
        if message.from_user.id not in admins:
            await message.answer('Что-то ещё?', reply_markup=menu)
        else:
            await message.answer('Что-то ещё?', reply_markup=menu_adm)
