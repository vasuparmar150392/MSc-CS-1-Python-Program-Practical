print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 34: Delete Records from MySQL Table")
print("-" * 50)

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

cur = con.cursor()

cur.execute(
    "DELETE FROM student WHERE id = %s",
    (1,)
)

con.commit()

cur.execute("SELECT * FROM student")

for row in cur.fetchall():
    print(row)

con.close()