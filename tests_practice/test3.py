import sqlite3 
conn=sqlite3.connect('readersclub_website/tests/Emp.db')
cur=conn.cursor()

#Creating a table
#cur.execute('CREATE TABLE Employees_Record(Emp_ID INTEGER PRIMARY KEY AUTOINCREMENT, Emp_Name TEXT, Contact TEXT, Department TEXT, Salary INTEGER );')
#Inserting values into the table
cur.execute('INSERT INTO Employees_Record(Emp_Name, Contact, Department, Salary) Values("Regina K", "080-251477", "Sales", 20000);')
cur.execute('INSERT INTO Employees_Record(Emp_Name, Contact, Department, Salary) Values("Alex","9898911111", "Testing", 25000);')
cur.execute('INSERT INTO Employees_Record(Emp_Name, Contact, Department, Salary) Values("Anika", "+91-9422783232", "Testing", 20000);')
cur.execute('INSERT INTO Employees_Record(Emp_Name, Contact, Department, Salary) Values("Peter", "8881217777", "Development", 40000);')
cur.execute('INSERT INTO Employees_Record(Emp_Name, Contact, Department, Salary) Values("Jenny", "8797224151", "Sales", 35000);')
conn.commit()
print("Created table & inserted values into it")