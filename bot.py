# from aiogram import executor
import logging
from aiogram.utils.executor import start_webhook

import middlewares
from data.config import WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT
from loader import dp
from utils.startup import on_startup, on_shutdown
# noinspection PyUnresolvedReferences
import handlers

middlewares.setup(dp)
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    # # bot launch
    # executor.start_polling(
    #     dispatcher=dp,
    #     on_startup=on_startup,
    #     on_shutdown=on_shutdown,
    #     skip_updates=True,
    # )

    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT
    )
