import sqlite3 as sql


async def sql_start():
    global connect, cursor
    connect = sql.connect('users.db')
    cursor = connect.cursor()

    if connect:
        print('Database connected successfully!')

    connect.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER,
        username TEXT,
        full_name TEXT
    )''')
    connect.commit()


async def sql_add(data):
    usr_id = data[0]
    cursor.execute(f'SELECT id FROM users WHERE id = {usr_id}')
    match = cursor.fetchone()
    if match is None:
        cursor.execute('INSERT INTO users VALUES(?, ?, ?);', data)
        connect.commit()
