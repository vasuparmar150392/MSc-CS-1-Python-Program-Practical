print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 51-Random Password Generator")
print("-" * 50)

#Write a Python program to generate a random password.

# Import random module
import random

# Define characters for password
characters = "abcdefghijk123456789@#$"

# Create an empty password
password = ""

# Generate 8 characters
for i in range(8):
    password = password + random.choice(characters)

# Display password
print("Generated Password:", password)
