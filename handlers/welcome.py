# импорты из библиотек
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

# локальные импорты
from loader import dp


# функция ответа на команду /start
@dp.message_handler(commands=['start'])
async def welcome(message: Message):
    # объявление клавиатуры
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    # создание кнопок
    couples = KeyboardButton('🗓 Расписание пар 🗓')
    bells = KeyboardButton('⏳ Расписание звонков ⏳')
    videcam = KeyboardButton('📸 ЧЭнК Онлайн 📸')
    support = KeyboardButton('✨ Поддержка ✨')
    # добавление кнопок в клавиатуру
    keyboard.add(couples, bells, videcam, support)

    # приветствнное сообщение и добавление клавиатуры
    text = '👋 Привет! 👋\n' \
           'ChenkBot поможет тебе быстро узнаить актуальное' \
           ' расписание пар и звонков.'
    await message.answer(text=text, reply_markup=keyboard)
