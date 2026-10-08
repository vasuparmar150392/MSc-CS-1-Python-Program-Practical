# 2.Python programs to demonstrate the use of various forms of inheritance 

print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)

# multilevel inheritance 

class Security:
    def protect(self):
        print("System protection is enabled")

class NetworkSecurity(Security):
    def monitor_network(self):
        print("Network traffic is monitored")

class Firewall(NetworkSecurity):
    def block_traffic(self):
        print("Malicious traffic is blocked")

f = Firewall()
f.protect()
f.monitor_network()
f.block_traffic()        

# multiple inheritance 

class Encryption:
    def encrypt(self):
        print("Data is encrypted")

class Authentication:
    def authenticate(self):
        print("User authentication is performed")

class SecureSystem(Encryption, Authentication):
    def secure_data(self):
        print("System provides secure data access")

s = SecureSystem()
s.encrypt()
s.authenticate()      
s.secure_data()

# hierarchical inheritance

class SecuritySystem:
    def monitor(self):
        print("Network is being monitored")

class  IDS(SecuritySystem):
    def detect(self):
        print("IDS detects suspicious activity")

class IPS(SecuritySystem):
    def prevent(self):
        print("IPS prevents malicious activity")        

i = IDS()        
p = IPS()

i.monitor()
i.detect()
p.prevent()