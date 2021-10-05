from aiogram.types import Message

from loader import dp


@dp.message_handler(text='✨ Поддержать бота ✨')
async def support(message: Message):
    if message.text == '✨ Поддержать бота ✨':
        await message.answer('Для того, чтобы бот '
                             'стабильно функионировал, '
                             'необходимо ежемесячно '
                             'оплачивать его хостинг. '
                             'Поддержать бота:\n'
                             '4276721509679478 СБЕР')
