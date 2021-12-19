from aiogram import executor

if __name__ == '__main__':
    # импорт всех хэндлеров
    from handlers.on_startup import on_startup
    from handlers.welcome import dp

    from handlers.admin_panel.admin_panel import dp
    from handlers.admin_panel import rings_changes
    rings_changes.register_handlers_admin(dp)
    from handlers.admin_panel.users_num import dp

    from handlers.courses.list import dp
    from handlers.courses.course_1 import dp
    from handlers.courses.course_2 import dp
    from handlers.courses.course_3 import dp
    from handlers.courses.course_4 import dp

    from handlers.about import dp
    from handlers.chenk_online import dp
    from handlers.rings import dp
    from handlers.error import dp

    # запуск бота
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
