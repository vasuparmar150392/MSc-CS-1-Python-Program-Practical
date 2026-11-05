print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 37: Create Pie Chart using Matplotlib")
print("-" * 50)

import matplotlib.pyplot as plt  # type: ignore[reportMissingModuleSource]

subjects = ['Python', 'Java', 'C++', 'PHP']
marks = [40, 30, 20, 10]

plt.pie(
    marks,
    labels=subjects,
    autopct='%1.1f%%'
)

plt.title("Subject Marks Distribution")
plt.show()
