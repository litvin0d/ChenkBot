from aiogram import executor

# запуск бота
if __name__ == '__main__':
    # импорт всех хэндлеров
    from handlers.for_admin import start_message, shutdown_message
    from handlers.welcome import dp
    from handlers.courses.list import dp
    from handlers.courses.course_1 import dp
    from handlers.courses.course_2 import dp
    from handlers.courses.course_3 import dp
    from handlers.courses.course_4 import dp
    from handlers.chenk_online import dp
    from handlers.bells_schedule import dp

    executor.start_polling(dp, on_startup=start_message, on_shutdown=shutdown_message)
