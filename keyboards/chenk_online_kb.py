from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

link_kb = InlineKeyboardMarkup(row_width=1)
link_btn = InlineKeyboardButton(text='ЧЭнК Онлайн', url='https://chenk.ru/ru/life/chenk-onlayn.php')
link_kb.add(link_btn)
