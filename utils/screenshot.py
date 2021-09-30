async def send_screenshot(uid, url):
    from selenium import webdriver
    import os
    from loader import bot

    # настройка браузера для работы в автономном режиме
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')

    # создание, отправка и удаление скриншота
    photo_path = str(uid) + '.png'
    driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\Geckodriver\geckodriver.exe', options=options)
    driver.set_window_size(1000, 1000)
    driver.get(url)
    driver.save_screenshot(photo_path)
    await bot.send_photo(uid, photo=open(photo_path, 'rb'))
    driver.quit()
    os.remove(photo_path)
