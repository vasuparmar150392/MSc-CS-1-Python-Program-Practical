print("Name: Vasu Parmar")
print("Enrollment: 92600565007")

# Q.2 Python program to do arithmetical operations


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b


num1 = 20
num2 = 5

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
