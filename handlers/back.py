from aiogram.types import Message

from loader import dp
from data.config import ADMINS
from keyboards import menu, menu_adm


# 'back' button handler, returning the main keyboard
@dp.message_handler(text='🔙 Назад 🔙')
async def back(message: Message):
    if message.text == '🔙 Назад 🔙':
        if message.from_user.id in ADMINS:
            await message.answer('Что-то ещё?', reply_markup=menu)
            await message.answer('Что-то ещё?', reply_markup=menu_adm)
        else:
            await message.answer('Что-то ещё?', reply_markup=menu)
