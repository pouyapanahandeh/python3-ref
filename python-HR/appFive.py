# logical operation

is_hot = True
is_tea = True
is_cofee = True
if is_hot and is_tea:
	print("Have fun with your tea")
elif is_cofee or is_tea:
	print("drink warm")
else:
	print("wtf!!! you drink cofee")
	
# use > < =

Tempture = 30

if Tempture >= 30:
	print("best weather ever, have fun")
else:
	print("ww with this weather")

# use logical operation in real world example
name = 'pooya'

if len(name) > 4:
	print("your name is long")
else:
	print("short name is better than short ####")
	
# if statement operation on user input

weight = input("please enter your weight: ")
unit = input("please enter your (L) or (K): ")

if unit.upper() == 'L':
	print(float(weight) * 0.45)
else:
	print(float(weight) / 0.45)
	
