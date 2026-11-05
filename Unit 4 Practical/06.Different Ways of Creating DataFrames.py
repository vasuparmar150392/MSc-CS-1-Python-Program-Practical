print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 36: Different Ways of Creating DataFrames")
print("-" * 50)

import pandas as pd
import numpy as np

# Using Dictionary
data1 = {
    'Name': ['Vasu', 'Rahul'],
    'Marks': [85, 90]
}

df1 = pd.DataFrame(data1)
print("Using Dictionary:")
print(df1)

# Using List
data2 = [
    ['Vasu', 85],
    ['Rahul', 90]
]

df2 = pd.DataFrame(
    data2,
    columns=['Name', 'Marks']
)

print("\nUsing List:")
print(df2)

# Using List of Dictionaries
data3 = [
    {'Name': 'Vasu', 'Marks': 85},
    {'Name': 'Rahul', 'Marks': 90}
]

df3 = pd.DataFrame(data3)
print("\nUsing List of Dictionaries:")
print(df3)

# Using NumPy Array
data4 = np.array([
    ['Vasu', 85],
    ['Rahul', 90]
])

df4 = pd.DataFrame(
    data4,
    columns=['Name', 'Marks']
)

print("\nUsing NumPy Array:")
print(df4)