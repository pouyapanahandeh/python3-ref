# array in python

cars = ["honda","mazda","kia"]

for x in cars:
	print(x)
	
# array following Index
	
print(cars[2])
print(cars[0])

# change element in array 

cars[0] = "benz"

for x in cars:
	print(x)
	
# the length of array 

y = len(cars)
print(y)

# add element to array

cars.append("opel")
print(cars)

# pop element from array 

cars.pop(1)
print(cars)

# remove element in array

cars.remove("kia")
print(cars)



