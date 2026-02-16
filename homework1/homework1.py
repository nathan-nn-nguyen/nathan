#File: homework1.py
# ------------ 3.1 Variables and Data Types --------------

a = 10
b = 1.5
c = 3j
d = "hello"
e = [1, 2, 3]
f = {"name": "Ellen", "favorite fruit": "strawwberry"}
g = (1, 2)
h = ["apple", "banana", "strawberry"]
i = True
j = None
k = [True, "blue", 12]
l = str(14)
m = 1e4

n = {'apple', 'banana'}
#1. There was 9 types of data, 
#2.  and they were: int, float, complex, str, list, doct, tuple, boolean, NoneType
#3. The variables with the same data type were, b and m(float), d and l (str), e, h and k (list).
#4. l is a string because of the function(str) which converts the number 14 into the text "14"
#5. variable n is a set, which carries sets of data but not in a particular order and without duplicates.

print(a)
print(type(a))
#int- a number with no decimals

print(b)
print(type(b))
#float- a number with decimals

print(c)
print(type(c))
#complex- complex numbers aka imaginary numbers

print(d)
print(type(d))
#str- text types that can't be changed

print(e)
print(type(e))
#list- variable that can store mutiple items that is ordered and changeable 

print(f)
print(type(f))
#dict- stores data in key-value pairs

print(g)
print(type(g))
#tuple- unchangeable datat type that stores data in a specific order and can have duplicate values

print(h)
print(type(h))
#list-  variable that can store mutiple items that is ordered and changeable

print(i)
print(type(i))
#bool- boolean type

print(j)
print(type(j))
#NoneType- none type

print(k)
print(type(k))
#list- variable that can store mutiple items that is ordered and changeable

print(l)
print(type(l))
#str- text types that can't be changed

print(m)
print(type(m))
#float-a number with decimals


#my type
print(n)
print(type(n))
#set- used to store mutiple items in a variable but not in a particular order and cannot duplicate


#------------------- 3.2 Booleans -------

print(10 > 9)
#true, it is factually true

print(10 == 9)
#false, it is factually false

print(10 <= 9)
#false, it is factually false

print(bool("abc"))
#true because it has a value inside

print(bool(123))
#true because it has a value inside

print(bool(["apple", "cherry", "banana"]))
#true because it has values inside

print(bool(True))
#true because true is true

print(bool(False))
#false because false is false

print(bool(0))
#false because 0 has no values

print(bool(""))
#false because the string has no value and so returns as false

print(bool(" "))
#True, the "" aren't empty because they have a space and so return as true

print(bool(()))
#false because the tuple has no value

print(bool([]))
#false because the list has no value

print(bool({}))
#false because the set has no value

print(bool(True and False))
#false, the value can't be true and false

print(bool(True and True))
#true, the true value is true

print(bool(False and False))
#false, the false value is false

print(bool(True or False))
#True, the value can be true or false

print(bool(True or True))
#True, the answer can be true or true and so returns true

print(bool(False or False))
#false, the answer can be false or false so its false

print(bool(not(False)))
#true, not false is true

print(bool(not(True)))
#false, not true is false

#1. non boolean pieces of data converted into booleans with bool() with actual content instead of empty brackets returned true, but empty ones returned false
#2. bool(0) = False
#3. print(bool(a == a)) because the value of a does equal itself
#4. print(bool(a == b)) because a does not necessarily equal b


#-------------------- 3.3 Operators--------------------

#3.3.1 Arithmetic Operators
print(10 + 5) 
#15, performs addition
print(10 - 5)
#5, performs subtraction
print(2 * 4)
#8, performs multiplication
print(6 / 3)
#2, performs division
print(5 % 2)
#1, takes the remainder
print(3 ** 2)
#9, 3 to the exponent of 2
print(15 // 2)
#7, performs floor division which is the amount of times it can be divided aka division without remainder


#3.3.2 Comparison Operators

print(5 == 2)
#false, 5 does not equal 2
print(10 != 10)
#false, not equal to, 10 is not, not equal to 10
print(2 < 5)
#true, 2 is less than 5
print(12 > 5)
#true, 12 is greater than 5
print(5 <= 6)
#true, 5 is not greater or equal than 6
print(1 >= 10)
#false, 1 is not greater or equal than 10


#3.3.3 Assignment Operators

x = 5
print(x)
#5
x += 5
print(x)
#10
x -= 4
print(x)
#6
x *= 3
print(x)
#18

#3.3.4 Logical Operators
#1. "and" expresses that both variables in the function have to be True or present
    # a = 1
    # b = 1
    # print(bool(a and b == 1))  
#2. "or" expresses that one of the variables in the function has to be present to return True
    # a = 1
    # b = 2
    # print(bool(a or b == 1))  
#3. "not" expresses that the variables cannot equal the value specified
    # a = False
    # print(bool(not a))  

# More questions
#1. / does real divison, while // returns division as an integer by only returning how many times the number can be completeley divided without decimal or remainder
#2 % gives the remainder of a division problem, while // returns an integer of a division problem without remainder or decimal
#3 I would use % 
    # for ex. print(20 % 3)
    # which prints out 2
#4 They change the numeric value of the parameter using the value of the action specifed so x-=4 would subtract 4 from x's total.



#----------------------------------3.4 Strings------------------------------

my_string = "hello"
print(my_string) #prints the whole string
print(my_string[0]) #prints the first letter of the string
print(my_string[1]) #prints the second letter of the string
print(my_string[2]) #prints the third letter of the string
print(my_string[3]) #prints the fourth letter of the string
print(my_string[4]) #prints the fifth letter of the string
print(my_string[-1]) #prints the first letter of the string in reverse order
print(my_string[1:3]) #prints the string starting with the second and ending with the third letters of the string
print(my_string[0:5:2]) #prints the string from the first, ending with the sixth and going by 2s
print(len(my_string)) #prints length of string
print(my_string + " goodbye") #adds the word goodbye to the string
print(my_string * 7) #repeats the string 7 times

#3.4.1
#1. slicing is manipulating the data to return the information at and from a specific interval. I sliced in #8 and #9
#2
name = "Oski"
print("Hello, my name is", name) #it suplements the printed string with the parameter name at the end of the sentence
#3
name = "Oski"
print(f"Hello, my name is {name}") #it suplements the printed string with the parameter name at the end of the sentence using an f string to imbed the parameter into the string
#4 the f string allows the parameter name to be inside the "" of the string for easier formatting



#---------------------------------------------3.5 Terminal Commands------------------------------------

#cd: changes directories and is used to go from one folder to another
#       cd folder1
#ls: lists out the files and directories in the system/folder
#       ls 
#ls -a: lists out hidden files additionally
#       ls -a
#mkdir: make directory, makes a new folder within the current folder
#       mkdir folder 2        
#cat: concatenates, allows you to view contents of files in the terminal without opening the text editor
#       cat python.py
#pwd: Print working directory, shows the path of where you are in the current directory 
#       pwd
#cd ..: change parent directory: changes the folder to the one above the one you are currently in. 
#       cd ..
#cd .: change curent directory: has to do with the current directory, changes the folder to the one currently in.
#        cd .
#cd ~: change home directory: changes folder from current location to the home directory
#       cd ~
#cp: copy: copies the contents of one file into another or duplicates files between folders.
#       cp file1 file2
#mv: move: changes the name of a file or folder or moves it.
#       mv folder1 folder2       
#rm: remove: permanently deletes files from the system
#       rm file1
#clear: clear: clears the terminal screen of past commands 
#       clear    
#grep: searches for specific words or patterns inside text files and prints them on screen
#       grep "hello, world" file.txt


#Questions
#1. rmdir: remove directory: deletes empty directories
#   locate: locate: finds specific file names in the dataset examined
#   echo: echo: prints arguments as lines so that they can be viewed
#2. ls prints only known and visible folders while ls -a prints everything plus hidden folders
#3. Hidden files are files/directories which are named with a . in front and aren't shown in directies typically to prevent accidental tampering
#4. -i is a flag and asks for conformation. -i can be used with after commands to ask for conformation like rm -i asks for conformation before deleting files
#   -f is a flag that forces a command to work even with barriers. cp -f can be used to force copy a file to a new location forcefully
#   -n helps display content with line numbers of files. In the cat -n function, it displays the results of the file conents from the text editor into the terminal but adds line numbers.     