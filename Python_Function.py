'''
Python’s functions are first-class objects. We can 
     assign them to variables, 
     store them in data structures, 
     pass them as arguments to other functions, and 
     even return them as values from other functions.
'''
def welcomeMsg(name):
    return 'Welcome {} !!'.format(name)

# 1. Functions Are Objects. we can assign it to another variable, just like any other object(example strings, lists)
receive = welcomeMsg
# The above line does’t call the function. It takes the function object reference and creates a second name,
# We can execute the method by calling receive:
print(receive("Saurabh"))

# Function objects and their names are two separate things. 
# We can delete the functions’ original name  and still call the function, 
# since another name still points to it.
del welcomeMsg
#print(welcomeMsg("Saurabh")) # O/P : NameError: "name 'greet' is not defined"
print(receive("Saurabh"))  # O/P :Welcome Saurabh !!

# 2. Functions Can Be Stored in Data Structures
# we can add functions to a list:
funcs = [len, str.isdigit, str.upper]

for f in funcs:
    print(f, f('Hello World!'))
    
# 3. Functions Can Be Passed to Other Functions
def accept(func):
    msg = func('Roark')
    print(msg)

def welcomeMsg(name):
    return 'Welcome {} !!'.format(name)

def leave(name):
    return "Good Bye {}!".format(name)

accept(welcomeMsg)
accept(leave)
'''
The ability to pass function objects as arguments to other functions is powerful. 
It allows us to abstract away and pass around behaviours. 
In above example, accept function stays the same but we can influence its output by passing in different behaviours.
'''

# 4. Functions Can Be Nested. They are often called nested functions or inner functions.
def num1(x):
   def num2(y):
      return x * y
   return num2

res = num1(10)
print(res(5)) # O/P :- 50 
