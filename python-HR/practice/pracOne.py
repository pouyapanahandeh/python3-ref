# write program to remove the duplicates in a list.

numbers = [2,4,6,2,4,5,7,6,7,8,9,8,9]
uniques = []

for number in numbers:
	if number not in uniques:
		uniques.append(number)
		
print(uniques)
