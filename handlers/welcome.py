from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from loader import dp
from utils import sql

# объявление клавиатуры
menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
# создание кнопок
couples = KeyboardButton('🗓 Расписание пар 🗓')
bells = KeyboardButton('⏳ Расписание звонков ⏳')
video = KeyboardButton('📸 ЧЭнК Онлайн 📸')
about = KeyboardButton('✨ О боте ✨')
# добавление кнопок в клавиатуру
menu.add(couples, bells, video, about)


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

    user = [message.from_user.id, message.from_user.username, message.from_user.full_name]
    await sql.sql_add(user)


@dp.message_handler(text='🔙 Назад 🔙')
async def back(message: Message):
    if message.text == '🔙 Назад 🔙':
        await message.answer('Что-то ещё?', reply_markup=menu)
