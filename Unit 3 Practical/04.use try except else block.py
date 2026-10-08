# Write a Python program to use try–except–else block.

print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)

try:
    number = int(input("Enter a number: "))
    print("You entered: ", number)

except ValueError:
    print("Error: invaild input. Please enter a number.")    