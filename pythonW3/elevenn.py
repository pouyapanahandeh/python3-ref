# classes in python

class Employee:
	
	x = 5

# empOne is object for class Eployee ==> in Java ==> NameOfClass object = NameOfClass();
	
empOne = Employee()
print(empOne.x)

# the __init__() function which is simillar to the Constructor in java

class Honda:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
honda = Honda("pooya", 25)

print(honda.name)
print(honda.age)

# class with function 

class Mazda:
	def __init__(self, name, age, email):
		self.name = name 
		self.age = age
		self.email = name+"@company.com"

def user:
	code