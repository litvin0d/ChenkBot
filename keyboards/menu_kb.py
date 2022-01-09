from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# main keyboard
menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
couples = KeyboardButton('🗓 Расписание пар 🗓')
bells = KeyboardButton('⏳ Расписание звонков ⏳')
video = KeyboardButton('📸 ЧЭнК Онлайн 📸')
about = KeyboardButton('✨ О боте ✨')
menu.add(couples, bells, video, about)

# admin version of main keyboard
menu_adm = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
admin_panel = KeyboardButton('🤖 Панель админа 🤖')
menu_adm.add(couples, bells, admin_panel, video, about)
