#The key function for working with files in Python is the open() function.
#
#The open() function takes two parameters; filename, and mode.
#
#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#
#"x" - Create - Creates the specified file, returns an error if the file exists
#
#In addition you can specify if the file should be handled as binary or text mode
#
#"t" - Text - Default value. Text mode
#
#"b" - Binary - Binary mode (e.g. images)

f = open("file.txt", "r")

# shows everything from the file you built

#   print(f.read())

# by adding number in read() we can tell programm print till character number become same as the value we gave to read()

#   print(f.read(8))

# to read only one line

f = open("file.txt", "r")
print(f.readline()) 

# to add text to our file

f = open("file.txt", "a")
f.write("Now the file has one more line!") 

f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")

# https://www.w3schools.com/python/python_file_remove.asp



