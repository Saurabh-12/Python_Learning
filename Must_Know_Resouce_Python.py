# all or any
x = [True, True, False]
if any(x):
    print("At least one True")
if all(x):
    print("Not one False")
if any(x) and not all(x):
    print("At least one True and one False")

from collections import OrderedDict, Counter
# Remembers the order the keys are added!
x = OrderedDict(a=1, b=2, c=3)
# Counts the frequency of each character
y = Counter("Hello World!")
print(y)
print(x)

# dir :- look inside a Python object and see what attributes it has?
print(dir())
print(dir("Hello World"))
print(dir(dir))

from emoji import emojize
print(emojize(":thumbs_up:"))

""" from geopy import GoogleV3
place = "Manjunatha Layout,Munnekolala,Marathali, Bangalore, India"
location = GoogleV3().geocode(place)
print(location.address)
print(location.location) """

# **kwargs
# The double-asterisk in front of a dictionary object lets you pass the contents 
# of that dictionary as named arguments to a function.
dictionary = {"a": 1, "b": 2}
def someFunction(a, b):
    print(a + b)
    return
# these do the same thing:
someFunction(**dictionary)
someFunction(a=1, b=2)

#zip
# Ever needed to form a dictionary out of two lists?
keys = ['a', 'b', 'c']
vals = [1, 2, 3]
zipped = dict(zip(keys, vals))
print(zipped)

# uuid
# A quick and easy way to generate Universally Unique IDs (or ‘UUIDs’) 
# is through the Python Standard Library’s uuid module.
import uuid
user_id = uuid.uuid4()
print(user_id)

# pprint
import requests
import pprint
url = 'https://randomuser.me/api/?results=1'
users = requests.get(url).json()
pprint.pprint(users)



