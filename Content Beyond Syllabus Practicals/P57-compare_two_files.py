print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 57: Compare Two Files")
print("-" * 50)

import os
import sys

# Check whether two files contain identical data.
script_dir = os.path.dirname(__file__)

if len(sys.argv) >= 3:
    file1_path = sys.argv[1]
    file2_path = sys.argv[2]
else:
    file1_path = os.path.join(script_dir, "P51-Random_Password.py")
    file2_path = os.path.join(script_dir, "P52-OTP_Generation.py")

# Read first file
file1 = open(file1_path, "r")
data1 = file1.read()
file1.close()

# Read second file
file2 = open(file2_path, "r")
data2 = file2.read()
file2.close()

# Compare file contents
if data1 == data2:
    print("Both files are identical")
else:
    print("Files are different")
