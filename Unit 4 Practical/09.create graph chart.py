print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 39: Create Graph using Matplotlib")
print("-" * 50)

import matplotlib.pyplot as plt
students = ['Vasu', 'Rahul', 'Amit', 'Raj']
marks = [85, 90, 75, 80]
plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()
