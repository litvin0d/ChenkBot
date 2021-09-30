from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from loader import dp
from utils.screenshot import send_screenshot
from data.links import course_2


@dp.message_handler(text=['2⃣ Второй курс 2⃣', '👷‍♂ ТТО 1-20 👷‍♂',
                          '👨‍🔧 ЭССиС 2-20 👨‍🔧', '👨‍🔧 ЭССиС 3-20 👨‍🔧',
                          '👨‍🔧 ЭС 4-20 👨‍🔧', '👨‍🔧 ЭП 5-20 👨‍🔧',
                          '👨‍💼 СА 6-20 👨‍💼', '👨‍💻 ИСП 7-20 👨‍💻',
                          '⭐ ИСП 8-20 ⭐'])
async def second_year(message: Message):
    if message.text == '2⃣ Второй курс 2⃣':
        groups = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        gr1_20 = KeyboardButton('👷‍♂ ТТО 1-20 👷‍♂')
        gr2_20 = KeyboardButton('👨‍🔧 ЭССиС 2-20 👨‍🔧')
        gr3_20 = KeyboardButton('👨‍🔧 ЭССиС 3-20 👨‍🔧')
        gr4_20 = KeyboardButton('👨‍🔧 ЭС 4-20 👨‍🔧')
        gr5_20 = KeyboardButton('👨‍🔧 ЭП 5-20 👨‍🔧')
        gr6_20 = KeyboardButton('👨‍💼 СА 6-20 👨‍💼')
        gr7_20 = KeyboardButton('👨‍💻 ИСП 7-20 👨‍💻')
        gr8_20 = KeyboardButton('⭐ ИСП 8-20 ⭐')
        back_to_courses = KeyboardButton('🔙 Выбрать курс 🔙')
        groups.add(gr1_20, gr2_20, gr3_20, gr4_20, gr5_20, gr6_20, gr7_20, gr8_20, back_to_courses)
        await message.answer('В какой ты группе?', reply_markup=groups)

    uid = message.from_user.id
    if message.text == '👷‍♂ ТТО 1-20 👷‍♂':
        await send_screenshot(uid, course_2[1_20])

    if message.text == '👨‍🔧 ЭССиС 2-20 👨‍🔧':
        await send_screenshot(uid, course_2[2_20])

    if message.text == '👨‍🔧 ЭССиС 3-20 👨‍🔧':
        await send_screenshot(uid, course_2[3_20])

    if message.text == '👨‍🔧 ЭС 4-20 👨‍🔧':
        await send_screenshot(uid, course_2[4_20])

    if message.text == '👨‍🔧 ЭП 5-20 👨‍🔧':
        await send_screenshot(uid, course_2[5_20])

    if message.text == '👨‍💼 СА 6-20 👨‍💼':
        await send_screenshot(uid, course_2[6_20])

    if message.text == '👨‍💻 ИСП 7-20 👨‍💻':
        await send_screenshot(uid, course_2[7_20])

    if message.text == '⭐ ИСП 8-20 ⭐':
        await send_screenshot(uid, course_2[8_20])
