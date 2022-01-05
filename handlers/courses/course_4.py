import json
from aiogram.types import Message
from aiogram.utils.exceptions import Throttled

from loader import dp
from utils.send_screen import send_screen
from keyboards import groups4, contents4

# парсинг json файла со ссылками
with open('data/links.json', 'r') as f:
    links = json.load(f)


@dp.message_handler(text=['4⃣ Четвёртый курс 4⃣'])
async def course_4(message: Message):
    if message.text == '4⃣ Четвёртый курс 4⃣':
        await message.answer('В какой ты группе?', reply_markup=groups4)


@dp.message_handler(text=contents4)
async def groups_4(message: Message):
    # реализация антифлуда в виде блоков try/except/else
    try:
        await dp.throttle(rate=3, key='group')
    except Throttled:
        return
    else:
        if message.text == '👷‍♂ ТТО 1-18 👷‍♂':
            await send_screen(message.from_user.id, links['course_4'][0])

        if message.text == '👨‍🔧 ЭССиС 2-18 👨‍🔧':
            await send_screen(message.from_user.id, links['course_4'][1])

        if message.text == '👨‍🔧 ЭП 3-18 👨‍🔧':
            await send_screen(message.from_user.id, links['course_4'][2])

        if message.text == '👨‍🔧 ЭС 4-18 👨‍🔧':
            await send_screen(message.from_user.id, links['course_4'][3])

        if message.text == '👨‍🔧 ЭП 5-18 👨‍🔧':
            await send_screen(message.from_user.id, links['course_4'][4])

        if message.text == '👨‍💼 СА 6-18 👨‍💼':
            await send_screen(message.from_user.id, links['course_4'][5])

        if message.text == '👨‍💻 ИСП 7-18 👨‍💻':
            await send_screen(message.from_user.id, links['course_4'][6])

        if message.text == '👨‍💻 ИСП 8-18 👨‍💻':
            await send_screen(message.from_user.id, links['course_4'][7])
