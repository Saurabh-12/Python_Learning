# To start out, we have to import it from the functools module. 
# The main idea behind this is that it will apply a given function to the array of items and will return a single value as a result.
# The last part is crucial — reduce() won’t return an array of items, it always returns a single value

from functools import reduce

def add_number(a, b):
    return (a+b)

data = [5, 10, 12, 18, 25]

print(reduce(add_number,data))
