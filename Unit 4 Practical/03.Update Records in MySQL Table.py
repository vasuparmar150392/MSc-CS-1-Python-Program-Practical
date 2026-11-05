print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 33: Update Records in MySQL Table")
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
    "UPDATE student SET marks = %s WHERE id = %s",
    (95, 1)
)

con.commit()

cur.execute("SELECT * FROM student")

for row in cur.fetchall():
    print(row)

con.close()