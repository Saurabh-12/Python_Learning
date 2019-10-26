'''
Tuples are an ordered sequences of items, just like lists. 
The main difference between tuples and lists is that tuples cannot be changed (immutable) 
unlike lists which can (mutable) 
'''

# 1. Initialize a Tuple
# Way 1
emptyTuple = ()

# Way 2
emptyTuple = tuple()

# 2. Assiging the value
# way 1
z = (3, 7, 4, 2)

# way 2 (tuples can also can be created without parenthesis)
z = 3, 7, 4, 2
print(z)

# 3. If you want to create a tuple containing only one value, 
# you need a trailing comma after your item.

# tuple with one value
tup1 = ('Michael',)# tuple with one value
tup2 = 'Michael', 

# This is a string, NOT a tuple.
notTuple = ('Michael')
print(tup1)
print(tup2)
print(notTuple)

# 4. Tuple slices
# Initialize a tuple
z = (3, 7, 4, 2)
# first index is inclusive (before the :) and last (after the :) is not.
print(z[0:2])
# everything up to but not including index 3
print(z[:3])

# 5. Tuples are Immutable
''' 
Tuples are immutable which means that after initializing a tuple, 
it is impossible to update individual items in a tuple
'''
z = (3, 7, 4, 2)
 # z[1] = "fish" # Error :- TypeError: 'tuple' object does not support item assignment
 
# Even though tuples are immutable, it is possible to take portions of existing tuples to create new tuples 
# Initialize tuple
tup1 = ('Python', 'SQL')
# Initialize another Tuple
tup2 = ('R',)
# Create new tuple based on existing tuples
new_tuple = tup1 + tup2;
print(new_tuple)

# 6. Tuple Method
     # 6. 1. index method
# Initialize a tuple
animals = ('lama', 'sheep', 'lama', 48)
print(animals.index('lama')) # O/P = 0, Gives index of element 

# 6. 2 count method: the count method returns the number of times a value occurs in a tuple.
print(animals.count('lama')) # o/p = 2 

# 6.3  Iterate through a Tuple
for item in animals:
   print(item)

# 6.4. Tuple Unpackin
x, y = (7, 10);
print("Value of x is {}, the value of y is {}.".format(x, y)) 

# 6.5 . Enumerate
'''
The enumerate function returns a tuple containing a count for every iteration (from start which defaults to 0)
'''
friends = ('Steve', 'Rachel', 'Michael', 'Monica')
for index, friend in enumerate(friends):
    print(index,friend)
