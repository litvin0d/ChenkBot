from selenium import webdriver

# настройка браузера для работы в автономном режиме
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=r'C:/Program Files (x86)/ChromeDriver/chromedriver.exe', options=options)
driver.set_window_size(1000, 1000)


async def send_screenshot(uid, url):
    import os
    from loader import bot

    await bot.send_message(uid, 'Секунду...')
    # создание, отправка и удаление скриншота
    photo_path = f'{str(uid)}.png'
    driver.get(url)
    driver.save_screenshot(photo_path)
    await bot.send_photo(uid, photo=open(photo_path, 'rb'))
    # driver.quit()
    os.remove(photo_path)
