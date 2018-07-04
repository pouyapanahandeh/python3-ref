# function in python define by typing def

def firstFunc():
	print("error 404")
	
firstFunc()

# function for passing value

def secondFunc(fname):
	print(fname + " refrence")
	
secondFunc("pooya")
secondFunc("mahdi")

# function with default value

def my_function(country = "Norway"):
	print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# function with return

def mathFunc(x):
	return x * 5
print(mathFunc(2))
print(mathFunc(4))
print(mathFunc(6))

# lambda function is anonymous function that do not need any pre def

anonFunc = lambda i: i*2
print(anonFunc(4))

