# Python programs to demonstrate the use of regular expression

print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)

# searching for a pattern

import re
text = "Cybersecurity Lab "

if re.search(r'\d',text):
    print("1.The srting contains a number.")
else:
    print("2.No number found in the string .")
    
