from aiogram.types import Message

from loader import dp
from utils.database import db_users_num


@dp.message_handler(text='👥 Количество пользователей 👥')
async def rings_changes(message: Message):
    if message.text == '👥 Количество пользователей 👥':
        await message.answer(f'Количество пользователей: <b>{await db_users_num()}</b>')
