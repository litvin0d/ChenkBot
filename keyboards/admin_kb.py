from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# клавиатура панели админа
panel = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
rings_changes = KeyboardButton('📝 Изменения в расп. звонков 📝')
users_num = KeyboardButton('👥 Количество пользователей 👥')
back = KeyboardButton('🔙 Назад 🔙')
panel.add(rings_changes, users_num, back)
