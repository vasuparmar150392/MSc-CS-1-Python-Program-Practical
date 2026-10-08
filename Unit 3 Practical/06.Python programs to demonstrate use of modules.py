# Python programs to demonstrate use of modules 

print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)

import math
import random

# 1. Using the math module
number = 16
square_root = math.sqrt(number)
print(f"The square root of {number} is: {square_root}")
print(f"Value of Pi: {math.pi}")

# 2. Using the random module
random_score = random.randint(1, 100) # Generates a random integer between 1 and 100
print(f"Your random score is: {random_score}")
