# getting input from user and pars it to the integer

your_weight = input("Enter your Weight in kg: ")
print(type(your_weight))

# to parse value of variable, we have to put it in seperate line or put it equal new variable

int_weight_parser = int(your_weight)
print(type(int_weight_parser))

# formatted String 

first_name = "pooya"
last_name = "panahandeh"

message = f'mr. {first_name} {last_name}, welcome to the python world.'
print(message)
# print the lenght of the string
print(len(message))
# find special element in string
print(message.find('p'))
# replace string with another one 
print(message.replace('python', 'your python'))
# boolean string function to check our string for specific value, the result will be true or false.
print('python' in message) # the result will be true.
