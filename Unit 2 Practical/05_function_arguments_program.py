print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 5: Demonstrate various types of function arguments")
print("-" * 50)

# 1. Positional Arguments
# The arguments are passed to the function in the correct positional order.
def student_info(name, age, course):
    print(f"   Name: {name}, Age: {age}, Course: {course}")

print("1. Positional Arguments:")
student_info("Vasu Parmar", 21, "MSc Cyber Security")


# 2. Keyword Arguments
# Parameters are identified by argument names during the function call.
print("\n2. Keyword Arguments (Order does not matter):")
student_info(course="MSc Cyber Security", age=22, name="Aman")


# 3. Default Arguments
# If no argument is provided, the default value is used.
def greet_user(name, greeting="Welcome to Python Programming"):
    print(f"   Hello {name}, {greeting}!")

print("\n3. Default Arguments:")
greet_user("Vasu")                             # Uses default greeting
greet_user("Riya", "Good Morning")             # Overrides default greeting


# 4. Variable-Length Positional Arguments (*args)
# Allows passing any number of positional arguments as a tuple.
def calculate_total(*numbers):
    total = sum(numbers)
    print(f"   Passed Numbers: {numbers} -> Total Sum: {total}")

print("\n4. Variable-Length Positional Arguments (*args):")
calculate_total(10, 20)
calculate_total(10, 20, 30, 40, 50)


# 5. Variable-Length Keyword Arguments (**kwargs)
# Allows passing any number of keyword arguments as a dictionary.
def display_profile(username, **details):
    print(f"   Username: {username}")
    for key, value in details.items():
        print(f"     - {key.capitalize()}: {value}")

print("\n5. Variable-Length Keyword Arguments (**kwargs):")
display_profile("vasu_07", Role="Admin", Department="Cyber Security", Status="Active")
