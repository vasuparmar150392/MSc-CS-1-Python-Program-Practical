print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 54: Identify Suspicious URLs")
print("-" * 50)

# Identify suspicious keywords in a URL.
# Accept URL from the user
url = input("Enter a URL: ")

# List of suspicious keywords
words = ["login", "verify", "bank", "free", "password"]

# Convert URL into lowercase
url = url.lower()

# Check suspicious keywords
found = False

for word in words:
    if word in url:
        print("Suspicious keyword found:", word)
        found = True

if found:
    print("Warning: URL needs further inspection")
else:
    print("No listed suspicious keywords found")
