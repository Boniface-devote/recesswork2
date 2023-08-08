# #syntax error
# x = 10000

# if(x > 2999)
# print("You are eligible to purchase Dsa Self Paced")
# #exception

# age= 21
# average = age / 0
# print(average)

#other Exception error typeof error
# name = "devote"
# age =21
# desc = name + age

# #we use the try and except to handle exceptions and errors
# name = "devote"
# age =21
# desc = name + age
# try:
#   desc = name + age
# except TypeError:
#     print("Error: cannot add an int and a str")


    # Program to handle multiple errors with one 
def fun(a):
    if a < 4:
 
        # throws ZeroDivisionError for a = 3
        b = a/(a-3)
 
    # throws NameError if a >= 4
    print("Value of b = ", b)
     
try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")

    
# using else clause with try-except

# Program to depict else clause with try-except 
# else is only executed if thr try doesnt show an error

def mak(a , b):
	try:
		c = a+b
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)

mak(2.0, 3.0)

#using finally key word in the try and except
try:
    age = 10 / 0
    print(age)
 
# handles zerodivision exception
except Exception:
    print("Can't divide by zero")
 
finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')

    #############################file handling in python###########################################
    # use the open() but at the time of opening, we have to specify the mode
    #opening a file 
    #example 1
   
file = open('devote.txt', 'r')

# print every line one by one in the file
for line in file:
	print (line)
file.close()
 #example 2
 #using the read function
file = open("devote.txt", "r")
print (file.read())
file.close()

 #example 3
# Read Only some Parts of the File
f = open("devote.txt", "r")
print(f.read(5))
f.close()

#writing in a File using the write() Function
#example 1
# Python code to create a file
#using the "w" to put the pointer at the beginning
file = open('devote2.txt','w')
file.write("I am write in a file ")
file.write("I am allowed to continue writing")
file.close()


#example 2
#using the "a" to put the pointer at the end and append
file = open("devote2.txt", "a")
file.write("Now the file has more content!")
file.close()

#open and read the file after the appending:
file = open("devote2.txt", "r")
print(file.read())

#Deleting a File
import os
if os.path.exists("devote.txt"):
  os.remove("devote.txt")
else:
  print("The file does not exist")

#Deleting a Folder
import os
if os.path.exists("my folder"):
 os.rmdir("myfolder")
else:
  print("The folder does not exist")