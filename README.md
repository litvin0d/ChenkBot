# ChenkBot

### Описание
**ChenkBot** - это Telegram-бот, позволяющий смотреть
расписание пар и звонков для Челябинского Энергетического
колледжа им. С.М.Кирова. Глвавная его функция - просмотр
расписания пар, реализована в виде отправки скриншота с сайта
колледжа. По мимо этого, бот может отправлять заренее заготовленные
фотографии расписания звонков, а также ссылку на сервис просмотра
онлайн трансляции с камеры главного входа в колледж.

Ссылка на бота в Telegram: https://t.me/chenky_bot

___

### Принцип работы и реализация
Данный Telegram-бот написан на языке **Python**.
Для работы самого бота используется библиотека **aiogram**,
главной особенностью которой является её асинхронность,
позволяющая быстро обрабатывать поступающие запросы.

Для получения скриншота расписания используется библиотека 
**Selenium**, в которую входит программный интерфейс
**WebDriver** для управления браузером. Бот взаимодействует с
сайтом колледжа через браузер Chrome, для работы с которым также
необходим **chromedriver**.

#### Алгоритм получения и отправки расписания пар:
* Запуск браузера в headless режиме
* Переход по заранее заготовленной ссылке
* Создание и сохраниние скриншота страницы в память
* Отправка скриншота пользователю
* Удаление скриншота из памяти

Реализация в виде кода:
```python
from selenium import webdriver

# настройка браузера для работы в автономном режиме
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)
driver.set_window_size(1000, 1000) # задаём размер скриншота

# создание, отправка и удаление скриншота
photo_path = f'{str(uid)}.png'  # uid - id чата
driver.get(url)  # url - ссылка на сайт
driver.save_screenshot(photo_path)
await bot.send_photo(uid, photo=open(photo_path, 'rb'))
os.remove(photo_path)  # удаление скриншта
```
___

### Установка библиотек и настройка бота

Прежде чем начать работать с ботом, необходимо установить ряд
библиотек:
* `pip install aiogramm`
* `pip install selenium`
* `pip install asyncio`

Также необхомо установить *chromedriver* для работы с Chrome,
скачать его можно [здесь](https://chromedriver.chromium.org).
После скачивания, необходимо поместить
`chromedriver.exe` в диск, на который установлена система
и добавить его в PATH (для Windows).

Перед запуском бота нужно указать его токен. Сделать это можно
в файле `/data/config.py` в переменной `TOKEN`. В этом же
файле в списке `admins` необходимо указать id одного или
нескольких администраторов бота.
```python
TOKEN = '1234567890:ABcd7f98dsf0Sdjf008Ldk2f'
admins = ['123456789']
```

В случае ошибки, файле `/utils/screenshot.py` в переменной `driver`
возможно потребуется изменить путь до chromedriver'а:

```python
driver = webdriver.Chrome(executable_path=r'C:/путь_до_файла', options=options)
```
___

*Токен бота, который вы могли заметить
в предыдущих коммитах, больше не актуален.*
