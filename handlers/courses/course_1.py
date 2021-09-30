from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from loader import dp
from utils.screenshot import send_screenshot
from data.links import course_1


@dp.message_handler(text=['1⃣ Первый курс 1⃣', '👷‍♂ ТТО 1-21 👷‍♂',
                          '👨‍🔧 ЭССиС 2-21 👨‍🔧', '👨‍🔧 ЭССиС 3-21 👨‍🔧',
                          '👨‍🔧 ЭС 4-21 👨‍🔧', '👨‍🔧 ЭП 5-21 👨‍🔧',
                          '👨‍💼 СА 6-21 👨‍💼', '👨‍💻 ИСП 7-21 👨‍💻',
                          '👨‍💻 ИСП 8-21 👨‍💻', '👨‍💻 ИСП 9-21 👨‍💻'])
async def second_year(message: Message):
    if message.text == '1⃣ Первый курс 1⃣':
        groups = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        gr1_21 = KeyboardButton('👷‍♂ ТТО 1-21 👷‍♂')
        gr2_21 = KeyboardButton('👨‍🔧 ЭССиС 2-21 👨‍🔧')
        gr3_21 = KeyboardButton('👨‍🔧 ЭССиС 3-21 👨‍🔧')
        gr4_21 = KeyboardButton('👨‍🔧 ЭС 4-21 👨‍🔧')
        gr5_21 = KeyboardButton('👨‍🔧 ЭП 5-21 👨‍🔧')
        gr6_21 = KeyboardButton('👨‍💼 СА 6-21 👨‍💼')
        gr7_21 = KeyboardButton('👨‍💻 ИСП 7-21 👨‍💻')
        gr8_21 = KeyboardButton('👨‍💻 ИСП 8-21 👨‍💻')
        gr9_21 = KeyboardButton('👨‍💻 ИСП 9-21 👨‍💻')
        back_to_courses = KeyboardButton('🔙 Выбрать курс 🔙')
        groups.add(gr1_21, gr2_21, gr3_21, gr4_21, gr5_21, gr6_21, gr7_21, gr8_21, gr9_21, back_to_courses)
        await message.answer('В какой ты группе?', reply_markup=groups)

    uid = message.from_user.id
    if message.text == '👷‍♂ ТТО 1-21 👷‍♂':
        await send_screenshot(uid, course_1[1_21])

    if message.text == '👨‍🔧 ЭССиС 2-21 👨‍🔧':
        await send_screenshot(uid, course_1[2_21])

    if message.text == '👨‍🔧 ЭССиС 3-21 👨‍🔧':
        await send_screenshot(uid, course_1[3_21])

    if message.text == '👨‍🔧 ЭС 4-21 👨‍🔧':
        await send_screenshot(uid, course_1[4_21])

    if message.text == '👨‍🔧 ЭП 5-21 👨‍🔧':
        await send_screenshot(uid, course_1[5_21])

    if message.text == '👨‍💼 СА 6-21 👨‍💼':
        await send_screenshot(uid, course_1[6_21])

    if message.text == '👨‍💻 ИСП 7-21 👨‍💻':
        await send_screenshot(uid, course_1[7_21])

    if message.text == '👨‍💻 ИСП 8-21 👨‍💻':
        await send_screenshot(uid, course_1[8_21])

    if message.text == '👨‍💻 ИСП 9-21 👨‍💻':
        await send_screenshot(uid, course_1[9_21])
