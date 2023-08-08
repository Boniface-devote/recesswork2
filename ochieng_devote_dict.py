devote_dict = {'name': "devote", 'age': 21, 'sex': "male"}

# Get a list of all values using values() method
list_devote = list(devote_dict.values())

print(list_devote)

""" Using 'in' keyword for checking"""
if 'name' in devote_dict:
    print("name is present in the dictionary.")


""" Using 'get' keyword for checking"""
if devote_dict.get('age') is not None:
    print("your age is exists in the dictionary",devote_dict["age"])
   

# Changing the value of an existing key
devote_dict['name'] = "ochieng"

print(devote_dict)


# Updating multiple items or add new items
devote_dict.update({'home': "seeta", 'class': 8})

print(devote_dict)

# Adding a new item to the dictionary
devote_dict['height'] = 4

print(devote_dict)

# Removing an item using del
del devote_dict['home']

print(devote_dict)


# Removing an item woth the  pop()
value_to_remove = devote_dict.pop('class')

print(devote_dict)
print("Value removed:", value_to_remove)




# Looping the devote dictionary
for  key,value in devote_dict.items():
    print('the key is ', key, 'and the value is', value)

#the second assigment for the strings and string functioms

#STRINGS
#declaration of a string in python
my_name = "devote "
print(my_name)

#string on a single line
girl= "dora"

'''using the len() method for length
of a string
'''
print (len(girl))

'''using a for loop in a string 
an example 
'''


for name in girl:
    print(name)
    

greeting= "Hello, World! from devote"

# Slicing a string
slice_name = greeting[19:]  # Slice from index 19 to end
slice1 = greeting[0:5]  # Slice from index 0 to 4 
slice2 = greeting[7:]   # Slice from index 7 to the end
slice3 = greeting[7:12]   # Slice from the index 7 to index 11
slice4 = greeting[::2]  # Slice with a step size of 2

# Print the slices
print("Slice name:", slice_name)
print("Slice 1:", slice1)
print("Slice 2:", slice2)
print("Slice 3:", slice3)

#using booleans evaluate to true or false
#  example 1


size= 39
if size < 40:
     print("false")   
else:
    print("true")
    
#  example 2
age= 21
adult=18
print(age >adult )
print( 10 == 9)

#  example 3
x="hello"

print(x=="hello")
    
    


