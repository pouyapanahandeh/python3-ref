# getting input from user

name = input('what is your name? ')
print('Hi ' + name + ' welcome to the python3 world')

# calculating the age of user

birth_year = input('when is your birthday? ' )
age = 2019 - int(birth_year) # here we need to use int() to parse birth_year from string to integer
print(type(birth_year)) # type of birth_year, now you can undrestand why we need to parse it from strong to integer
print(type(age))
print(age)

