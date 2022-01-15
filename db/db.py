import sqlite3


con = sqlite3.connect('db.db')
cur = con.cursor()


cur.execute("INSERT INTO logs VALUES ('Hello', '21:44 15.01.2022', 'Sergey')")

con.commit()
con.close()