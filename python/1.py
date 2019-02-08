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
