from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from loader import dp


@dp.message_handler(text=['🔙 Назад 🔙'])
async def back(message: Message):
    if message.text == '🔙 Назад 🔙':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        couples = KeyboardButton('🗓 Расписание пар 🗓')
        bells = KeyboardButton('⏳ Расписание звонков ⏳')
        videcam = KeyboardButton('📸 ЧЭнК Онлайн 📸')
        support = KeyboardButton('✨ Поддержка ✨')
        keyboard.add(couples, bells, videcam, support)
        await message.answer('Что-то ещё?', reply_markup=keyboard)
