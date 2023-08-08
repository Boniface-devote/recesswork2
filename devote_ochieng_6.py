#Regular expressions
"""

Matching and searching
NB:A RegEx /regular expression is a sequence of characters that forms a search pattern.
regex.re.match() ,re.search(),re.findall()

findall	- Returns a list containing all matches
search -Returns a Match object if there is a match anywhere in the string
split -	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string
"""
#Example 1- demonstrating RegEx |match First Word, match all numbers,match group word
import re
text = "i am called devote boniface"

#Match first word
match = re.search(r"\b\w+\b", text)

if match :
    print(match.group())

#Match all numbers
match = re.search(r"\d+", text)

if match :
    print(match.group())

matches = re.findall(r"\d+", text)
print(matches)
#Example 2 - validating email format or email address
def validated_email(email):
    pattern = r'^[\w\. -]+ @[\w\. -]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False
    
#Example usage
Email1 = "ochiengdevote@gmail.com"
Email2 = "ochiengdevote@outlook.com"

print(validated_email(Email1))
print(validated_email(Email2))


#Generators and Iterators
#An iterator is an object that can be iterated upon meaning you can traverse through all values
#An iterator is an object that contains a countable number of values
#i.e __iter__() and __next__()
tuple = ("gun", "ak47", "uzigun")
guns = iter(tuple)

print(next(guns))
print(next(guns))
print(next(guns))

#Generators
#Agenerator function uses the yield keyword to generate a value

#Example 3
def squares():
    for i in range(1, 10):
        yield i ** 2

#create an iterator object 

Iterator = squares()

for i in range(5):
    print(next(Iterator))

#decorators in python
def my_decorator(func):
    def inner():
        print("This is my decorator")
        func()
        return inner
    
@my_decorator
def outer_decorator():
    print("This is my function")

outer_decorator()



