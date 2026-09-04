# Name: Vasu Parmar
# Enrollment: 92600565007

# Q.7 Python program to find largest and smallest element in an array
print("Name: Vasu Parmar")
print("Enrollment: 92600565007")

arr = [23, 5, 89, 45, 12, 7]

largest = arr[0]
smallest = arr[0]

for i in arr:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest element:", largest)
print("Smallest element:", smallest)
