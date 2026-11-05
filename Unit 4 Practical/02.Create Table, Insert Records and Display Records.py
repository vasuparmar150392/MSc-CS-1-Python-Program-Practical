print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 32: Create Table, Insert Records and Display Records")
print("-" * 50)

import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college"
    )
except mysql.connector.Error:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    cur = con.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS college")
    con.commit()
    con.close()

    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college"
    )

cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    marks INT
)
""")

cur.execute(
    "INSERT INTO student (id, name, marks) VALUES (%s, %s, %s)",
    (1, "Vasu", 85)
)

con.commit()

cur.execute("SELECT * FROM student")
records = cur.fetchall()

for row in records:
    print(row)

con.close()
