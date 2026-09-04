#Name: Vasu Parmar
#Enrollment: 92600565007

print("Name: Vasu Parmar")
print("Enrollment: 92600565007")

#Q.5 Python program to find fibonacci sequence

n=int(input("Enter the number: "))

a=0
b=1
for i in range (n):
    a,b=b,a+b
    print(a)