#Read numpy.nditer docs
#https://numpy.org/devdocs/reference/generated/numpy.nditer.html#numpy.nditer
import numpy as np, os
os.system("cls")

a = np.arange(12).reshape(3,4)
print(a,"\n")
for cell in np.nditer(a,order='C'): #in the columns order
    print(cell,end=" ")
print("\n")
for cell in np.nditer(a,order='F'): #in the rows(Fortran) order
    print(cell,end=" ")
print("\n")
for x in np.nditer(a,order='F',flags=["external_loop"]): #external_loop for column values
    print(x, end=" ")
b = np.arange(3).reshape(3,1)
print("\n")
#iterate teo arrays simultaneously but either their dimensions should be same or one of the dimension in one of the array should be one this is called as general broadcasting rule(read in documentation)
for x,y in np.nditer([a,b]): 
    print(x,y)




input()