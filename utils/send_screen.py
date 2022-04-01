from selenium import webdriver

from data.config import WEBDRIVER_PATH, SCREEN_PATH

# configuring the browser to work in headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=WEBDRIVER_PATH, options=options)


# creating, sending and then deleting a screenshot
async def send_screen(chat_id, url):
    import os

    from keyboards import timetable_link
    from loader import bot

    loading_message = await bot.send_message(chat_id, '<i>Загрузка</i>')
    await loading_message.edit_text('<i>Загрузка.</i>')

    driver.get(url)

    # determining the size of the screenshot
    driver.set_window_size(1080, 0)
    size = driver.execute_script('return document.documentElement.scrollHeight')
    driver.set_window_size(1080, size)

    await loading_message.edit_text('<i>Загрузка..</i>')

    photo_path = SCREEN_PATH + str(chat_id) + '.png'  # creating a path for a screenshot
    driver.save_screenshot(photo_path)  # saving a screenshot
    await loading_message.edit_text('<i>Загрузка...</i>')
    await loading_message.delete()  # delete loading message
    await bot.send_photo(
        chat_id,
        photo=open(photo_path, 'rb'),
        reply_markup=timetable_link(url)
    )  # sending a screenshot
    os.remove(photo_path)  # deleting a screenshot
