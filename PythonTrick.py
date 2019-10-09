# 1. Python way of value swaping
a,b = 5,10
print(a,b)
a,b = b,a
print(a,b)

# 2. Create a single String for the list
my_string_list = ["Python", "is", "awesome"]
print(" ".join(my_string_list))

# 3. Reverse the String using slicing
singeString = " ".join(my_string_list)
print(singeString[::-1])

# 4. Find The Most Frequent Value In A List.
number_list = [1,2,3,1,2,3,2,2,4,5,1,2]
print(max(set(number_list), key =number_list.count))

from collections import Counter
cnt = Counter(number_list)
print(cnt.most_common(3))

#5. Checking two word Anagrams Listen = Silent.
s1 = "listen" # tringle
s2 = "silent" # integral
print("Words are Anagrams" if Counter(s1) == Counter(s2) else "No")

# 6. Chained Comparison
b = 6
print(4<b<8)
print(1==b<20)

# 7. Chained Function call
c = True

def multiply(a, b):
    return (a*b)
def addition(a,b):
    return (a+b)
#print(multiply if c else addition)(5,2) # only works in Python 2.x

# 8. Copying List
my_list = [2,4,6,8,10]
# Shallow copy
my_copy_list = my_list
print(my_list)
my_copy_list[0] = 10
print(my_list)

# Deep copy
my_copy_list = my_copy_list[:]
my_copy_list[0] = 15
print(my_list)
print(my_copy_list)

# Copy list by Type casting 
a = [1,2,3,4,5]
print(list(a))
# copy and deep copy method Python 3
print(a.copy())

# 9. Min and Max index in List
list_check = [40,10,60,20,23,8]

def minIndex(lst):
    return min(range(len(lst)), key = lst.__getitem__)

def maxIndex(lst):
    return max(range(len(lst)), key = lst.__getitem__)

print(minIndex(list_check))
print(maxIndex(list_check))

# 10. Remove duplicates from a list
duplicate_list = [1,2,2,3,3,4,5,5,6]
# 1st way
newListwithoutDup = list(set(duplicate_list))
print(newListwithoutDup)
# 2nd Way 
from collections import OrderedDict
print(list(OrderedDict.fromkeys(duplicate_list).keys()))

# 11. Print The File Path Of Imported Modules
import os; 
import socket; 
print(os) 
print(socket) 

# 12. Use Of Enums In Python.
class MyName:
    Saurabh, Kumar, Sharma = range(3)

print(MyName.Saurabh)
print(MyName.Sharma)
print(MyName.Kumar)

# 13. Returm multiple value function
def returnMultipleValue():
    return 1,2,3,4,5
a1, b1, c1, d1, e1 = returnMultipleValue()
print("a1,b1,c1,d1,e1 = ",a1,b1,c1,d1,e1)

# 14. Check The Memory Usage Of An Object.
import sys 
x = 1
print(sys.getsizeof(x)) 

# 15.Store all values of the list new variables
my_list_value = [2,4,6]
x,y,z = my_list_value
print("x, y, z = ", x,y,z)

# 16. Combined Two list corresponding value and print 
list1 = ['a', 'b', 'c', 'd']
list2 = ['p', 'q', 'r', 's']
# print like ap,bq,cr, ds
for x,y in zip(list1,list2):
    print(x,y)
#17. Merge two dictionaries in Python 3.5+:
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(z)

#18. Measure the time elapsed to execute your code
import time
startTime = time.time()
# write your code or functions calls
for i in range(55):
    print(i)

endTime = time.time()
totalTime = endTime - startTime
print("Total time required to execute code is= ", totalTime)

# 19. Get the difference between the two Lists
list1 = ['Scott', 'Eric', 'Kelly', 'Emma', 'Smith']
list2 = ['Scott', 'Eric', 'Kelly']

set1 = set(list1)
set2 = set(list2)

list3 = list(set1.symmetric_difference(set2))
print(list3)

# 20. Find if all elements in a list are identical
list1 = [20, 20, 20, 20]
print("All element are duplicate in list1", list1.count(list1[0]) == len(list1))

list2 = [20, 20, 20, 50]
print("All element are duplicate in list2", list2.count(list2[0]) == len(list2))

# 21. Compare two unordered lists
from collections import Counter

one = [33, 22, 11, 44, 55]
two = [22, 11, 44, 55, 33]

print("is two list are equal: ", Counter(one) == Counter(two))

# 22. Check if all elements in a list are unique
def isUnique(item):
    tempSet = set()
    return not any(i in tempSet or tempSet.add(i) for i in item)

firstList = [123, 345, 456, 23, 567]
print("All elemtnts are Unique: ", isUnique(firstList))

secondList = [123, 345, 567, 23, 567]
print("All elemtnts are Unique ", isUnique(secondList))

# 23. Convert hex string, String to int
hexNumber = "0xfde"
stringNumber="34"
print("hexNumber", hexNumber, " >> ", "intNumber", int(hexNumber, 0))
print("String >> int", int(stringNumber, 0))

# 24. Format a decimal to always show 2 decimal places
number= 88.2365
print('{0:.2f}'.format(number))

# 25. Convert two lists into a dictionary
ItemId = [54, 65, 76]
names = ["Hard Disk", "Laptop", "RAM"]

itemDictionary = dict(zip(ItemId, names))
print(itemDictionary)

# 26. convert a string to title case.
my_string = "my name is Saurabh Sharma"
# using the title() function of string class
new_string = my_string.title()
print(new_string)

# 27. find all the unique elements in a strin
my_string = "aavvccccddddeee"

# converting the string to a set
temp_set = set(my_string)

# stitching set into a string using join
new_string = ''.join(temp_set)
print(new_string)

# 28. creating lists based on other lists.
original_list = [1,2,3,4]
new_list = [2*x for x in original_list]
print(new_list)

# 29. Split a string
string_1 = "My name is Saurabh Sharma"
string_2 = "sample/ string 2"
# default separator ' '
print(string_1.split())
# defining separator as '/'
print(string_2.split('/'))

# 30. Error handling in Python using the try/except block
a, b = 1,0
try:
    print(a/b)
    # exception raised when b is 0
except ZeroDivisionError:
    print("division by zero")
else:
    print("no exceptions raised")
finally:
    print("Run this always")

# 31. Enumerate to Get Index/Value Pairs
my_list = ['a', 'b', 'c', 'd', 'e']
for index, value in enumerate(my_list):
    print('{0}: {1}'.format(index, value))

# 32. convert an integer into a list of digits
num = 123456
list_of_digits = list(map(int, str(num)))
print(list_of_digits)

#33. Calculate the factorial of any number in one line.
import functools
result = (lambda k: functools.reduce(int.__mul__, range(1,k+1),1))(5)
print(result)

# 34. Four ways to reverse string/list.
   # A. Reverse the list itself.
testList = [1, 3, 5]
testList.reverse()
print(testList)
  # B. Reverse while iterating in a loop.
for element in reversed([1,3,5]): 
    print(element)
  # C. Reverse a string in line.
print("Test Python"[::-1])
  # D. Reverse a list using slicing.
print([1, 3, 5][::-1])

# 35. 

