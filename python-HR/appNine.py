# operation on list

numbers = [1,2,3,4,5,6,7,8]
numbers.append(9)	 # append use to add element to the list
print(numbers)

numbers.insert(0, 0) # by insert we can add element in specific index we want
print(numbers)

numbers.pop()
print(numbers) # pop means delete the last number of the list


numbers.remove(8) # by remove method we can delete element from list[ it's not indexing ]
print(numbers)

print(numbers.index(3)) # Shows the index of number 3

