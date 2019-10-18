# So everything in Python is an object,
#  and every object has a unique ID and has a type associated with it
#  — but what exactly is an object?
''' An object is a type of variable that contains values and functions all grouped under one roof. 
This organization of values and functions are defined by a class '''
class SimpleClass :
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# An object 'example' is instantiated based on class 'sampleclass'       
example = SimpleClass()
''' Once an object is instantiated based on its class definition, what can we do with it? 
....We can make changes to the object, but only if it is mutable'''

# Mutable objects
# In context of objects, mutable objects are objects that can change in place without having their IDs and type change
list_a = [1,2,3,4]
print(id(list_a))
# ID of list_a : 1926210840776
list_a.append(5)
print(list_a)
# [1, 2, 3, 4, 5]
print(id(list_a))
# Id of list_a : 1926210840776,  Still same
''' other types of mutable object :-  bytearray, set, and dict '''

# Immutable objects
''' Immutable objects are objects that cannot change their contents. They are unchanging — aka immutable. 
Some examples of immutable objects are int, float, str, tuples, and frozenset.'''

str_1 = "Hi"
print(" str_1 "+str_1)
print(id(str_1))

# Change String 1 now by adding a character 
str_1 +='t'
print(" str_1 "+str_1)
print(id(str_1))


# put the str_1 content : Since Str is Immutable, str_2 point the Str_1 reference 
str_2 = "Hi"
print(" str_2 "+str_2)
print(id(str_2))

''' Let’s try using the value equality operator and the object ID comparison operator'''
# to compare Mutable and Immutable Object

print("----"*5)
# Mutable Object
list_1 = [1,2,3]
list_2 = [1,2,3]
print(list_1 == list_2)
# O/P = True
print(list_1 is list_2)
# O/P = False
print(id(list_1) == id(list_2))
# O/P = False

print("----"*5)
#Immutable Object
a = "Hi"
b = "Hi"
print(a == b)
# O/P : True
print(a is b)
# True
print(id(a) == id(b))
# O/P : True

''' How arguments are passed to functions'''
# Every argument in Python is passed to functions in a process called Call-by-Object
# What this means is that how the function handles the argument is entirely based on the type of object
''' For example, if we pass an integer into a function, then the function will treat the integer argument
 as “pass-by-value” because an integer is immutable'''
 # If a list was passed into a function, then the function will treat it like a “pass-by-reference” 
 # and can make changes to the contents of the list that will actually affect the caller’s list
 
 # Mutable Objects
''' 
 list
 Dictionary
 Set
 bytearray
 user defined classes
'''
# Immutable Objects
'''
int
float
decimal
complex
bool
string
tuple
range
frozenset
bytes
'''
# Thanks
#  Saurbh 
# Hapopy Coding !!!! 







