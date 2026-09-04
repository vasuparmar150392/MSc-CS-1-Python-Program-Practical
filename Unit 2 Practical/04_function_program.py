print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 14: Python Programs to create a function")
print("-" * 50)

# Function 1: Check if a number is Even or Odd
def check_even_odd(number):
    """Function to check whether a given number is even or odd."""
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"


# Function 2: Calculate factorial of a number
def calculate_factorial(n):
    """Function to compute the factorial of a non-negative integer."""
    if n < 0:
        return "Factorial does not exist for negative numbers"
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


# Function 3: Calculate Student Grade based on marks percentage
def calculate_grade(marks):
    """Function to determine grade based on marks percentage."""
    if marks >= 90:
        return "Grade A+"
    elif marks >= 75:
        return "Grade A"
    elif marks >= 60:
        return "Grade B"
    elif marks >= 50:
        return "Grade C"
    elif marks >= 40:
        return "Grade D"
    else:
        return "Fail"


# Demonstrating Function Calls:
print("1. Testing Even/Odd Function:")
print("  ", check_even_odd(16))
print("  ", check_even_odd(7))

print("\n2. Testing Factorial Function:")
print("   Factorial of 5:", calculate_factorial(5))
print("   Factorial of 0:", calculate_factorial(0))

print("\n3. Testing Grade Calculation Function:")
print("   Marks: 85 ->", calculate_grade(85))
print("   Marks: 68 ->", calculate_grade(68))
print("   Marks: 32 ->", calculate_grade(32))
