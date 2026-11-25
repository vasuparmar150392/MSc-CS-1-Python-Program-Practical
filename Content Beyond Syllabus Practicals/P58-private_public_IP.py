print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 58: Identify Private and Public IP Addresses")
print("-" * 50)

# Identify the category of an IP address.
# Import ipaddress module
import ipaddress

# Accept IP address
ip = input("Enter IP address: ")

try:
    address = ipaddress.ip_address(ip)

    if address.is_private:
        print("Private IP Address")
    else:
        print("Public IP Address")

except ValueError:
    print("Invalid IP address")

'''
1. What is a private IP address?
A private IP address is used within a local network, such as a home, college, office or computer laboratory.

The following IPv4 ranges are reserved for private networks:
Private IP range	Example
10.0.0.0 – 10.255.255.255	10.0.0.5
172.16.0.0 – 172.31.255.255	172.16.1.10
192.168.0.0 – 192.168.255.255	192.168.1.1

2. What is a public IP address?
A public IP address is generally used to identify a device or network on the internet. It is globally routable.

Examples:
- 8.8.8.8
- 1.1.1.1
- 142.250.183.14
'''


