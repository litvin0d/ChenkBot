from aiogram import executor
import logging

import middlewares
from loader import dp
from utils.startup import on_startup, on_shutdown
# noinspection PyUnresolvedReferences
import handlers

middlewares.setup(dp)
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    # bot launch
    executor.start_polling(
        dispatcher=dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
    )
