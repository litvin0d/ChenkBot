from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# главная клавиатура
menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
couples = KeyboardButton('🗓 Расписание пар 🗓')
bells = KeyboardButton('⏳ Расписание звонков ⏳')
video = KeyboardButton('📸 ЧЭнК Онлайн 📸')
about = KeyboardButton('✨ О боте ✨')
menu.add(couples, bells, video, about)

# версия админа
menu_adm = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
admin_panel = KeyboardButton('🤖 Панель админа 🤖')
menu_adm.add(couples, bells, admin_panel, video, about)
