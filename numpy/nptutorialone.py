# numpy is multi dimensional array library that we can use it instead of using list. lists are slow and numpy is fast.
# numpy has a less byte compared to lists.
import numpy as np

one_dim = np.array([1,2,3,4,5])
print(one_dim)

two_dim = np.array([[1.,2,3,4,5],[6,7,8,9,10]])
print(two_dim)

print("----------------------------------------------------------------")

# print the number of dimensions of and array
print(two_dim.ndim)

print("----------------------------------------------------------------")

# print the number of rows and column

print(two_dim.shape)
print(one_dim.shape)

print("----------------------------------------------------------------")

# get the type of the array

print(two_dim.dtype)

print("----------------------------------------------------------------")

# we can specify the size of array if we know how large the number is

three_dim = np.array([5,8,1], dtype="int32")
four_dim = np.array([5,8,1], dtype="int16")
print(three_dim.dtype)
print(four_dim.dtype)

# same array but have different size, it's because of the dtype that we specified
# size of each item
print(three_dim.itemsize)
print(four_dim.itemsize)

print("----------------------------")
print("SIZE")

print(one_dim.size) # shows the size of the array

# get total size of the array in bytes
print(one_dim.size * one_dim.itemsize)
# or
print(one_dim.nbytes)

