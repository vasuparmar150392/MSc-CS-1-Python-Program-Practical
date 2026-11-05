print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 35: Demonstrate the Use of DataFrames in Python")
print("-" * 50)

import pandas as pd

data = {
    'Name': ['Vasu', 'Rahul', 'Amit'],
    'Age': [22, 23, 21],
    'Marks': [85, 90, 78]
}

df = pd.DataFrame(data)

print("Student DataFrame:")
print(df)

print("\nFirst Two Records:")
print(df.head(2))

print("\nStudent Names:")
print(df['Name'])