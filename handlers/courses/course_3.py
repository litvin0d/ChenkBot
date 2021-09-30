from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from loader import dp
from utils.screenshot import send_screenshot
from data.links import course_3


@dp.message_handler(text=['3⃣ Третий курс 3⃣', '👷‍♂ ТТО 1-19 👷‍♂',
                          '👨‍🔧 ЭССиС 2-19 👨‍🔧', '👨‍🔧 ЭССиС 3-19 👨‍🔧',
                          '👨‍🔧 ЭС 4-19 👨‍🔧', '👨‍🔧 ЭП 5-19 👨‍🔧',
                          '👨‍💼 СА 6-19 👨‍💼', '👨‍💻 ИСП 7-19 👨‍💻',
                          '👨‍💻 ИСП 8-19 👨‍💻'])
async def second_year(message: Message):
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

    uid = message.from_user.id
    if message.text == '👷‍♂ ТТО 1-19 👷‍♂':
        await send_screenshot(uid, course_3[1_19])

    if message.text == '👨‍🔧 ЭССиС 2-19 👨‍🔧':
        await send_screenshot(uid, course_3[2_19])

    if message.text == '👨‍🔧 ЭССиС 3-19 👨‍🔧':
        await send_screenshot(uid, course_3[3_19])

    if message.text == '👨‍🔧 ЭС 4-19 👨‍🔧':
        await send_screenshot(uid, course_3[4_19])

    if message.text == '👨‍🔧 ЭП 5-19 👨‍🔧':
        await send_screenshot(uid, course_3[5_19])

    if message.text == '👨‍💼 СА 6-19 👨‍💼':
        await send_screenshot(uid, course_3[6_19])

    if message.text == '👨‍💻 ИСП 7-19 👨‍💻':
        await send_screenshot(uid, course_3[7_19])

    if message.text == '👨‍💻 ИСП 8-19 👨‍💻':
        await send_screenshot(uid, course_3[8_19])
