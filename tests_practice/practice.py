import sqlite3
conn=sqlite3.connect('readers.db')
cur=conn.cursor()
cur.execute("""CREATE TABLE leaderboard
(id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
score INTEGER,
grade INTEGER,
class INTEGER);""")
print("Leaderboard created")
conn.commit()
conn.close()
