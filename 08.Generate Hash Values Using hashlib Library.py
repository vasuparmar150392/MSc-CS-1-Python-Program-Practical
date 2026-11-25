print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 48: Generate Hash Values Using hashlib Library")
print("-" * 50)

# Program to generate hash values of a string
import hashlib

text = "CyberSecurity123"

# MD5 Hash
md5_hash = hashlib.md5(text.encode())
print("MD5 Hash:", md5_hash.hexdigest())

# SHA1 Hash
sha1_hash = hashlib.sha1(text.encode())
print("SHA1 Hash:", sha1_hash.hexdigest())

# SHA256 Hash
sha256_hash = hashlib.sha256(text.encode())
print("SHA256 Hash:", sha256_hash.hexdigest())