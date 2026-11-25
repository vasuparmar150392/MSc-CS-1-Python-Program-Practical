print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 49: os Library – Check Files in a Directory")
print("-" * 50)

import os

path = input("Enter directory path: ")

if os.path.exists(path):

    print("\nFiles in Directory:")

    for file in os.listdir(path):
        print(file)

else:
    print("Directory does not exist.")