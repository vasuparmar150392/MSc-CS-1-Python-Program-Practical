print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 43: Display Domain Creation Date Using WHOIS")
print("-" * 50)

import whois

domain = input("Enter domain name: ")

data = whois.whois(domain)

print("Domain Name:", domain)
print("Registrar Name:", data.registrar)
