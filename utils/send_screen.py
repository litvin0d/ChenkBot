from selenium import webdriver

# configuring the browser to work in headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=r'C:/Program Files (x86)/ChromeDriver/chromedriver.exe', options=options)


# creating, sending and then deleting a screenshot
async def send_screen(chat_id, url):
    import os
    from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

    from loader import bot

    loading_message = await bot.send_message(chat_id, '<i>Загрузка</i>')
    await loading_message.edit_text('<i>Загрузка.</i>')

    driver.get(url)

    # determining the size of the screenshot
    driver.set_window_size(1000, 0)
    size = driver.execute_script('return document.documentElement.scrollHeight')
    driver.set_window_size(1000, size)

    await loading_message.edit_text('<i>Загрузка..</i>')

    # creating an inline keyboard for attaching under a photo
    switch_kb = InlineKeyboardMarkup()
    prev_btn = InlineKeyboardButton(text='Открыть в браузере', url=url)
    switch_kb.add(prev_btn)

    await loading_message.edit_text('<i>Загрузка...</i>')

    photo_path = f'img/{str(chat_id)}.png'  # creating a path for a screenshot
    driver.save_screenshot(photo_path)  # saving a screenshot
    await loading_message.delete()  # delete loading message
    await bot.send_photo(chat_id, photo=open(photo_path, 'rb'), reply_markup=switch_kb)  # sending a screenshot
    os.remove(photo_path)  # deleting a screenshot
