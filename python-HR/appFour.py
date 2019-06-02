# if statement 

# after if we need indent to make our if executeable, the first print shown when the condition is true
# if second print has no indent, then python knows it as else statement, but if it has indent it count s if statement
is_hot = False
if is_hot:
	print("enjoy your day")
print("drink lots of water")

# if else statement

drink_hot = True

if drink_hot:
	print("be careful, hot drink can be dangerous.")
else:
	print("Do not drink cola too much")
	
# if, else, elif

is_rainy = True
is_snowy = True
is_sunny = True

if is_rainy:
	print("Do not forget your umbrella!!!")
elif is_snowy:
	print("wear some warm clothes")
elif is_sunny:
	print("it's a fucking lovey day, have fun")
else:
	print("Have no Idea about the weather, probably you live in london or Vitenam")

	