print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 46: Using re – Detect Emails Using Regular Expressions")
print("-" * 50)

import re

text = input("Enter text: ")

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, text)

print("\nEmail Addresses Found:")

for email in emails:
    print(email)