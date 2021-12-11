import sqlite3
conn=sqlite3.connect('database/readersclub.db')
cur=conn.cursor()
# cur.execute('CREATE TABLE members_registration \
#             (id INTEGER PRIMARY KEY AUTOINCREMENT,\
#             name TEXT,username TEXT, \
#             age INTEGER,email TEXT,password TEXT,\
#             gender TEXT);')
# print('table is created')
 
cur.execute('''CREATE TABLE feedback
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            feedback TEXT);''')
print("table created")
conn.close()

