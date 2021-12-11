import sqlite3
conn = sqlite3.connect ('readersclub_website/tests/Emp.db')
cur = conn.cursor()
#cur.execute("CREATE TABLE Employee_Record(Emp_ID INTEGER PRIMARY KEY AUTOINCREMENT, Emp_Name TEXT, Age INTEGER);")
print("table created")

emp_name=input('Whats your name')
emp_age=int(input('Whats your age'))

cur.execute('INSERT INTO Employee_Record(Emp_Name,Age) VALUES(?,?);',[emp_name,emp_age])
conn.commit()
conn.close()