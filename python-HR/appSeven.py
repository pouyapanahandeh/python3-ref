# for loop in python

# here we iterate through the string we defined
for item in 'pooya':
	print(item)
	
# iterate through the array

for index in ['pooya', 'amir', 'flix']:
	print(index)
	
for indexer in [1,2,3,4,5,6]:
	print(indexer)

# range start from 0 to range < desire number, here is ten
for i in range(10):
	print(i)
	
# using range include start from, till desire number, and stepping,. by using range we print even number from 2 to 9
for j in range(2, 10, 2):
	print(j)
	
# sum up the number of array
prices = [6, 22, 33]
total = 0
for price in prices:
	total += price
print(f'the Total is: {total}')

# nested for loop

for x in range(4):
	for y in range(4):
		print(f'({x},{y})')
	