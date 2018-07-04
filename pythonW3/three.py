# list in python and follow indexing rule, start from 0

thisList = ["pooya","mohammad","Mahdi","Alireza"]
print(thisList)

thisList[1] = "Eshghe Man"
print(thisList)

# The list() constructor include add item to list and delete the item

listTwo = list(("apple","melon","orange"))
print(listTwo)

# append() use to add item to the list

listTwo.append("mandarin")
print(listTwo)

# instead the way I did for removing the element we can write the name of item

listTwo.remove(listTwo[2])
print(listTwo)

# get the length of the list

print(len(listTwo))

# remove all the element of the list

print(thisList)
print(thisList.clear())

# copy of list and store in new var and we can print it

x = listTwo.copy()
print(x)

# by count() we can get how many time variable repeat

listOne = ["waac","nowo","carea","jento","nowo","waac","nowo"]
z = listOne.count("nowo")
print(z)
print(listOne.count(listOne[0]))

# built in function extend use to concat two list

listOne.extend(listTwo)
print(listOne)

# extend with integers 

points = (1,2,3,4,5,6)
listOne.extend(points)

print(listOne)

# get the index number of element in list, and you need to write the name of element

animal = ["horse","eagle","elephant","monkey"]
print(animal)
print(animal.index("horse"))

# insert element in specific position 

animal.insert(1,"chipmunks")
print(animal)

# pop popout element from list by index number

animal.pop(0)
print(animal)

# reverse use to reverse the order of function

animal.reverse()
print(animal)

# sort use for sort elements 

"""will back here after function""" 