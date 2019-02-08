# python identifiers

# we have a way to check if an identifier is valid or not

import keyword

print(keyword.iskeyword("pooya"))

print(keyword.iskeyword("for"))


# in above example we saw how we can check if one word is one of the keywords or not, by this method we can make sure that we select the correct identifier


# directly checking the identifier

print("pooya".isidentifier())
print("name".isidentifier())
print("this".isidentifier())

# variable in python

print("\n -------------------------- \n")

print(keyword.iskeyword("var"))

var = 10

print(var)

print(type(var))


var_two = "name should be string"

print(type(var_two))
