import numpy as np

init_arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(init_arr)

print("--------------------------------")

# All zero matrix 
zeros_one = np.zeros((1,2,2))
print(zeros_one)

# All ones matrix
ones_one = np.ones((1,2,2), dtype="int32")
print(ones_one)

# array with  specific number. (2,2) it shows shape, 4 is the number we wanna add to matrix.
arr_one = np.full((2,2), 4)
print(arr_one)

print("----------------------------------")

# full like method use when we want use an array that built before
print(np.full_like(init_arr, 2))

print("--------------------------------")

# random matrix
print(np.random.rand(4,4))

print("----------------------------")
print(np.random.rand(2,2,3))

print("----------------------------")
# random matrix with shape 
print(np.random.random_sample(init_arr.shape))

print("----------------------------")
# random matrix with integer value, random number below 5
print(np.random.randint(5, size=(3,3)))

print("----------------------------")
# random number in specific interval
print(np.random.randint(3,9, size=(4,4)))

print("----------------------------")
# create identical matrix, we only path one value, because identity matrix must be square
print(np.identity(3))

# copying array
n_arr = np.array([1,2,3,4])
o_arr = n_arr.copy()
o_arr[0] = 69
print(n_arr)
print(o_arr)

print("----------------------------")