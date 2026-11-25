print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 55: Identify Potentially Risky File Extensions")
print("-" * 50)

# Identify potentially risky file extensions.
# Accept file name
filename = input("Enter file name: ")

# List of potentially risky extensions
extensions = [".exe", ".bat", ".vbs", ".scr", ".cmd"]

# Check file extension
if filename.lower().endswith(tuple(extensions)):
    print("Potentially risky file")
else:
    print("Extension not in the risky list")
