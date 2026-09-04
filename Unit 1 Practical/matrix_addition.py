#Name: Vasu Parmar
#Enrollment: 92600565007

print("Name: Vasu Parmar")
print("Enrollment: 92600565007")

#Q.8 Python program to add two matrix using array and function

#Using array
a= [[1,2,3],[4,5,6],[7,8,9]]
b= [[9,8,7],[6,5,4],[3,2,1]]

print("Matrix of a:")
for i in range (len (a)):
    for j in range (len(a[0])):
        print(a[i][j], end=" ")
    print("")

print("\nMatrix of b:")
for i in range (len (b)):
    for j in range (len(b[0])):
        print(b[i][j], end=" ")
    print("")

print("\n#Using Function\n")
def matrix_addition():
    a= [[1,3,2],[5,4,6],[8,7,9]]   
    b= [[8,9,7],[4,6,5],[3,1,2]]

    print("Matrix of a:")
    for i in range (len (a)):
        for j in range (len(a[0])):
            print(a[i][j], end=" ")
        print("")

    print("\nMatrix of b:")
    for i in range (len (b)):
        for j in range (len(b[0])):
            print(b[i][j], end=" ")
        print("")


matrix_addition()