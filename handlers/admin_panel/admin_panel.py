from aiogram.types import Message

from loader import dp
from keyboards import panel


@dp.message_handler(text='🤖 Панель админа 🤖')
async def admin_panel(message: Message):
    if message.text == '🤖 Панель админа 🤖':
        await message.answer('Выбери действие:', reply_markup=panel)
