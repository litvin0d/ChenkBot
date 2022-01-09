import sqlite3 as sql


# connecting to or creating a database
async def db_start():
    global connect, cursor
    connect = sql.connect('data/users.db')
    cursor = connect.cursor()

    if connect:
        print('Databases connected successfully!')

    connect.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER,
        username TEXT,
        full_name TEXT
    )''')
    connect.commit()


# adding a user to the database if he was not there
async def db_add(user_data):
    uid = user_data[0]
    cursor.execute(f'SELECT id FROM users WHERE id = {uid}')
    match = cursor.fetchone()
    if match is None:
        cursor.execute('INSERT INTO users VALUES(?, ?, ?);', user_data)
        connect.commit()


# number of users in the database
async def db_users_num():
    cursor.execute('SELECT Count(*) FROM users')
    users_num = cursor.fetchone()
    return users_num[0]


# returning all id's as an array
async def db_users_id():
    cursor.execute('SELECT id FROM users')
    users_id = cursor.fetchall()
    return users_id
