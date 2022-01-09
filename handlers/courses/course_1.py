import json
from aiogram.types import Message
from aiogram.utils.exceptions import Throttled

from loader import dp
from utils.send_screen import send_screen
from keyboards import groups1, contents1

# parsing json file with links
with open('data/links.json', 'r') as f:
    links = json.load(f)


@dp.message_handler(text=['1⃣ Первый курс 1⃣'])
async def course_1(message: Message):
    if message.text == '1⃣ Первый курс 1⃣':
        await message.answer('В какой ты группе?', reply_markup=groups1)


@dp.message_handler(text=contents1)
async def groups_1(message: Message):
    # anti-flood implementation in form of try/except/else
    try:
        await dp.throttle(rate=3, key='group')
    except Throttled:
        return
    else:
        if message.text == '👷‍♂ ТТО 1-21 👷‍♂':
            await send_screen(message.from_user.id, links['course_1'][0])

        if message.text == '👨‍🔧 ЭССиС 2-21 👨‍🔧':
            await send_screen(message.from_user.id, links['course_1'][1])

        if message.text == '👨‍🔧 ЭССиС 3-21 👨‍🔧':
            await send_screen(message.from_user.id, links['course_1'][2])

        if message.text == '👨‍🔧 ЭС 4-21 👨‍🔧':
            await send_screen(message.from_user.id, links['course_1'][3])

        if message.text == '👨‍🔧 ЭП 5-21 👨‍🔧':
            await send_screen(message.from_user.id, links['course_1'][4])

        if message.text == '👨‍💼 СА 6-21 👨‍💼':
            await send_screen(message.from_user.id, links['course_1'][5])

        if message.text == '👨‍💻 ИСП 7-21 👨‍💻':
            await send_screen(message.from_user.id, links['course_1'][6])

        if message.text == '👨‍💻 ИСП 8-21 👨‍💻':
            await send_screen(message.from_user.id, links['course_1'][7])

        if message.text == '👨‍💻 ИСП 9-21 👨‍💻':
            await send_screen(message.from_user.id, links['course_1'][8])
