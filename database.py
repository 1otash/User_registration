import sqlite3

db = sqlite3.connect("registration.db")
reg_list = db.cursor()
reg_list.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER, username TEXT, phone_number TEXT)')


def register_user(user_id, username, phone_number):
    db = sqlite3.connect("registration.db")
    reg_list = db.cursor()
    reg_list.execute("INSERT INTO users (user_id, username, phone_number) values (?, ?, ?);", (user_id, username, phone_number))
    db.commit()


def check_user(user_id):
    db = sqlite3.connect('registration.db')

    reg_list = db.cursor()

    checker = reg_list.execute('SELECT user_id FROM users WHERE user_id=?;', (user_id,))

    if checker.fetchone():
        return True
    else:
        return False


reg_list.close()

