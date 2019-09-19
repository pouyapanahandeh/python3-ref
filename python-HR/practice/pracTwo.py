# getting input from user

user_name = input('please enter your name: ')
print(user_name)


# age calculator

birth_year = input('please enter your birth year: ')
age = 2019 - int(birth_year)
print(age)
# to get the type of value
print(type(age))

# long string

email = ''' Dear Python Learner

Thanks for using this repo to learn python. '''

print(email)

# check the type of EMAIL

print(type(email))

# indexing string

str_one = 'Hey, this is the first string that we use for indexing'
print(str_one[0])

# print the last element of the string

print(str_one[-1])

# print specific part of the array by indexing

# start printing from the index 0

print(str_one[0:])

# print the string from index 2

print(str_one[2:])

# print the string in special boundaris

print(str_one[0:10]) # index number 10 is not included

last_name = input('Please enter the your lastname: ')

# using the variable directly inside the string

message = f'{user_name}  {last_name} is a beginner in python'
print(message)

# nothing special, just for using special character

message_two = f'{user_name} [{last_name}] is a beginner in python'
print(message_two)

# get the length of the string

str_length = len(message_two)
print(str_length)

# print the message in uppercase

str_upper = message_two.upper()
print(str_upper)

# print in lower case

str_lower = message_two.lower()
print(str_lower)

# finding the index of element in first appearance only

print(message_two.find('p'))

# replace word in the string

print(message_two.replace('beginner', 'Expert'))

# now we are going to check if specific element exist in string or not, the result will be true or false

print('beginner' in message_two) # the result will be true, it will check the orginal string
print('hey' in message_two) # the result will be false

print(10 / 3)   # the result here will be float
print(10 // 3)  # the result here will be integer


z = 2 + 10 ** 2
print(z)
