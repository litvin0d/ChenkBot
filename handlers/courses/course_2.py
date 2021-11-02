from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.exceptions import Throttled

from loader import dp
from utils.screenshot import send_screenshot
from data.links import course_2


@dp.message_handler(text=['2⃣ Второй курс 2⃣'])
async def second_course(message: Message):
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
        back = KeyboardButton('🔙 Назад 🔙')
        groups.add(gr1_20, gr2_20, gr3_20, gr4_20, gr5_20, gr6_20, gr7_20, gr8_20, back)
        await message.answer('В какой ты группе?', reply_markup=groups)


@dp.message_handler(text=['👷‍♂ ТТО 1-20 👷‍♂', '👨‍🔧 ЭССиС 2-20 👨‍🔧',
                          '👨‍🔧 ЭССиС 3-20 👨‍🔧', '👨‍🔧 ЭС 4-20 👨‍🔧',
                          '👨‍🔧 ЭП 5-20 👨‍🔧', '👨‍💼 СА 6-20 👨‍💼',
                          '👨‍💻 ИСП 7-20 👨‍💻', '⭐ ИСП 8-20 ⭐'])
async def second_groups(message: Message):
    # реализация антифлуда в виде блоков try/except/else
    try:
        await dp.throttle(rate=3, key='group')
    except Throttled:
        return
    else:
        user_data = [
            message.from_user.id,
            message.from_user.username,
            message.from_user.full_name
        ]

        if message.text == '👷‍♂ ТТО 1-20 👷‍♂':
            await send_screenshot(user_data, course_2[1])

        if message.text == '👨‍🔧 ЭССиС 2-20 👨‍🔧':
            await send_screenshot(user_data, course_2[2])

        if message.text == '👨‍🔧 ЭССиС 3-20 👨‍🔧':
            await send_screenshot(user_data, course_2[3])

        if message.text == '👨‍🔧 ЭС 4-20 👨‍🔧':
            await send_screenshot(user_data, course_2[4])

        if message.text == '👨‍🔧 ЭП 5-20 👨‍🔧':
            await send_screenshot(user_data, course_2[5])

        if message.text == '👨‍💼 СА 6-20 👨‍💼':
            await send_screenshot(user_data, course_2[6])

        if message.text == '👨‍💻 ИСП 7-20 👨‍💻':
            await send_screenshot(user_data, course_2[7])

        if message.text == '⭐ ИСП 8-20 ⭐':
            await send_screenshot(user_data, course_2[8])
