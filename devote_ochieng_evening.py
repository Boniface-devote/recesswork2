#1. Create a list with 5 items (names of people) and write a python program to output the 2nd
#item.

Namez = ["devote" , "trevor", "ian", "vanier","morgan"]

#2. Write a python program to change the value of the first item to a new value

Namez[0] = "rashid"

#3. Write a python program to add a sixth item to the list

Namez.append("elton")

#4. Write a python program to add “Bathel” as the 3rd item in your list

Namez.insert(2, "Bathel")
print(Namez)

#5. Write a python program to remove the 4th item from the list

Namez.pop(4)

print(Namez)

#6. Use negative indexing to print the last item in your list

print(Namez[-1])

#7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items
next_list = [21,23,3,4,5,3,2]

print("3rd", next_list[2])
print("4th", next_list[3])
print("5th", next_list[4])

#8. Write a list of countries and make a copy of it
countries_list = ["rwanda", "usa", "sudan", "uganda"]

countries_copy = list(countries_list)

print(countries_list is countries_copy)

#9. Write a python program to loop through the list of countries

for country in countries_list:
    print(country)

#10. Write a list of animal names and sort them in both descending and ascending order
Animals = ["cow", "donkey", "duck", "cow", "zebra"]
Animals.sort()
print("ascending order of animals ", Animals)

Animals.sort(reverse=True)
print("descending order of animals", Animals)

#11. Using the list above, write a python program to output only animal names with the letter 
#‘a’ in them

for animal in Animals:
    index = animal.find("a")
    if(index != -1):
        print(animal)

#12. Write two lists, one containing your first names and the other your second names. Join 
#the two lists 

fname = ["devote"]
sname = ["ochieng"]

name = fname + sname
print(name)


# Exercise2 (Tuples)

"""
1. Consider the tuple below;
x = (“samsung”, “iphone”, “tecno”, “redmi”)
Write a python program to output your favorite phone brand.
"""

x = ("samsung", "iphone", "tecno", "redmi")
print(x[0])

#2. Use negative indexing to print the 2nd last item in your tuple.

print(x[-2])

#3. Using the phones list above, write a python program to update “iphone” to “itel”
x = list(x)
x[1] = "itel"
print(x)

#4. Write a python program to add “Huawei” to your tuple.
x = tuple(x)

x = tuple(list(x) + ["Huawei"])
print(x)

#5. Write a python program to loop through the tuple above.
for my_phone in x:
    print(my_phone)

#6. Write a python program to remove/delete the first item in your tuple.
x = x[1:]

print(x)

#Using the tuple() constructor, create a tuple of the cities in Uganda.
uganda_cities = ("soroti", "masaka", "mukono","kampala")

#8. Write a python program to unpack your tuple.
for city in uganda_cities:
    print(city)

#9. Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
for i in range(1, len(uganda_cities)):
    print(uganda_cities[i])

print("2nd", uganda_cities[1])
print("3rd", uganda_cities[2])
print("4th", uganda_cities[3])

"""
10. Write two tuples, one containing your first names and the other your second names. Join 
the two tuples
"""

fname = ("devote")
sname = ("ochieng")

my_namz = fname + sname
print(my_namz)

#11. Create a tuple of colors and multiply it by 3
colors = ("red", "blue", "green","white")

print(colors * 3)

"""
12. Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
"""


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

print(thistuple.count(8))


#Exercise3 (Sets)

#1. Use the set() constructor to create a set of 3 of your favorite beverages

my_beverage = set(["yaket", "nile special", "bell"])

print(my_beverage)

#2. Use the correct method to add 2 more items to the beverages set.

my_beverage.add("kumbucha")

my_beverage.add("pepsi")

"""
3. Given the set below;
mySet = {“oven”, “kettle”, “microwave”, “refrigerator”}
Check if microwave is present in the set.
"""
mySet = {"oven", "kettle", "microwave", "refrigerator"}

print(mySet.intersection({"microwave"}))

#4. Write a python program to remove “kettle” from the set above

mySet.remove("kettle")

print(mySet)

#5. Write a python program to loop through the set above
for things in mySet:
    print(things)

#6. Write a set of 4 items and a list of two items. Write a python program to add elements in 
#the list to elements in the set.

new_set = {"yoo", "man", "gwe" , "gd"}
new_list = ["wewe", "ji"]

new_set = new_set.union(new_list)

print(new_set)

#Write two sets, one containing your ages and the other your first names. Join the two 
#sets

ages = {22,24}
my_names = {"devote", "ochieng"}

unite = ages.union(my_names)

print(unite)

# Exercise4 strings

#1. Declare two variables, an integer and a string and use the correct method to concatenate 
#the two variable

x = 22
y = "this is my age "

z = y + str(x)

print(z)

"""
2. Consider the example below;
txt = “ Hello, Uganda! ”
Output the string without spaces at the beginning, in the middle and at the end.
"""

txt = " Hello, Uganda! "

non_spaced = "".join(txt.strip().split(" "))

print(non_spaced)

#3. Write a python program to convert the value of ‘txt’ to uppercase.

print("txt".upper())

#4. Write a python program to replace character ‘U’ with ‘V’ in the string above
replaced = txt.replace("U", "V")

print(replaced)

"""
5. Using the code below, write a python program to return a range of characters in the 2nd
, 3rd and 4th position.
y = “I am proudly Ugandan”
"""


message = "I am proudly Ugandan"
print("2nd position",message [1])
print("3rd position", message[2])
print("4th position", message[3])

"""
6. The piece of code below will give an error when output;
x = “All “Data Scientists” are cool!” 
Write a python program to correct it
"""

x = "All \"Data Scientists\" are cool!"
print(x) 


#    Exercise5 Dictionaries

"""
1. With reference to the dictionary below, write a python program to print the value of the 
shoe size. 
Add this dictionary to your .py file
Shoes = {
“brand” : “Nick”,
“color” : “black”,
“size” : 40
}
"""

Shoes = {
"brand" : "Nick",
"color" : "black",
"size" : 40
}

print(Shoes["size"])

#2. Write a python program to change the value “Nick” to “Adidas"
Shoes["brand"] = "Adidas"
print(Shoes)

#3. Write a python program to add a key/value pair "type”: "sneakers" to the dictionary

Shoes["type"] = "sneakers"
print(Shoes)

#4. Write a python program to return a list of all the keys in the dictionary above.

print(Shoes.keys())

#5. Write a python program to return a list of all the values in the dictionary above.

print(Shoes.values())

#6. Check if the key “size” exists in the dictionary above

if "size" in Shoes:
    print(True)
else:
    print(False)

#. Write a python program to loop through the dictionary above.
for values in Shoes.items():
    print(values)

#8. Write a python program to remove “color” from the dictionary

Shoes.pop("color")

print(Shoes)

#9. Write a python program to empty the dictionary above

Shoes.clear()

print(Shoes)

#10. Write a dictionary of your choice and make a copy of it

dict1 = {
    "fname":"devote",
    "sname":"ochieng",
    "lname":"boniface"
}

dict2 = dict1.copy()

print(dict1 is dict2)

#11. Write a python program to show nested dictionaries

net_dict = {
    "dict" : {
        5: "five",
        2 : "two"
    },

    "inn" : {
        "in" : {
            "age" : 23
        }
    }
}

print(net_dict)