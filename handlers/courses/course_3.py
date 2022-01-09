import json
from aiogram.types import Message
from aiogram.utils.exceptions import Throttled

from loader import dp
from utils.send_screen import send_screen
from keyboards import groups3, contents3

# parsing json file with links
with open('data/links.json', 'r') as f:
    links = json.load(f)


@dp.message_handler(text=['3⃣ Третий курс 3⃣'])
async def course_3(message: Message):
    if message.text == '3⃣ Третий курс 3⃣':
        await message.answer('В какой ты группе?', reply_markup=groups3)


@dp.message_handler(text=contents3)
async def groups_3(message: Message):
    # anti-flood implementation in form of try/except/else
    try:
        await dp.throttle(rate=3, key='group')
    except Throttled:
        return
    else:
        if message.text == '👷‍♂ ТТО 1-19 👷‍♂':
            await send_screen(message.from_user.id, links['course_3'][0])

        if message.text == '👨‍🔧 ЭССиС 2-19 👨‍🔧':
            await send_screen(message.from_user.id, links['course_3'][1])

        if message.text == '👨‍🔧 ЭССиС 3-19 👨‍🔧':
            await send_screen(message.from_user.id, links['course_3'][2])

        if message.text == '👨‍🔧 ЭС 4-19 👨‍🔧':
            await send_screen(message.from_user.id, links['course_3'][3])

        if message.text == '👨‍🔧 ЭП 5-19 👨‍🔧':
            await send_screen(message.from_user.id, links['course_3'][4])

        if message.text == '👨‍💼 СА 6-19 👨‍💼':
            await send_screen(message.from_user.id, links['course_3'][5])

        if message.text == '👨‍💻 ИСП 7-19 👨‍💻':
            await send_screen(message.from_user.id, links['course_3'][6])

        if message.text == '👨‍💻 ИСП 8-19 👨‍💻':
            await send_screen(message.from_user.id, links['course_3'][7])
