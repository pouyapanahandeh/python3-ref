# Linear Algebra

import numpy as np

a = np.random.randint(8, size=(2,3))
b = np.random.randint(9, size=(3,2))
c = np.matmul(a,b)
print(c)

print("================================")

# matrix determinant
identical = np.identity(3)
print(identical)
print(np.linalg.det(identical))

print("================================")

# min, max and etc.
new_arr = np.array([[1,2,3,4],[5,6,7,8]])
print(new_arr.min())
print(new_arr.max())
# add all elements of the array to each other
print(new_arr.sum())