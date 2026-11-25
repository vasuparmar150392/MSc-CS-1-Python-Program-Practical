print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 56: Count Failed Login Attempts")
print("-" * 50)

# Read a sample security log and count failed login attempts.
import os

# Open the sample log relative to this script
log_path = os.path.join(os.path.dirname(__file__), "login.txt")
file = open(log_path, "r")

# Initialize counter
count = 0

# Read each line
for line in file:
    if "Failed" in line:
        count = count + 1

# Display result
print("Failed login attempts:", count)

# Close file
file.close()
