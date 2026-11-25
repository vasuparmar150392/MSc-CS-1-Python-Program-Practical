print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 42: Accept a Domain Name and Show Basic WHOIS Information")
print("-" * 50)

import whois

domain = input("Enter domain name: ")

data = whois.whois(domain)

print("\nBasic WHOIS Information")
print("Domain Name:", data.domain_name)
print("Registrar:", data.registrar)
print("Creation Date:", data.creation_date)
print("Expiration Date:", data.expiration_date)
print("Name Servers:", data.name_servers)

