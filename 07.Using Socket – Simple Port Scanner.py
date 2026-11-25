print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 47: Using Socket – Simple Port Scanner")
print("-" * 50)

import socket

host = input("Enter IP address or hostname: ")

print("\nScanning Ports...")

for port in range(1, 1025):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((host, port))

    if result == 0:
        print("Port", port, "is OPEN")

    s.close()

print("\nScanning Completed.")