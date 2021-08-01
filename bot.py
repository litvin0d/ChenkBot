import telebot
import os
from telebot import types
from selenium import webdriver

# создание бота (токен бота указать в ковычках)
bot = telebot.TeleBot('TOKEN', parse_mode=None)

# настройка браузера для работы в автономном режиме
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')

# функция получения и отправки скрина
def get_screenshot(uid, url):
    photo_path = str(uid) + '.png'
    driver = webdriver.Chrome(chrome_options = options)
    driver.set_window_size(900, 900)
    driver.get(url)
    driver.save_screenshot(photo_path)
    bot.send_photo(uid, photo = open(photo_path, 'rb'))
    driver.quit()
    os.remove(photo_path)

# команда /start
@bot.message_handler(commands=['start'])
def welcome(message):
    # создание клавиатуры из кнопок выбора группы и расписания звонков
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    choose = types.KeyboardButton('Выбрать группу')
    bells = types.KeyboardButton('Расписание звонков')
    keyboard.add(choose, bells)
    # приветствие и добавление клавиатуры в чат
    bot.send_message(message.chat.id, 'Привет!\nЭтот бот позволит тебе быстро узнать актуальное расписание пар.', reply_markup=keyboard)

# выбор группы и отправка скриншота
@bot.message_handler(content_types=['text'])
def groups(message):
    # создаёт список групп в виде клавиатуры из кнопок, если был выбран вариант 'Выбрать группу'
    if message.text == 'Выбрать группу':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        gr1_20 = types.KeyboardButton('ТТО 1-20')
        gr2_20 = types.KeyboardButton('ЭССиС 2-20')
        gr3_20 = types.KeyboardButton('ЭССиС 3-20')
        gr4_20 = types.KeyboardButton('ЭС 4-20')
        gr5_20 = types.KeyboardButton('ЭП 5-20')
        gr6_20 = types.KeyboardButton('СА 6-20')
        gr7_20 = types.KeyboardButton('ИСП 7-20')
        gr8_20 = types.KeyboardButton('ИСП 8-20')
        gr18_20 = types.KeyboardButton('ИСП 18-20')
        # создаёт кнопку 'назад' для возвращения к клавиатуре 'выбор группы' и 'расписание звонков'
        back = types.KeyboardButton('Назад')
        keyboard.add(gr1_20, gr2_20, gr3_20, gr4_20, gr5_20, gr6_20, gr7_20, gr8_20, gr18_20, back)
        # добавляет кнопки в чат
        bot.send_message(message.chat.id, 'Выбери группу:', reply_markup=keyboard)
   
    # отправляет нужный скриншот в зависимости от выбранной группы
    elif message.text == 'ТТО 1-20':
        uid = message.chat.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=246&dep=3'
        get_screenshot(uid, url)
    elif message.text == 'ЭССиС 2-20':
        uid = message.chat.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=247&dep=3'
        get_screenshot(uid, url)
    elif message.text == 'ЭССиС 3-20':
        uid = message.chat.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=248&dep=3'
        get_screenshot(uid, url)
    elif message.text == 'ЭС 4-20':
        uid = message.chat.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=249&dep=3'
        get_screenshot(uid, url)
    elif message.text == 'ЭП 5-20':
        uid = message.chat.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=250&dep=3'
        get_screenshot(uid, url)
    elif message.text == 'СА 6-20':
        uid = message.chat.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=251&dep=3'
        get_screenshot(uid, url)
    elif message.text == 'ИСП 7-20':
        uid = message.chat.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=252&dep=3'
        get_screenshot(uid, url)
    elif message.text == 'ИСП 8-20':
        uid = message.chat.id
        url = "https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=253&dep=3"
        get_screenshot(uid, url)
    elif message.text == 'ИСП 18-20':
        uid = message.chat.id
        url = "https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=254&dep=3"
        get_screenshot(uid, url)
    # возвращает клавиатуру 'Выбор группы' и 'Расписание звонков'
    elif message.text == 'Назад':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        choose = types.KeyboardButton('Выбрать группу')
        bells = types.KeyboardButton('Расписание звонков')
        keyboard.add(choose, bells)
        bot.send_message(message.chat.id, 'Выбери действие:', reply_markup=keyboard)
        
    # отправляет фотографию расписания звоноков    
    elif message.text == 'Расписание звонков':
        bot.send_photo(message.chat.id, photo=open('bells.png', 'rb'))
    

# запуск бота
if __name__ == '__main__':
    bot.infinity_polling()
