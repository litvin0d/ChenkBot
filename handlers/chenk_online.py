from aiogram.types import Message

from loader import dp


@dp.message_handler(text='📸 ЧЭнК Онлайн 📸')
async def chenk_online(message: Message):
    if message.text == '📸 ЧЭнК Онлайн 📸':
        await message.answer('Прямая трансляция с камеры главного входа в ЧЭнК:\n'
                             'https://chenk.ru/ru/life/chenk-onlayn.php')
