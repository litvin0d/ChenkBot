import sqlite3 as sql


# подключение к базе данных или её создание
async def db_start():
    global connect, cursor
    connect = sql.connect('users.db')
    cursor = connect.cursor()
    # connect_act = sql.connect('active.db')

    if connect:
        print('Databases connected successfully!')

    connect.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER,
        username TEXT,
        full_name TEXT
    )''')
    connect.commit()

    # connect_act.execute('''CREATE TABLE IF NOT EXISTS active(
    #     id INTEGER,
    #     username TEXT,
    #     full_name TEXT
    # )''')
    # connect_act.commit()


# добавление данных в базу
async def db_add(user_data):
    uid = user_data[0]
    cursor.execute(f'SELECT id FROM users WHERE id = {uid}')
    match = cursor.fetchone()
    if match is None:
        cursor.execute('INSERT INTO users VALUES(?, ?, ?);', user_data)
        connect.commit()


# # добавление данных в базу активных пользователей
# async def db_act_add(user_data):
#     uid = user_data[0]
#     cursor.execute(f'SELECT id FROM active WHERE id = {uid}')
#     match = cursor.fetchone()
#     if match is None:
#         cursor.execute('INSERT INTO active VALUES(?, ?, ?);', user_data)
#         connect.commit()


# количество записей в базе
async def db_users_num():
    cursor.execute('SELECT Count(*) FROM users')
    users_num = cursor.fetchone()
    return users_num[0]


# async def db_active_num():
#     cursor.execute('SELECT Count(*) FROM active')
#     active_num = cursor.fetchone()
#     return active_num[0]


# возвращение всех id в виде массива
async def db_users_id():
    cursor.execute('SELECT id FROM users')
    users_id = cursor.fetchall()
    return users_id
