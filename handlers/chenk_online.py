from aiogram.types import Message

from loader import dp
from keyboards import link_kb


@dp.message_handler(text='📸 ЧЭнК Онлайн 📸')
async def chenk_online(message: Message):
    if message.text == '📸 ЧЭнК Онлайн 📸':
        await message.answer('<a href="https://chenk.ru/ru/life/chenk-onlayn.php">Прямая трансляция</a> '
                             'с камеры главного входа в ЧЭнК.', reply_markup=link_kb)
