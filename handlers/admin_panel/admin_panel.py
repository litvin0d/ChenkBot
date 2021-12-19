from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from loader import dp

panel = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
rings_changes = KeyboardButton('📝 Изменения в расп. звонков 📝')
users_num = KeyboardButton('👥 Количество пользователей 👥')
back = KeyboardButton('🔙 Назад 🔙')
panel.add(rings_changes, users_num, back)


@dp.message_handler(text='🤖 Панель админа 🤖')
async def admin_panel(message: Message):
    if message.text == '🤖 Панель админа 🤖':
        await message.answer('Выбери действие:', reply_markup=panel)
