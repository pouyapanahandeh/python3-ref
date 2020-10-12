import numpy as np

# Load data from file
data = np.genfromtxt('data.txt', delimiter = ',', dtype = "int32")
print(data)

print('--------------------------------')

# boolean masking
print(data <= 20)

