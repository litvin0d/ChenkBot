from aiogram.types import Message

from loader import dp


@dp.message_handler(text='✨ Поддержка ✨')
async def support(message: Message):
    if message.text == '✨ Поддержка ✨':
        await message.answer('Для того, чтобы бот функионировал, '
                             'необходимо ежемесячно оплачивать его хостинг. '
                             'Поддержать работу бота:\n'
                             '4276721509679478')
