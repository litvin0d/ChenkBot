from aiogram import executor

import middlewares
from loader import dp
from utils.on_startup import on_startup

middlewares.setup(dp)

# noinspection PyUnresolvedReferences
import handlers


if __name__ == '__main__':
    # from handlers.admin_panel import rings_changes
    # rings_changes.register_handlers_admin(dp)

    # запуск бота
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
