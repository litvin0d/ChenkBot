from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State

from data.config import admins
from loader import dp


# панель управление изменениями
@dp.message_handler(text='📝 Изменения в расп. звонков 📝')
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
@dp.message_handler(commands='upload', state=None)
async def upload_changes(message: Message):
    if message.from_user.id in admins:
        await FSMAdmin.photo.set()
        await message.answer('Отправь фото изменений:')
    else:
        await message.answer('Тебе недоступна данная команда!')


# ловим ответ и сохраняем данные
@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def save_changes(message: Message, state: FSMContext):
    with open('data/rings_changes.txt', 'w') as file:
        file.write(message.photo[0].file_id)

    await message.reply('Изменения сохранены!')
    await state.finish()


# выход из состояний
@dp.message_handler(state="*", commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state="*")
async def cancel_changes(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.answer('Отменено!')
    await state.finish()


# удаление изменений
@dp.message_handler(commands='delete')
async def delete_changes(message: Message):
    if message.from_user.id in admins:
        with open('data/rings_changes.txt', 'w') as file:
            file.write('')
        await message.answer('Изменения удалены!')
    else:
        await message.answer('Тебе недоступна данная команда!')
