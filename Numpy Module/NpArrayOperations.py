import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr)
print(arr.itemsize)
print(arr.shape)
print(arr.ndim)
print(arr.dtype)
print(arr.size)
print(np.sqrt(arr))
print(np.std(arr)) #standard deviation
print(arr.min())
print(arr.max())
print(arr.sum())
print()

a = np.array([[1,2],[3,4],[5,6]], dtype=np.float64)
print(a)
print(a.itemsize)
print(a.shape)
print(a.ndim)
print(a.dtype)
print(a.size)
print(a.sum())
print(a.sum(axis=0)) #sum of all rows into a single row
print(a.sum(axis=1)) #sum of all columns into a single row
print()

ar = np.array([[1,2],[3,4],[5,6]], dtype=np.complex64)
print(ar)
print()

arrayOfZeros = np.zeros((3,4), dtype=np.int64)
print(arrayOfZeros)
print()

arrayOfOnes = np.ones((3,4))
print(arrayOfOnes)
print()

l = np.arange(0,15,2)
print(l)
print()

linearlySpacedArray = np.linspace(1,5,10) # 1 to 5 (both inclusive) generate 10 numbers those are linearly spaced
print(linearlySpacedArray)
print()

reshapedArray = linearlySpacedArray.reshape(5,2)
print(reshapedArray)
print()

flattedArray = reshapedArray.ravel() # n dimensional to one dimensional array
print(flattedArray)
print()

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(a+b)
print(b-1)
print(b-a)
print(a*b)
print(b/a)
print(b//a)
print(b%a)
print(b>a)
print(b<=a)
print(a.dot(b))
print(np.dot(a,b))