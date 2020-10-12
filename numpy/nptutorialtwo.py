import numpy as np

arr_one = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr_one.size)
print(arr_one.itemsize)
print(arr_one.shape)
print(arr_one.nbytes)

# get specific index in multi dimensional array

print(arr_one[0,2])

# get specific row

print(arr_one[0 , :])

# get specific column

print(arr_one[: , 2])

# get specific interval in specific row 
# first 0 shows the number of row, the second zero shows the index number we want to target in first row, 5 represent the last number and 2 shows the step size
print(arr_one[0, 0:5:2])

# access to the element and change it
print(arr_one[1,3]) # output will be 9
arr_one[1,3] = 99
print(arr_one[1,3]) # output will be 99
print(arr_one)

# change all the number of specific dimension

print(arr_one[:, 2])

# we change all the number in column with the index number 3 to 6
arr_one[:,3] = 6
print(arr_one)

print("------------------------------")

# 3D examoles

arr_two = np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])
print(arr_two)

# 1 is the first dimension, 0 mean first matrix, and 4 refers to index number
print(arr_two[1,0,4]) # output will be 15

# all dimension second row, second column
print(arr_two[:,1,1])
# all dimension second row, all column
print(arr_two[:,1,:])
arr_two[:,1,:] = [[6,6,6,6,6],[9,9,9,9,9]]
print(arr_two)