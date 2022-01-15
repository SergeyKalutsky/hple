from datetime import datetime
import sqlite3


con = sqlite3.connect('db/db.db')


def log_message(message, author):
    date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    cur = con.cursor()
    cur.execute(f"INSERT INTO logs VALUES ('{message}', '{date}', '{author}')")
    con.commit()
    