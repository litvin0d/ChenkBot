def timetable_link(url):
    from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

    timetable_kb = InlineKeyboardMarkup()
    link_btn = InlineKeyboardButton(text='Открыть в браузере', url=url)
    timetable_kb.add(link_btn)
    return timetable_kb
