# print index of string 

str_one = 'python land is a place for everyone not just beginner'
#		   012345
print(str_one[0]) # print the first letter of our string str-one
print(str_one[-1]) # pring the last letter of our string str_one

# print special range of string

print(str_one[0:4]) # reult will be from index 0 till index 4, index 4 is not included, only 4 index is included.

print(str_one[0:]) # start from index 0 till end and will print whole string

print(str_one[1:]) # same as above just start from index 1

# f string in python, good for concat multiple string

first_name = 'pooya'
last_name = 'panahandeh'
message = f'{first_name} [{last_name}] is a beginner programmer.' # f string is a method to manipulate the string

print(message)

# get the number of element of string

course = 'python is awsome'
print(len(course))

# change string to upper case 

print(course.upper())

# change letter to lower case 

course_two = "NODEJS PROGRAMMING"

print(course_two.lower())

# finding specific element in string

str_two = 'we are one of the best group of people'
print(str_two.find('g'))

# replace two words in string

print(str_two.replace('best', 'fucking best'))

print('one' in str_two) # checking if there the string we mentioned is exist in str_two or not, result will be true or false
 	 
# division and remainder operation in python

print(10 / 3) # result will be float
print(10 // 3) # result will be integer

# multiplication
print(10 * 2)	# multiplication of two number
print(10 ** 2)	# power of number

# assign variable to number and manipulate.
x = 10 
# x = x + 4 short way in next line
x += 4
print(x)

# first multiplication then addition

z = 10 + 2 ** 2
print(z)
