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
    driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\ChromeDriver\chromedriver.exe', options=options)
    driver.set_window_size(900, 900)
    driver.get(url)
    driver.save_screenshot(photo_path)
    bot.send_photo(uid, photo=open(photo_path, 'rb'))
    driver.quit()
    os.remove(photo_path)


# команда /start
@bot.message_handler(commands=['start'])
def welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    couples = types.KeyboardButton('🗓 Расписание пар 🗓')
    bells = types.KeyboardButton('⏳ Расписание звонков ⏳')
    videcam = types.KeyboardButton('📸 ЧЭнК Онлайн 📸')
    support = types.KeyboardButton('✨ Поддержка ✨')
    keyboard.add(couples, bells, videcam, support)
    bot.send_message(message.chat.id, '👋 Привет! 👋\n'
                                      'ChenkBot поможет тебе быстро узнаить актуальное '
                                      'расписание пар и звонков.', reply_markup=keyboard)


# выбор группы и отправка скриншота
@bot.message_handler(content_types=['text'])
def groups(message):
    # список курсов
    if message.text == "🗓 Расписание пар 🗓":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        first_grade = types.KeyboardButton('1⃣ Первый курс 1⃣')
        second_grade = types.KeyboardButton('2⃣ Второй курс 2⃣')
        third_grade = types.KeyboardButton('3⃣ Третий курс 3⃣')
        fourth_grade = types.KeyboardButton('4⃣ Четвёртый курс 4⃣')
        back = types.KeyboardButton('🔙 Назад 🔙')
        keyboard.add(first_grade, second_grade, third_grade, fourth_grade, back)
        bot.send_message(message.chat.id, 'На каком ты курсе?', reply_markup=keyboard)

    # группы первого курса
    elif message.text == '1⃣ Первый курс 1⃣':
        bot.send_message(message.chat.id, 'На данный момент расписание пар доступно '
                                          'только для групп второго курса.')

    # группы второго курса
    elif message.text == '2⃣ Второй курс 2⃣':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        gr1_20 = types.KeyboardButton('👷‍♂ ТТО 1-20 👷‍♂')
        gr2_20 = types.KeyboardButton('👨‍🔧 ЭССиС 2-20 👨‍🔧')
        gr3_20 = types.KeyboardButton('👨‍🔧 ЭССиС 3-20 👨‍🔧')
        gr4_20 = types.KeyboardButton('👨‍🔧 ЭС 4-20 👨‍🔧')
        gr5_20 = types.KeyboardButton('👨‍🔧 ЭП 5-20 👨‍🔧')
        gr6_20 = types.KeyboardButton('👨‍💼 СА 6-20 👨‍💼')
        gr7_20 = types.KeyboardButton('👨‍💻 ИСП 7-20 👨‍💻')
        gr8_20 = types.KeyboardButton('👨‍💻 ИСП 8-20 👨‍💻')
        back_to_grades = types.KeyboardButton('🔙 Выбрать курс 🔙')
        keyboard.add(gr1_20, gr2_20, gr3_20, gr4_20, gr5_20, gr6_20, gr7_20, gr8_20, back_to_grades)
        bot.send_message(message.chat.id, 'В какой ты группе?', reply_markup=keyboard)
   
    # отправляет нужный скриншот в зависимости от выбранной группы
    elif message.text == '👷‍♂ ТТО 1-20 👷‍♂':
        uid = message.chat.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=246&dep=3'
        get_screenshot(uid, url)
    elif message.text == '👨‍🔧 ЭССиС 2-20 👨‍🔧':
        uid = message.chat.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=247&dep=3'
        get_screenshot(uid, url)
    elif message.text == '👨‍🔧 ЭССиС 3-20 👨‍🔧':
        uid = message.chat.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=248&dep=3'
        get_screenshot(uid, url)
    elif message.text == '👨‍🔧 ЭС 4-20 👨‍🔧':
        uid = message.chat.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=249&dep=3'
        get_screenshot(uid, url)
    elif message.text == '👨‍🔧 ЭП 5-20 👨‍🔧':
        uid = message.chat.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=250&dep=3'
        get_screenshot(uid, url)
    elif message.text == '👨‍💼 СА 6-20 👨‍💼':
        uid = message.chat.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=251&dep=3'
        get_screenshot(uid, url)
    elif message.text == '👨‍💻 ИСП 7-20 👨‍💻':
        uid = message.chat.id
        url = 'https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=252&dep=3'
        get_screenshot(uid, url)
    elif message.text == '👨‍💻 ИСП 8-20 👨‍💻':
        uid = message.chat.id
        url = "https://pronew.chenk.ru/blocks/manage_groups/website/view.php?gr=253&dep=3"
        get_screenshot(uid, url)

    # группы третьего курса
    elif message.text == '3⃣ Третий курс 3⃣':
        bot.send_message(message.chat.id, 'На данный момент расписание пар доступно '
                                          'только для групп второго курса.')

    # группы четвёртого курса
    elif message.text == '4⃣ Четвёртый курс 4⃣':
        bot.send_message(message.chat.id, 'На данный момент расписание пар доступно '
                                          'только для групп второго курса.')

    # отправляет фотографию расписания звоноков
    elif message.text == '⏳ Расписание звонков ⏳':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        monday_friday = types.KeyboardButton('⏳ Понедельник-пятница ⏳')
        saturday = types.KeyboardButton('⏳ Суббота ⏳')
        back = types.KeyboardButton('🔙 Назад 🔙')
        keyboard.add(monday_friday, saturday, back)
        bot.send_message(message.chat.id, 'Какой день недели?', reply_markup=keyboard)
    elif message.text == '⏳ Понедельник-пятница ⏳':
        bot.send_photo(message.chat.id, photo=open('img/monday-friday.jpeg', 'rb'))
    elif message.text == '⏳ Суббота ⏳':
        bot.send_photo(message.chat.id, photo=open('img/saturday.jpeg', 'rb'))

    # ссылка на трансляцию с камеры
    elif message.text == '📸 ЧЭнК Онлайн 📸':
        bot.send_message(message.chat.id, 'Трансляция с камеры '
                                          'главного входа в колледж: '
                                          'https://chenk.ru/ru/life/chenk-onlayn.php')

    elif message.text == '✨ Поддержка ✨':
        bot.send_message(message.chat.id, 'На оплату хостинга для бота и булочку с маком в буфете 🙃:\n'
                                          'СБЕР: 4276721509679478')

    # кнопки назад
    elif message.text == '🔙 Выбрать курс 🔙':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        first_grade = types.KeyboardButton('1⃣ Первый курс 1⃣')
        second_grade = types.KeyboardButton('2⃣ Второй курс 2⃣ ')
        third_grade = types.KeyboardButton('3⃣ Третий курс 3⃣')
        fourth_grade = types.KeyboardButton('4⃣ Четвёртый курс 4⃣')
        back = types.KeyboardButton('🔙 Назад 🔙')
        keyboard.add(first_grade, second_grade, third_grade, fourth_grade, back)
        bot.send_message(message.chat.id, 'На каком ты курсе?', reply_markup=keyboard)

    elif message.text == '🔙 Назад 🔙':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        couples = types.KeyboardButton('🗓 Расписание пар 🗓')
        bells = types.KeyboardButton('⏳ Расписание звонков ⏳')
        videcam = types.KeyboardButton('📸 ЧЭнК Онлайн 📸')
        support = types.KeyboardButton('✨ Поддержка ✨')
        keyboard.add(couples, bells, videcam, support)
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=keyboard)

    else:
        bot.send_message(message.chat.id, 'Воспользуйтесь встроеной клавиатурой.')

# запуск бота
bot.polling(none_stop=True)
