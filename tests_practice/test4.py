import sqlite3
conn=sqlite3.connect('Employee.db')
cur=conn.cursor()
#Creating a table
cur.execute('CREATE TABLE Employee_Record(Emp_ID INTEGER PRIMARY KEY AUTOINCREMENT, Emp_Name TEXT, Age INTEGER);')
#Inserting values into the table
cur.execute('INSERT INTO Employee_Record(Emp_Name, Age) Values("Regina", 25);')
cur.execute('INSERT INTO Employee_Record(Emp_Name, Age) Values("Alex", 31);')
cur.execute('INSERT INTO Employee_Record(Emp_Name, Age) Values("Anika", 23);')
cur.execute('INSERT INTO Employee_Record(Emp_Name, Age) Values("Peter", 34);')
cur.execute('INSERT INTO Employee_Record(Emp_Name, Age) Values("Jenny", 28);')
conn.commit()
print("Table created & inserted values into it")