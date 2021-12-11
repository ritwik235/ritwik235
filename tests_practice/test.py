import sqlite3
conn = sqlite3.connect ('readersclub_website/tests/Emp.db')
cur=conn.cursor()
cur.execute('CREATE TABLE Students_Record(Roll_No INTEGER PRIMARY KEY, Student_Name TEXT, Age INTEGER);')
print("Table created")