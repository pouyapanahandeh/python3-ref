# dictionary is same as struct in c++

thisDict = {
	"apple" : "red",
	"banana" : "yellow",
	"mandarin" : "orange"
}

print(thisDict)

# change the value of element of dictionary

thisDict["banana"] = "green"
print(thisDict)

# dict() constructor to make a dictionary:

dictionary = dict(monkey="brown",chipmunk="orange",elephant="blue")
print(dictionary)

# adding an item to the dictionary

thisDict["kalagh"]= "black";
print(thisDict)

# removing an item from dictionary

newDic = dict(nameOne="pooya",nameTwo="Mahdi",nameThree="Ehsan")
del(newDic["nameOne"])
print(newDic)

# print the length of dictionary

print(len(thisDict))