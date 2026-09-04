print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 11: Demonstrate use of List and various functions")
print("-" * 50)

# 1. Initializing a list
my_list = [10, 20, 30, "apple", "banana"]
print(f"1. Initial list: {my_list}")

# 2. append() - Adds an element at the end of the list
my_list.append(40)
print(f"2. After append(40): {my_list}")

# 3. insert() - Inserts an element at a specified index
my_list.insert(1, 35)
print(f"3. After insert(1, 35): {my_list}")

# 4. extend() - Adds all elements of an iterable to the end
my_list.extend(["orange", 50])
print(f"4. After extend(['orange', 50]): {my_list}")

# 5. remove() - Removes the first occurrence of a value
my_list.remove(30)
print(f"5. After remove(30): {my_list}")

# 6. pop() - Removes and returns element at given index (default last)
popped_item = my_list.pop(0)
print(f"6. After pop(0): {my_list} (Removed element: {popped_item})")

# 7. len() - Returns the total number of elements in the list
print(f"7. Length of list: {len(my_list)}")

# 8. count() - Returns the number of occurrences of an element
my_list.append("banana")
print(f"8. Count of 'banana': {my_list.count('banana')}")

# 9. index() - Returns the index of the first occurrence of a value
print(f"9. Index of 'banana': {my_list.index('banana')}")

# 10. sort() - Sorts the list (demonstrated on numeric list)
num_list = [42, 10, 55, 2, 60, 53]
print(f"\nNumeric list before sorting: {num_list}")
num_list.sort()
print(f"10. After sort() (Ascending): {num_list}")
num_list.sort(reverse=True)
print(f"    After sort(reverse=True) (Descending): {num_list}")

# 11. reverse() - Reverses the elements of the list in place
num_list.reverse()
print(f"11. After reverse(): {num_list}")

# 12. clear() - Removes all elements from the list
num_list.clear()
print(f"12. After clear(): {num_list}")
