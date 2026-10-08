# Python program to demonstrate the use of various modes of files

print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)

# w+ - write and read mode

file = open ("cyber_security.txt", "w+")
file.write("security report \n")
file.write("theret analysis completed. \n")
file.seek(0)
print("w+ mode:")
print(file.read())
file.close()

# r+ - read and write mode 

file = open ("cyber_security.txt", "r+")
print("r+ Mode:")
print(file.read())
file.write("additional data using r+ mode.\n")
file.close()



# a+ append and read mode

file = open ("cyber_security.txt", "a+")
file.write("security report updated \n")
file.seek(0)
print("a+ mode:")
print(file.read())
file.close()
