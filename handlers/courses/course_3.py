from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.exceptions import Throttled

from loader import dp
from utils import sql
from utils.screenshot import send_screenshot
from data.links import course_3


@dp.message_handler(text=['3⃣ Третий курс 3⃣'])
async def third_course(message: Message):
    if message.text == '3⃣ Третий курс 3⃣':
        groups = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        gr1_19 = KeyboardButton('👷‍♂ ТТО 1-19 👷‍♂')
        gr2_19 = KeyboardButton('👨‍🔧 ЭССиС 2-19 👨‍🔧')
        gr3_19 = KeyboardButton('👨‍🔧 ЭССиС 3-19 👨‍🔧')
        gr4_19 = KeyboardButton('👨‍🔧 ЭС 4-19 👨‍🔧')
        gr5_19 = KeyboardButton('👨‍🔧 ЭП 5-19 👨‍🔧')
        gr6_19 = KeyboardButton('👨‍💼 СА 6-19 👨‍💼')
        gr7_19 = KeyboardButton('👨‍💻 ИСП 7-19 👨‍💻')
        gr8_19 = KeyboardButton('👨‍💻 ИСП 8-19 👨‍💻')
        back_to_courses = KeyboardButton('🔙 Выбрать курс 🔙')
        groups.add(gr1_19, gr2_19, gr3_19, gr4_19, gr5_19, gr6_19, gr7_19, gr8_19, back_to_courses)
        await message.answer('В какой ты группе?', reply_markup=groups)


@dp.message_handler(text=['👷‍♂ ТТО 1-19 👷‍♂', '👨‍🔧 ЭССиС 2-19 👨‍🔧',
                          '👨‍🔧 ЭССиС 3-19 👨‍🔧', '👨‍🔧 ЭС 4-19 👨‍🔧',
                          '👨‍🔧 ЭП 5-19 👨‍🔧', '👨‍💼 СА 6-19 👨‍💼',
                          '👨‍💻 ИСП 7-19 👨‍💻', '👨‍💻 ИСП 8-19 👨‍💻'])
async def third_groups(message: Message):
    # реализация антифлуда в виде блоков try/except/else
    try:
        await dp.throttle(rate=3, key='group')
    except Throttled:
        return
    else:
        uid = message.from_user.id
        if message.text == '👷‍♂ ТТО 1-19 👷‍♂':
            await send_screenshot(uid, course_3[1])
            user = [message.from_user.id, message.from_user.username, message.from_user.full_name]
            await sql.sql_add(user)

        if message.text == '👨‍🔧 ЭССиС 2-19 👨‍🔧':
            await send_screenshot(uid, course_3[2])
            user = [message.from_user.id, message.from_user.username, message.from_user.full_name]
            await sql.sql_add(user)

        if message.text == '👨‍🔧 ЭССиС 3-19 👨‍🔧':
            await send_screenshot(uid, course_3[3])
            user = [message.from_user.id, message.from_user.username, message.from_user.full_name]
            await sql.sql_add(user)

        if message.text == '👨‍🔧 ЭС 4-19 👨‍🔧':
            await send_screenshot(uid, course_3[4])
            user = [message.from_user.id, message.from_user.username, message.from_user.full_name]
            await sql.sql_add(user)

        if message.text == '👨‍🔧 ЭП 5-19 👨‍🔧':
            await send_screenshot(uid, course_3[5])
            user = [message.from_user.id, message.from_user.username, message.from_user.full_name]
            await sql.sql_add(user)

        if message.text == '👨‍💼 СА 6-19 👨‍💼':
            await send_screenshot(uid, course_3[6])
            user = [message.from_user.id, message.from_user.username, message.from_user.full_name]
            await sql.sql_add(user)

        if message.text == '👨‍💻 ИСП 7-19 👨‍💻':
            await send_screenshot(uid, course_3[7])
            user = [message.from_user.id, message.from_user.username, message.from_user.full_name]
            await sql.sql_add(user)

        if message.text == '👨‍💻 ИСП 8-19 👨‍💻':
            await send_screenshot(uid, course_3[8])
            user = [message.from_user.id, message.from_user.username, message.from_user.full_name]
            await sql.sql_add(user)
