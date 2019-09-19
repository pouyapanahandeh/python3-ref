# write program to remove the duplicates in a list.

numbers = [2,4,6,2,4,5,7,6,7,8,9,8,9]
uniques = []
for index in numbers:
	if index not in uniques:
		uniques.append(index)
		
print(uniques)