from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State

from data.config import admins


# панель управление изменениями
async def rings_changes(message: Message):
    if message.text == '📝 Изменения в расп. звонков 📝':
        await message.answer('Управление изменениями:\n'
                             '/upload - загрузить изменения\n'
                             '/cancel - отменить загрузку\n'
                             '/delete - удалить изменения')


# объявление машины состояний
class FSMAdmin(StatesGroup):
    photo = State()


# активация машины состояний
async def upload_changes(message: Message):
    if message.from_user.id in admins:
        await FSMAdmin.photo.set()
        await message.answer('Отправь фото изменений:')
    else:
        await message.answer('Тебе недоступна данная команда!')


# ловим ответ и сохраняем данные
async def save_changes(message: Message, state: FSMContext):
    with open('../../rings_changes.txt', 'w') as file:
        file.write(message.photo[0].file_id)

    await message.reply('Изменения сохранены!')
    await state.finish()


# выход из состояний
async def cancel_changes(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.answer('Отменено!')
    await state.finish()


# удаление изменений
async def delete_changes(message: Message):
    if message.from_user.id in admins:
        with open('rings_changes.txt', 'w') as file:
            file.write('')
        await message.answer('Изменения удалены!')
    else:
        await message.answer('Тебе недоступна данная команда!')


# регивстрация хэндлеров для импорта в bot.py
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(rings_changes, text='📝 Изменения в расп. звонков 📝')
    dp.register_message_handler(upload_changes, commands='upload', state=None)
    dp.register_message_handler(save_changes, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(cancel_changes, state="*", commands='cancel')
    dp.register_message_handler(cancel_changes, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(delete_changes, commands='delete')
