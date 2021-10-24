from selenium import webdriver

# настройка браузера для работы в автономном режиме
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=r'C:/Program Files (x86)/ChromeDriver/chromedriver.exe', options=options)


# создание, отправка и последующее удаление скриншота
async def send_screenshot(uid, url):
    import os
    from loader import bot

    await bot.send_message(uid, 'Секунду...')
    driver.get(url)

    # определение размеров скриншота
    driver.set_window_size(1000, 0)
    size = driver.execute_script('return document.documentElement.scrollHeight')
    driver.set_window_size(1000, size)

    # сохранение, отправка и удаление
    photo_path = f'{str(uid)}.png'
    driver.save_screenshot(photo_path)
    await bot.send_photo(uid, photo=open(photo_path, 'rb'))
    os.remove(photo_path)
