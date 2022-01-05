from aiogram.types import Message

from loader import dp
from data.received_messages import received_messages


# ответ на неопознанное сообщение
@dp.message_handler()
async def unknown_msg(message: Message):
    if message.text not in received_messages:
        await message.answer('Воспользуйся встроенной клавиатурой либо перезагрузи бота командой /start!')
