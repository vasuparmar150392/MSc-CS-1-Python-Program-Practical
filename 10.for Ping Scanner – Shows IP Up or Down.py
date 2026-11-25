print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 50:for Ping Scanner – Shows IP Up or Down")
print("-" * 50)

#Python program for Ping Scanner shows ip up or down
import os   # Import os module to run system commands like 'ping'

# Loop from 1 to 5 → this will generate IPs: 192.168.1.1 to 192.168.1.5
for i in range(1, 6):

    ip = f"192.168.1.{i}"   # Create IP address by adding i at the end

    # Run the ping command once (-c 1)
    # > /dev/null hides the ping output from the terminal
    # os.system returns 0 if ping is successful, otherwise non-zero
    response = os.system(f"ping -c 1 {ip}")

    if response == 0:   # If response is 0, the IP replied → system is UP
        print(f"{ip} is UP")
    else:               # If response is not 0 → system is DOWN
        print(f"{ip} is DOWN")