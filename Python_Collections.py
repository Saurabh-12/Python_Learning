# Python collections are container data types, namely lists, sets, tuples, dictionary.
'''
A list is is mutable, stores duplicate values and elements can be accessed in it using indexes.
A tuple is ordered and immutable in nature, although duplicate entries can be present inside a tuple.
A set is an unordered collection of items.
A set created with set is mutable while the one created with frozenset is immutable.
Set is not indexed and does not have duplicate elements as well.
A dictionary has key value pairs and is mutable.
'''
# Explaning five of the most common python collections along with their usage.

# 1. namedtuple()
'''
It returns a tuple with a named entry, which means there will be a name assigned to each value in the tuple. 
It overcomes the problem of accessing the elements using the index values
'''
from collections import namedtuple
Marks = namedtuple('Marks', 'physics, chemistry, biology')
m1 = Marks('87', '54', '69')
print(m1.chemistry) # o/p : 54
# _make() to create a namedtuple instance with a list
m2 = Marks._make(['63','72','94'])
print(m2) #O/P: Marks(physics='63', chemistry='72', biology='94')

# 2. deque : The deque is a list optimized for inserting and removing items
from collections import deque
list = [1, 2, 3, 4, 5]
deq = deque(list)
print(deq) # O/P : deque([1, 2, 3, 4, 5])

deq.append(6)  # Add element in last
print(deq) # O/P : deque([1, 2, 3, 4, 5, 6])
deq.appendleft(0) # add element in begning 
print(deq) # O/P : deque([0, 1, 2, 3, 4, 5, 6])

deq.pop() # remove lastone
print(deq) # O/P : deque([0, 1, 2, 3, 4, 5])
deq.popleft() # remove first one 
print(deq) # O/P : deque([1, 2, 3, 4, 5])

# 3. Counter
'''
The Counter() function takes an iterable, such as a list or tuple, and returns a Counter Dictionary
The dictionary’s keys will be the unique elements present in the iterable, 
and the values for each key will be the count of the elements present in the iterable
'''
from collections import Counter
count = Counter(['a','b','c','d','b','c','d','b'])
print(count) #  O/P : Counter({'b': 3, 'c': 2, 'd': 2, 'a': 1})
# Passing string 
count = Counter("collections")
print(count) # O/P : Counter({'c': 2, 'o': 2, 'l': 2, 'e': 1, 't': 1, 'i': 1, 'n': 1, 's': 1})
#most_common() function. On applying it to a Counter object, 
# it returns a list of the N most common elements with their counts ordered from the most common to the least
count1 = Counter([1, 2, 3, 3, 2, 3, 1])
print(count1.most_common(3)) #O/P : [(3, 3), (1, 2), (2, 2)]

# 4. OrderedDict
'''
OrderedDict is a dictionary where keys maintain the order in which they are inserted, 
which means even if you change the value of a key later, it will not change the position of the key
'''
from collections import OrderedDict
od = OrderedDict()
od[1] = 'p'
od[2] = 'y'
od[3] = 't'
od[4] = 'h'
od[5] = 'o'
od[6] = 'n'
print(od) # OrderedDict([(1, 'p'), (2, 'y'), (3, 't'), (4, 'h'), (5, 'o'), (6, 'n')])

# 5. defaultdict
'''
The defaultdict works exactly like a python dictionary, 
with the only change that it does not throw KeyError on trying to access a non-existent key. 
Instead, it initializes the key with the element of the data type which is passed as an argument to defaultdict.
'''
from collections import defaultdict
d = defaultdict(int)
d[1] = 'python'
d[2] = 'collections'
print(d) # defaultdict(<class 'int'>, {1: 'python', 2: 'collections'})
print(d[3]) # 0

