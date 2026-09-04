print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 13: demonstrate the use of dictionary and various functions")
print("-" * 50)

# 1. Creating a Dictionary
student_dict = {
    'Name': 'Zara',
    'Age': 7,
    'Class': 'First',
    'Department': 'Cyber Security'
}
print("1. Initial Dictionary:")
print("  ", student_dict)

# 2. Accessing Elements
print("\n2. Accessing Elements:")
print("   Direct access student_dict['Name']:", student_dict['Name'])
print("   Using get() method student_dict.get('Age'):", student_dict.get('Age'))
print("   Using get() with default value:", student_dict.get('Grade', 'Not Assigned'))

# 3. Adding and Updating Elements
print("\n3. Adding & Updating Elements:")
student_dict['Age'] = 8                      # Updating existing key
student_dict['School'] = "DPS School"        # Adding new key-value pair
student_dict.update({'City': 'Rajkot', 'Marks': 95})  # Using update()
print("   Updated Dictionary:", student_dict)

# 4. Dictionary Methods (keys, values, items)
print("\n4. Dictionary Built-in Methods:")
print("   Keys:", list(student_dict.keys()))
print("   Values:", list(student_dict.values()))
print("   Key-Value Pairs (Items):", list(student_dict.items()))
print("   Total pairs (len):", len(student_dict))

# 5. Removing Elements (pop, popitem, del, clear)
print("\n5. Removing Elements:")
popped_val = student_dict.pop('Marks')
print(f"   After pop('Marks'): (Removed value: {popped_val})")
print("   Current Dict:", student_dict)

popped_item = student_dict.popitem()
print(f"   After popitem(): (Removed item: {popped_item})")
print("   Current Dict:", student_dict)

del student_dict['School']
print("   After del student_dict['School']:", student_dict)

# 6. Properties of Dictionary Keys
print("\n6. Properties of Dictionary Keys:")
# Property A: Duplicate keys are not allowed (last assignment overwrites)
dup_key_dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Vasu'}
print("   Duplicate keys overwrite previous value:", dup_key_dict)

# Property B: Keys must be immutable (hashable). Lists cannot be keys.
try:
    invalid_dict = {['Course']: 'Cyber Security'}
except TypeError as e:
    print("   Trying to use list as a key raises TypeError:", e)
    print("   Tuple (immutable) CAN be a key:")
    valid_dict = {('Course', 'Year'): 'MSc 2026'}
    print("   Valid Dict with Tuple key:", valid_dict)

# 7. Clearing Dictionary
student_dict.clear()
print("\n7. After clear():", student_dict)
