# we call it module in python, it's like import class from another package into the current class

import subtwelve

subtwelve.greeting("pooya")

# in prv example module(subtwelve.py) contain func but it can be include dictionary,array and etc
# we are going to build dictionary in subtwelve and use it here

moduleObject = subtwelve.dictionary["age"]
print(moduleObject)
