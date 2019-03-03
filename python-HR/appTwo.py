# print index of string 

str_one = 'python land is a place for everyone not just beginner'
#		   012345
print(str_one[0]) # print the first letter of our string str-one
print(str_one[-1]) # pring the last letter of our string str_one

# print special range of string

print(str_one[0:4]) # reult will be from index 0 till index 4, index 4 is not included

print(str_one[0:]) # start from index 0 till end and will print whole string

print(str_one[1:]) # same as above just start from index 1

# f string in python, good for concat multiple string

first_name = 'pooya'
last_name = 'panahandeh'
message = f'{first_name} [{last_name}] is a beginner programmer.' # f string is a method to manipulate the string

print(message)

