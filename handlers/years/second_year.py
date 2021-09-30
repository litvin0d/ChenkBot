from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from loader import dp
from utils.screenshot import get_screenshot


@dp.message_handler(text=['2⃣ Второй курс 2⃣', '👷‍♂ ТТО 1-20 👷‍♂',
                          '👨‍🔧 ЭССиС 2-20 👨‍🔧', '👨‍🔧 ЭССиС 3-20 👨‍🔧',
                          '👨‍🔧 ЭС 4-20 👨‍🔧', '👨‍🔧 ЭП 5-20 👨‍🔧',
                          '👨‍💼 СА 6-20 👨‍💼', '👨‍💻 ИСП 7-20 👨‍💻',
                          '👨‍💻 ИСП 8-20 👨‍💻'])
async def second_year(message: Message):
    if message.text == '2⃣ Второй курс 2⃣':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        gr1_20 = KeyboardButton('👷‍♂ ТТО 1-20 👷‍♂')
        gr2_20 = KeyboardButton('👨‍🔧 ЭССиС 2-20 👨‍🔧')
        gr3_20 = KeyboardButton('👨‍🔧 ЭССиС 3-20 👨‍🔧')
        gr4_20 = KeyboardButton('👨‍🔧 ЭС 4-20 👨‍🔧')
        gr5_20 = KeyboardButton('👨‍🔧 ЭП 5-20 👨‍🔧')
        gr6_20 = KeyboardButton('👨‍💼 СА 6-20 👨‍💼')
        gr7_20 = KeyboardButton('👨‍💻 ИСП 7-20 👨‍💻')
        gr8_20 = KeyboardButton('👨‍💻 ИСП 8-20 👨‍💻')
        back_to_grades = KeyboardButton('🔙 Выбрать курс 🔙')
        keyboard.add(gr1_20, gr2_20, gr3_20, gr4_20, gr5_20, gr6_20, gr7_20, gr8_20, back_to_grades)
        await message.answer('В какой ты группе?', reply_markup=keyboard)

    if message.text == '👷‍♂ ТТО 1-20 👷‍♂':
        uid = message.from_user.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=246&dep=3'
        await get_screenshot(uid, url)

    if message.text == '👨‍🔧 ЭССиС 2-20 👨‍🔧':
        uid = message.from_user.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=247&dep=3'
        await get_screenshot(uid, url)

    if message.text == '👨‍🔧 ЭССиС 3-20 👨‍🔧':
        uid = message.from_user.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=248&dep=3'
        await get_screenshot(uid, url)

    if message.text == '👨‍🔧 ЭС 4-20 👨‍🔧':
        uid = message.from_user.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=249&dep=3'
        await get_screenshot(uid, url)

    if message.text == '👨‍🔧 ЭП 5-20 👨‍🔧':
        uid = message.from_user.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=250&dep=3'
        await get_screenshot(uid, url)

    if message.text == '👨‍💼 СА 6-20 👨‍💼':
        uid = message.from_user.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=251&dep=3'
        await get_screenshot(uid, url)

    if message.text == '👨‍💻 ИСП 7-20 👨‍💻':
        uid = message.from_user.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=252&dep=3'
        await get_screenshot(uid, url)

    if message.text == '👨‍💻 ИСП 8-20 👨‍💻':
        uid = message.from_user.id
        url = "https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=253&dep=3"
        await get_screenshot(uid, url)
