from selenium import webdriver

# настройка браузера для работы в автономном режиме
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=r'C:/Program Files (x86)/ChromeDriver/chromedriver.exe', options=options)


# создание, отправка и последующее удаление скриншота
async def send_screen(chat_id, url):
    import os
    from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

    from loader import bot

    loading_message = await bot.send_message(chat_id, '<i>Загрузка</i>')
    await loading_message.edit_text('<i>Загрузка.</i>')

    driver.get(url)

    # определение размеров скриншота
    driver.set_window_size(1000, 0)
    size = driver.execute_script('return document.documentElement.scrollHeight')
    driver.set_window_size(1000, size)

    await loading_message.edit_text('<i>Загрузка..</i>')

    # создание inline-клавиатуры для прикрепления под последующей фотографией
    switch_kb = InlineKeyboardMarkup()
    prev_btn = InlineKeyboardButton(text='Открыть в браузере', url=url)
    switch_kb.add(prev_btn)

    await loading_message.edit_text('<i>Загрузка...</i>')

    # сохранение, отправка и удаление
    photo_path = str(chat_id) + '.png'
    driver.save_screenshot(photo_path)
    await loading_message.delete()  # удаление сообщения о загрузке
    await bot.send_photo(chat_id, photo=open(photo_path, 'rb'), reply_markup=switch_kb)
    os.remove(photo_path)
