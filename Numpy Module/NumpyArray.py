import numpy, sys, time

#python list
list = [x for x in range(1000)]
a = 10
print("Python list size of 1000 elements of int type:",sys.getsizeof(a)*len(list))

#numpy array
arr = numpy.array(numpy.arange(1000))
print("Numpy array size of 1000 elements of int type:",arr.size)

print()

SIZE = 10000000
l1 = range(SIZE)
l2 = range(SIZE)
startTime = time.time()
addLists = [x+y for x,y in zip(l1,l2)]
print(f"Python list adding time: {(time.time() - startTime)*1000:.20f} ms")

a1 = numpy.arange(SIZE)
a2 = numpy.arange(SIZE)
startTime = time.time()
addArray = a1 + a2
print(f"Numpy array adding time: {(time.time() - startTime)*1000:.2f} ms")
# print(dir(addArray))
# print(help(addArray))
