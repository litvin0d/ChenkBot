from aiogram import executor

if __name__ == '__main__':
    # импорт всех хэндлеров
    from handlers.for_admin import for_admin
    from handlers.welcome import dp
    from handlers.courses.list import dp
    from handlers.courses.course_1 import dp
    from handlers.courses.course_2 import dp
    from handlers.courses.course_3 import dp
    from handlers.courses.course_4 import dp
    from handlers.chenk_online import dp
    from handlers.rings import dp
    from handlers.about import dp
    from handlers.error import dp

    # запуск бота
    executor.start_polling(dp, on_startup=for_admin, skip_updates=True)
