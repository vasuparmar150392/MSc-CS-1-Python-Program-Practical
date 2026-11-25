print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 52: One-Time Password (OTP) Generation")
print("-" * 50)

# Write a Python program to generate a six-digit One-Time Password (OTP).
# Import random module
import random

# Generate a six-digit OTP
otp = random.randint(100000, 999999)

# Display OTP
print("Your OTP is:", otp)
