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

class Person: # instead self we can write what ever we want but it has to be first
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def myfunc(self):
		print("Hello my name is " + self.name)

p1 = Person("pooya", 25)
p1.myfunc()

print(p1.age)

# thats how we can delete the element

#del p1.age
#print(p1.age)

# we can remove object like below

#del p1
