# set , set can not contain duplicates, sets are unordered

thisset = {"apple", "banana", "cherry"}
print(thisset)

# set() Constructor

thisset = set(("apple", "banana", "cherry"))
print(thisset) 

# add() method to add an item:

thisset = set(("apple", "banana", "cherry"))
thisset.add("damson")
print(thisset) 

# remove() method to remove an item

thisset = set(("apple", "banana", "cherry"))
thisset.remove("banana")
print(thisset)

# len() method to return the number of items:

thisset = set(("apple", "banana", "cherry"))
print(len(thisset))