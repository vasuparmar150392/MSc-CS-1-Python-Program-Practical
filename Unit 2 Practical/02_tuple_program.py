print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 12: Demonstrate use of Tuple and various functions")
print("-" * 50)

# 1. Tuple Creation
tup1 = ('Physics', 'Chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print("1. Initial Tuples:")
print("   tup1:", tup1)
print("   tup2:", tup2)

# 2. Accessing Elements (Indexing and Slicing)
print("\n2. Accessing Elements:")
print("   tup1[0] (First element):", tup1[0])
print("   tup1[-1] (Last element):", tup1[-1])
print("   tup2[1:5] (Slicing [1:5]):", tup2[1:5])
print("   tup1[1:] (Slicing [1:]):", tup1[1:])
print("   tup1[:3] (Slicing [:3]):", tup1[:3])

# 3. Tuple Operations (Concatenation and Repetition)
print("\n3. Tuple Operations:")
tup3 = tup1 + tup2
print("   Concatenation (tup1 + tup2):", tup3)
tup_repeat = ('Cyber', 'Security') * 2
print("   Repetition (('Cyber', 'Security') * 2):", tup_repeat)

# 4. Built-in Functions on Tuples
print("\n4. Built-in Functions:")
print("   len(tup1):", len(tup1))
numbers_tup = (10, 50, 20, 80, 30, 50)
print("   Numeric Tuple:", numbers_tup)
print("   max(numbers_tup):", max(numbers_tup))
print("   min(numbers_tup):", min(numbers_tup))
print("   sum(numbers_tup):", sum(numbers_tup))

# 5. Tuple Methods (count, index)
print("\n5. Tuple Methods:")
print("   Count of 50 in numbers_tup:", numbers_tup.count(50))
print("   Index of 80 in numbers_tup:", numbers_tup.index(80))

# 6. Membership Testing
print("\n6. Membership Testing:")
print("   'Physics' in tup1:", 'Physics' in tup1)
print("   100 in numbers_tup:", 100 in numbers_tup)

# 7. Tuple Packing and Unpacking
print("\n7. Tuple Packing & Unpacking:")
student_tuple = ("Vasu", 21, "MSc Cyber Security")  # Packing
name, age, course = student_tuple                   # Unpacking
print(f"   Unpacked -> Name: {name}, Age: {age}, Course: {course}")
