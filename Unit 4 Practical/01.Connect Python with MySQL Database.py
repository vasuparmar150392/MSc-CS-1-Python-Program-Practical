print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 31: Connect Python with MySQL Database")
print("-" * 50)

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",   # replace with your actual MySQL password
    database=""            # optional: use your database name
)

if con.is_connected():
    print("Database Connected Successfully")

con.close()
