print([x for x in "Hello Saurabh"])
print([ord(x) for x in "Hello Saurabh"])

# Function to squre
def stupidFunction(x):
    return x**2+5

# List of number
my_list = [1,2,3,4,5,6,7,8,9]
# List of odd number
new_list = []

# Iterating list, filtering odd number, using squre function 
# and adding result in new list 
for x in my_list:
    if x%2 !=0:
        new_list.append(stupidFunction(x))
print(new_list)

# Above all thing done in one liner list
print([stupidFunction(x) for x in my_list if x%2 != 0])

# Without function one liner
print([x**2+5 for x in my_list if x%2 != 0])

# boom!! above example is power of python list comprehension
