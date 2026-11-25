print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 41: Python Program to Perform WHOIS Lookup")
print("-" * 50)

import whois

domain = input("Enter domain name: ")

result = whois.whois(domain)

print("\nWHOIS Information:")
print(result)