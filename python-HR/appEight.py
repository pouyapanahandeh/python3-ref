# list in python

# List is a collection which is ordered and changeable. Allows duplicate members.

names = ['pooya', 'amir', 'jim', 'jeniffer']
print(names) # print the list as we write it

# index printing in array

print(names[0])

# print from index 1 till end

print(names[1:])

# print the end of the array

print(names[-1])

print(names) # as you can see here, those operation didn't change element of the list	

# changing element of the list 

names[0] = 'mohammad'	# change the first element of the array
print(names)

# find the largest number in the list

number = [1,2,3,4,5,6,7]
maxnum = number[0]

# example to find the largest number in the list

for i in number:
	if i > maxnum:
		maxnum = number[i]
print(maxnum)

# 2D list 

matrix = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]

print(matrix)

# print specific list in list

print(matrix[0])

# access to element in 2D list

print(matrix[0][2])

for row in matrix:
	for column in row:
		print([column])