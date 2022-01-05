from aiogram.types import Message

from loader import dp
from utils import database
from data.config import admins
from keyboards import menu, menu_adm


# функция ответа на команду /start
@dp.message_handler(commands=['start'])
async def welcome(message: Message):
    await message.answer(text=f'👋 <b>Привет, {message.from_user.full_name}!</b> 👋\n'
                              'Этот бот поможет тебе узнать расписание пар на неделю. Просто '
                              'выбери свой курс и группу, бот пришлёт тебе фото '
                              'с расписанием. Так же ты можешь узнать расписание звонков '
                              'и получить ссылку на прямую трансляцию с камеры главного входа '
                              'в ЧЭнК.\n'
                              'Группа ЧЭнКа в ТГ: @chenk_chat', reply_markup=menu)

    if message.from_user.id in admins:
        await message.answer('Вам доступна панель админа!', reply_markup=menu_adm)

    # добавление пользователя в базу данных (если его там не было)
    user_data = [message.from_user.id, message.from_user.username, message.from_user.full_name]
    await database.db_add(user_data)
