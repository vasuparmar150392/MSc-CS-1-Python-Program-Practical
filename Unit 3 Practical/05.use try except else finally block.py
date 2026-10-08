# 5.Write a Python program to use try–except–finally block.

print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)

try:
    attempts = int(input ("Enter number of login attempts: "))
except ValueError:
    print("Error: invaild input. Please enter a number.")    
else:
    print("Login attempts recorded: ", attempts)
finally:
    print("Security check compelted.")

    