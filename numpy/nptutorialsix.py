import numpy as np

main_arr = np.array([[1,2,3,4],[5,6,7,8]])

# print the number of row and column of a matrix
print(main_arr.shape)

print("----------------------------")

# reshape matrix
new_arr = main_arr.reshape((2,4))
print(new_arr)

print("----------------------------")

# vertically stacking vectors
vec_one = np.array([1,2,3,4])
vec_two = np.array([5,6,7,8])

print(np.vstack([vec_one, vec_two, vec_one, vec_two]))

print("----------------------------")

# Horizontally stacking vectors

print(np.hstack([vec_one, vec_two]))


