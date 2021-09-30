from aiogram.types import Message

from loader import dp
from data.received_messages import received_messages


@dp.message_handler()
async def support(message: Message):
    if message.text not in received_messages:
        await message.answer('Воспользуйся встроенной клавиатурой!')
