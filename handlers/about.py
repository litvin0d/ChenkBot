from aiogram.types import Message

from loader import dp


# about bot message
@dp.message_handler(text='✨ О боте ✨')
async def about(message: Message):
    if message.text == '✨ О боте ✨':
        await message.answer('Бот написан на языке Python. Для работы самого бота '
                             'использована библиотека aiogram, для получения и отправки скриншота '
                             'расписания – библиотека Selenium.\n\n'
                             ''
                             'Создатель: @litvinod\n'
                             'Группа ЧЭнКа в ТГ: @chenk_chat\n\n'
                             ''
                             'Исходный код: https://github.com/litvin0d/ChenkBot')
