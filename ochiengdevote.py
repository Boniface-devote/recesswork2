#Running Python Scripts
print("I love Python and Data Science")

#VARIABLES
name= "ochieng devote"
age= 23


print("I am "+ name+" and I am "+ str(age)+" years old.")

language= "Python"
print("I love "+language+("."))

'''
Multiline commment
recess is fun
'''
#PEP8: Python script guidelines

#DATA STRUCTURES
'''
Sequence types
List enclosed with square brackets [] represented in order collections
Tuples Enclosed in Parentheses () range often used for iterations
Mapping types
Dictionary is enclosed in is enclosed with with curly braces{} containing key-value pairs
'''
#List
Cars=['Mercedes ', "Volkswagen", 'Kia', "Toyota"]
print(Cars)   #["Mercedes", "Volkswagen", "Kia", "Toyota"]
print(type(Cars)) #<class 'list'>

#Tuple
Names=("Devote", "Boniface", 'Morgan')
print(Names)
print(Names[0])

print(type(Names))

Name= "Jack"
New_Tuple= Names +(Name,) #Concatenation of Tuples
print(New_Tuple)

#Dictionary
Dictionary={"First": 6, "Second": 3, "Third":5, "Fourth":2}
print(Dictionary)
print(Dictionary["Fourth"])

'''
Set Types
{Apple, Mango, Banana} Unordered Collection type

None Types: None represents Absence of a value
'''
gender= True
print(gender)
