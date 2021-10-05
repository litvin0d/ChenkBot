import asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data.config import TOKEN

loop = asyncio.get_event_loop()
bot = Bot(token=TOKEN, parse_mode='HTML', loop=loop)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
