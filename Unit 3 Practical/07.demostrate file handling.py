# Python program to demostrate file handling 

print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)

# create and write data or file 
file = open ("security_log.txt", "w")
file.write("cyber secuirty lab\n")
file.write("MSc cyber securty and cyber law\n")
file.write("file handling is important for managing security log")
file.close()

# read data form the file

file = open("security_log.txt", "r")
data = file.read()
print("file contents:")
print(data)
file.close()

# append new data to the file

file = open("security_log.txt", "a")
file.write("\n\nnew security event recorded.\n")
file.close()

# read the updated file

file = open("security_log.txt", "r")
print("updated file contents")
print(file.read())
file.close()



