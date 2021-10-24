from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from loader import dp

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
    text = '👋 <b>Привет!</b> 👋\n' \
           'ChenkBot поможет тебе быстро узнать актуальное ' \
           'расписание пар и звонков. Больше не нужно тратить время и заходить на ' \
           'сайт ЧЭнКа или смотреть расписание на стэнде.\n' \
           'Группа в ТГ: @chenk_chat'
    await message.answer(text=text, reply_markup=menu)


@dp.message_handler(text='🔙 Назад 🔙')
async def back(message: Message):
    if message.text == '🔙 Назад 🔙':
        await message.answer('Что-то ещё?', reply_markup=menu)
