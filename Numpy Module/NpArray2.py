import numpy as n

a = n.array([1,2,3,4,5,6,7,8,9])
print(a[0:4])
print(a[3:9:2])
print(a[::-1])
print(a[7:0:-2])
print()
a2 = n.array([  [1,2,3],
                [4,5,6],
                [7,8,9]  ])
print(a2[1,2]) #element of 1st row and 2nd column (i.e. a12 = 5)
print(a2[0:2,1:3])
print(a2[-1]) #last row
print(a2[:,1:])
for row in a2:
    print(row)
for row in a2:
    for column in row:
        print(column,end=" ")
    print()
for cell in a2.flat: #it will not alter the original array
    print(cell, end=" ")
print()
#_______________OR_______________#
for cell in a2.flatten(): #it will not alter the original array
    print(cell, end=" ")
print()
print(a2) #you can see here original array is not altered
print()

a = n.arange(6).reshape(3,2)
b = n.arange(6,12).reshape(3,2)
print(n.vstack((a,b))) #argument in the form of tuple
print(n.hstack((a,b))) #argument in the form of tuple
print()

a = n.arange(30).reshape(2,15)
print("Original array is: ")
print(a)
result = n.hsplit(a,3) #split array into 3 horizontal arrays
for i,element in enumerate(result):
    print(f"Array{i+1} is :")
    print(element)
result = n.vsplit(a,2) #split array into 2 vertical arrays
for i,element in enumerate(result):
    print(f"Array{i+1} is :")
    print(element)
print()
a = n.arange(12).reshape(3,4)
b = a > 4
print(b)
print(a[b]) #wherever b is true print all those values of a
#    OR
print(a[a>4]) #directly extract values of a those are >4
a[b] = -1 #wherever b is true modify the value of a at that place as -1 (i.e. => a[a>4] = -1)
print(a)