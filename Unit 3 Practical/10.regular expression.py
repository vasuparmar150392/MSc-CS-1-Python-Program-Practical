print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)

# Python programs to demonstrate the use of regular expression

import re

# 1 . searching for a pattern

import re
text = "Cybersecurity Lab 2026"

if re.search(r'\d',text):
    print("1.The srting contains a number.")
else:
    print("1.String does not contain number .")

# 2 . Extracting Emails

text_with_emails = "contact us at vasu@ac.in "

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]'
emails = re.findall(email_pattern , text_with_emails)
print("2.Extracted mail : ", emails)

# 3. Validating a phone number

phone = "9454648117"

if re.fullmatch(r'\d{10}', phone ):
    print("3.Valid phone number .", phone)
else:
    print("3.Invalid phone number .", phone)        

# 4. Finding capitalized  word

sentence = "Python Is Fun and Important"

capital_words = re.findall(r'b[A-Z] [a-z] *\b', sentence)
print ("4.Words starting with capital letters :", capital_words)

# 5. Replacing digits

text_with_digits = "Server123 has IP456"

replaced_text = re.sub(r'\d', '#', text_with_digits)
print("5.Text after replacing digits :", replaced_text)
