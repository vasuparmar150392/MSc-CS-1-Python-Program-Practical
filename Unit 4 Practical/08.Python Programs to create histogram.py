print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 38: Create Histogram using Matplotlib")
print("-" * 50)

import matplotlib.pyplot as plt
marks = [
    45, 50, 55, 60, 65, 70, 75,
    80, 85, 90, 95, 60, 70, 80
]
plt.hist(marks, bins=5, edgecolor='black')
plt.title("Student Marks Histogram")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()


