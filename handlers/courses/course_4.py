from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.exceptions import Throttled

from loader import dp
from utils import sql
from utils.screenshot import send_screenshot
from data.links import course_4


@dp.message_handler(text=['4⃣ Четвёртый курс 4⃣'])
async def fourth_year(message: Message):
    if message.text == '4⃣ Четвёртый курс 4⃣':
        groups = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        gr1_18 = KeyboardButton('👷‍♂ ТТО 1-18 👷‍♂')
        gr2_18 = KeyboardButton('👨‍🔧 ЭССиС 2-18 👨‍🔧')
        gr3_18 = KeyboardButton('👨‍🔧 ЭП 3-18 👨‍🔧')
        gr4_18 = KeyboardButton('👨‍🔧 ЭС 4-18 👨‍🔧')
        gr5_18 = KeyboardButton('👨‍🔧 ЭП 5-18 👨‍🔧')
        gr6_18 = KeyboardButton('👨‍💼 СА 6-18 👨‍💼')
        gr7_18 = KeyboardButton('👨‍💻 ИСП 7-18 👨‍💻')
        gr8_18 = KeyboardButton('👨‍💻 ИСП 8-18 👨‍💻')
        back_to_courses = KeyboardButton('🔙 Выбрать курс 🔙')
        groups.add(gr1_18, gr2_18, gr3_18, gr4_18, gr5_18, gr6_18, gr7_18, gr8_18, back_to_courses)
        await message.answer('В какой ты группе?', reply_markup=groups)


@dp.message_handler(text=['👷‍♂ ТТО 1-18 👷‍♂', '👨‍🔧 ЭССиС 2-18 👨‍🔧',
                          '👨‍🔧 ЭП 3-18 👨‍🔧', '👨‍🔧 ЭС 4-18 👨‍🔧',
                          '👨‍🔧 ЭП 5-18 👨‍🔧', '👨‍💼 СА 6-18 👨‍💼',
                          '👨‍💻 ИСП 7-18 👨‍💻', '👨‍💻 ИСП 8-18 👨‍💻'])
async def fourth_year(message: Message):
    # реализация антифлуда в виде блоков try/except/else
    try:
        await dp.throttle(rate=3, key='group')
    except Throttled:
        return
    else:
        uid = message.from_user.id
        if message.text == '👷‍♂ ТТО 1-18 👷‍♂':
            await send_screenshot(uid, course_4[1])
            user = [message.from_user.id, message.from_user.username, message.from_user.full_name]
            await sql.sql_add(user)

        if message.text == '👨‍🔧 ЭССиС 2-18 👨‍🔧':
            await send_screenshot(uid, course_4[2])
            user = [message.from_user.id, message.from_user.username, message.from_user.full_name]
            await sql.sql_add(user)

        if message.text == '👨‍🔧 ЭП 3-18 👨‍🔧':
            await send_screenshot(uid, course_4[3])
            user = [message.from_user.id, message.from_user.username, message.from_user.full_name]
            await sql.sql_add(user)

        if message.text == '👨‍🔧 ЭС 4-18 👨‍🔧':
            await send_screenshot(uid, course_4[4])
            user = [message.from_user.id, message.from_user.username, message.from_user.full_name]
            await sql.sql_add(user)

        if message.text == '👨‍🔧 ЭП 5-18 👨‍🔧':
            await send_screenshot(uid, course_4[5])
            user = [message.from_user.id, message.from_user.username, message.from_user.full_name]
            await sql.sql_add(user)

        if message.text == '👨‍💼 СА 6-18 👨‍💼':
            await send_screenshot(uid, course_4[6])
            user = [message.from_user.id, message.from_user.username, message.from_user.full_name]
            await sql.sql_add(user)

        if message.text == '👨‍💻 ИСП 7-18 👨‍💻':
            await send_screenshot(uid, course_4[7])
            user = [message.from_user.id, message.from_user.username, message.from_user.full_name]
            await sql.sql_add(user)

        if message.text == '👨‍💻 ИСП 8-18 👨‍💻':
            await send_screenshot(uid, course_4[8])
            user = [message.from_user.id, message.from_user.username, message.from_user.full_name]
            await sql.sql_add(user)
