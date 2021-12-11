import sqlite3
conn = sqlite3.connect ('redersclub_website/tests/Emp.db')
cur=conn.cursor()
cur.execute('SELECT age FROM Employee_Record where emp_id=3;')

records=cur.fetchall()
print(records)