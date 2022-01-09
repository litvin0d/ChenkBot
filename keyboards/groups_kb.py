from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# group selection keyboards for each course

# first course
groups1 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
gr1_21 = KeyboardButton('👷‍♂ ТТО 1-21 👷‍♂')
gr2_21 = KeyboardButton('👨‍🔧 ЭССиС 2-21 👨‍🔧')
gr3_21 = KeyboardButton('👨‍🔧 ЭССиС 3-21 👨‍🔧')
gr4_21 = KeyboardButton('👨‍🔧 ЭС 4-21 👨‍🔧')
gr5_21 = KeyboardButton('👨‍🔧 ЭП 5-21 👨‍🔧')
gr6_21 = KeyboardButton('👨‍💼 СА 6-21 👨‍💼')
gr7_21 = KeyboardButton('👨‍💻 ИСП 7-21 👨‍💻')
gr8_21 = KeyboardButton('👨‍💻 ИСП 8-21 👨‍💻')
gr9_21 = KeyboardButton('👨‍💻 ИСП 9-21 👨‍💻')
back = KeyboardButton('🔙 Назад 🔙')
groups1.add(gr1_21, gr2_21, gr3_21, gr4_21, gr5_21, gr6_21, gr7_21, gr8_21, gr9_21, back)

contents1 = ['👷‍♂ ТТО 1-21 👷‍♂', '👨‍🔧 ЭССиС 2-21 👨‍🔧',
             '👨‍🔧 ЭССиС 3-21 👨‍🔧', '👨‍🔧 ЭС 4-21 👨‍🔧',
             '👨‍🔧 ЭП 5-21 👨‍🔧', '👨‍💼 СА 6-21 👨‍💼',
             '👨‍💻 ИСП 7-21 👨‍💻', '👨‍💻 ИСП 8-21 👨‍💻',
             '👨‍💻 ИСП 9-21 👨‍💻']

# second course
groups2 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
gr1_20 = KeyboardButton('👷‍♂ ТТО 1-20 👷‍♂')
gr2_20 = KeyboardButton('👨‍🔧 ЭССиС 2-20 👨‍🔧')
gr3_20 = KeyboardButton('👨‍🔧 ЭССиС 3-20 👨‍🔧')
gr4_20 = KeyboardButton('👨‍🔧 ЭС 4-20 👨‍🔧')
gr5_20 = KeyboardButton('👨‍🔧 ЭП 5-20 👨‍🔧')
gr6_20 = KeyboardButton('👨‍💼 СА 6-20 👨‍💼')
gr7_20 = KeyboardButton('👨‍💻 ИСП 7-20 👨‍💻')
gr8_20 = KeyboardButton('⭐ ИСП 8-20 ⭐')
groups2.add(gr1_20, gr2_20, gr3_20, gr4_20, gr5_20, gr6_20, gr7_20, gr8_20, back)

contents2 = ['👷‍♂ ТТО 1-20 👷‍♂', '👨‍🔧 ЭССиС 2-20 👨‍🔧',
             '👨‍🔧 ЭССиС 3-20 👨‍🔧', '👨‍🔧 ЭС 4-20 👨‍🔧',
             '👨‍🔧 ЭП 5-20 👨‍🔧', '👨‍💼 СА 6-20 👨‍💼',
             '👨‍💻 ИСП 7-20 👨‍💻', '⭐ ИСП 8-20 ⭐']

# third course
groups3 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
gr1_19 = KeyboardButton('👷‍♂ ТТО 1-19 👷‍♂')
gr2_19 = KeyboardButton('👨‍🔧 ЭССиС 2-19 👨‍🔧')
gr3_19 = KeyboardButton('👨‍🔧 ЭССиС 3-19 👨‍🔧')
gr4_19 = KeyboardButton('👨‍🔧 ЭС 4-19 👨‍🔧')
gr5_19 = KeyboardButton('👨‍🔧 ЭП 5-19 👨‍🔧')
gr6_19 = KeyboardButton('👨‍💼 СА 6-19 👨‍💼')
gr7_19 = KeyboardButton('👨‍💻 ИСП 7-19 👨‍💻')
gr8_19 = KeyboardButton('👨‍💻 ИСП 8-19 👨‍💻')
groups3.add(gr1_19, gr2_19, gr3_19, gr4_19, gr5_19, gr6_19, gr7_19, gr8_19, back)

contents3 = ['👷‍♂ ТТО 1-19 👷‍♂', '👨‍🔧 ЭССиС 2-19 👨‍🔧',
             '👨‍🔧 ЭССиС 3-19 👨‍🔧', '👨‍🔧 ЭС 4-19 👨‍🔧',
             '👨‍🔧 ЭП 5-19 👨‍🔧', '👨‍💼 СА 6-19 👨‍💼',
             '👨‍💻 ИСП 7-19 👨‍💻', '👨‍💻 ИСП 8-19 👨‍💻']

# fourth course
groups4 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
gr1_18 = KeyboardButton('👷‍♂ ТТО 1-18 👷‍♂')
gr2_18 = KeyboardButton('👨‍🔧 ЭССиС 2-18 👨‍🔧')
gr3_18 = KeyboardButton('👨‍🔧 ЭП 3-18 👨‍🔧')
gr4_18 = KeyboardButton('👨‍🔧 ЭС 4-18 👨‍🔧')
gr5_18 = KeyboardButton('👨‍🔧 ЭП 5-18 👨‍🔧')
gr6_18 = KeyboardButton('👨‍💼 СА 6-18 👨‍💼')
gr7_18 = KeyboardButton('👨‍💻 ИСП 7-18 👨‍💻')
gr8_18 = KeyboardButton('👨‍💻 ИСП 8-18 👨‍💻')
groups4.add(gr1_18, gr2_18, gr3_18, gr4_18, gr5_18, gr6_18, gr7_18, gr8_18, back)

contents4 = ['👷‍♂ ТТО 1-18 👷‍♂', '👨‍🔧 ЭССиС 2-18 👨‍🔧',
             '👨‍🔧 ЭП 3-18 👨‍🔧', '👨‍🔧 ЭС 4-18 👨‍🔧',
             '👨‍🔧 ЭП 5-18 👨‍🔧', '👨‍💼 СА 6-18 👨‍💼',
             '👨‍💻 ИСП 7-18 👨‍💻', '👨‍💻 ИСП 8-18 👨‍💻']
