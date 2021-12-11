import sqlite3
#to connect with database
conn=sqlite3.connect("readers.db")
cur=conn.cursor
print("database created")
conn.commit()
conn.close()