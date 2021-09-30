from aiogram import executor

# запуск бота
if __name__ == '__main__':
    from handlers.for_admin import start_message, shutdown_message
    from handlers.welcome import dp
    from handlers.years.list import dp
    from handlers.years.second_year import dp
    from handlers.bells_schedule import dp
    from handlers.back import dp
    executor.start_polling(dp, on_startup=start_message, on_shutdown=shutdown_message)
