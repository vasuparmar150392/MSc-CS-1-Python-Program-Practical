print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 40: Create Line Graph using Matplotlib")
print("-" * 50)

import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [100, 150, 120, 200, 250]

plt.plot(
    months,
    sales,
    marker='o',
    linestyle='-'
)

plt.title("Monthly Sales Report")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()