from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State

from data.config import ADMINS
from loader import dp


# control panel for changes in rings schedule
@dp.message_handler(text='📝 Изменения в расп. звонков 📝')
async def rings_changes(message: Message):
    if message.text == '📝 Изменения в расп. звонков 📝':
        await message.answer('Управление изменениями:\n'
                             '/upload - загрузить изменения\n'
                             '/cancel - отменить загрузку\n'
                             '/delete - удалить изменения')


# state machine declaration
class FSMAdmin(StatesGroup):
    photo = State()


# state machine activation
@dp.message_handler(commands='upload', state=None)
async def upload_changes(message: Message):
    if message.from_user.id in ADMINS:
        await FSMAdmin.photo.set()
        await message.answer('Отправь фото изменений:')
    else:
        await message.answer('Тебе недоступна данная команда!')


# catching the answer and save the data
@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def save_changes(message: Message, state: FSMContext):
    with open('data/rings_changes.txt', 'w') as file:
        file.write(message.photo[0].file_id)

    await message.reply('Изменения сохранены!')
    await state.finish()


# exit from states
@dp.message_handler(state="*", commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state="*")
async def cancel_changes(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.answer('Отменено!')
    await state.finish()


# deleting changes
@dp.message_handler(commands='delete')
async def delete_changes(message: Message):
    if message.from_user.id in ADMINS:
        with open('data/rings_changes.txt', 'w') as file:
            file.write('')
        await message.answer('Изменения удалены!')
    else:
        await message.answer('Тебе недоступна данная команда!')
