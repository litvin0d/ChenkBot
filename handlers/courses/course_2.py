import json
from aiogram.types import Message
from aiogram.utils.exceptions import Throttled

from loader import dp
from utils.send_screen import send_screen
from keyboards import groups2, contents2
from data.config import LINKS_PATH

# parsing json file with links
with open(LINKS_PATH, 'r') as f:
    links = json.load(f)
    f.close()


@dp.message_handler(text=['2⃣ Второй курс 2⃣'])
async def course_2(message: Message):
    if message.text == '2⃣ Второй курс 2⃣':
        await message.answer('В какой ты группе?', reply_markup=groups2)


@dp.message_handler(text=contents2)
async def groups_2(message: Message):
    # anti-flood implementation in form of try/except/else
    try:
        await dp.throttle(rate=3, key='group')
    except Throttled:
        return
    else:
        if message.text == '👷‍♂ ТТО 1-20 👷‍♂':
            await send_screen(message.from_user.id, links['course_2'][0])

        if message.text == '👨‍🔧 ЭССиС 2-20 👨‍🔧':
            await send_screen(message.from_user.id, links['course_2'][1])

        if message.text == '👨‍🔧 ЭССиС 3-20 👨‍🔧':
            await send_screen(message.from_user.id, links['course_2'][2])

        if message.text == '👨‍🔧 ЭС 4-20 👨‍🔧':
            await send_screen(message.from_user.id, links['course_2'][3])

        if message.text == '👨‍🔧 ЭП 5-20 👨‍🔧':
            await send_screen(message.from_user.id, links['course_2'][4])

        if message.text == '👨‍💼 СА 6-20 👨‍💼':
            await send_screen(message.from_user.id, links['course_2'][5])

        if message.text == '👨‍💻 ИСП 7-20 👨‍💻':
            await send_screen(message.from_user.id, links['course_2'][6])

        if message.text == '⭐ ИСП 8-20 ⭐':
            await send_screen(message.from_user.id, links['course_2'][7])
