# 3.Write a Python program to handle division by zero using try and except. 

print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)

a=10
b=0

try:
    print(a/b)
except Exception  as e:
    print(e)
print("hello")

a=10
b=0

try:
    print(a/b)
except Exception  as e:
    print("ohh it's error" ,e)

finally:    
    print("hello")


      
      
