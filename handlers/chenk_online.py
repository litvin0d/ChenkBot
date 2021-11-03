from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp

link_kb = InlineKeyboardMarkup(row_width=1)
link_btn = InlineKeyboardButton(text='ЧЭнК Онлайн', url='https://chenk.ru/ru/life/chenk-onlayn.php')
link_kb.add(link_btn)


@dp.message_handler(text='📸 ЧЭнК Онлайн 📸')
async def chenk_online(message: Message):
    if message.text == '📸 ЧЭнК Онлайн 📸':
        await message.answer('<a href="https://chenk.ru/ru/life/chenk-onlayn.php">Прямая трансляция</a> '
                             'с камеры главного входа в ЧЭнК.', reply_markup=link_kb)
