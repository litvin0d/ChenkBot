from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from loader import bot
from utils.database import db_users_id


# панель управления рассылкой
async def mailing(message: Message):
    if message.text == '✉ Рассылка ✉':
        await message.answer('Управление рассылкой:\n'
                             '/send - провести рассылку\n'
                             '/cancel - отменить рассылку')


# объявление машины состояний
class FSMailing(StatesGroup):
    message = State()


# активация машины состояний
async def upload_msg_text(message: Message):
    await FSMailing.message.set()
    await message.answer('Отправь текст рассылки:')


# получение текста и выполнение рассылки
async def save_msg_text(message: Message, state: FSMContext):
    if message.text != '/cancel':
        users_id = await db_users_id()
        text = message.text
        for i in range(len(users_id)):
            await bot.send_message(users_id[i][0], text)

        await message.reply('Рассылка выполнена!')
        await state.finish()

    # выход из состояний
    else:
        await message.answer('Рассылка отменена!')
        await state.finish()


def register_handlers_mailing(dp: Dispatcher):
    dp.register_message_handler(mailing, text='✉ Рассылка ✉')
    dp.register_message_handler(upload_msg_text, commands='send', state=None)
    dp.register_message_handler(save_msg_text, state=FSMailing.message)
