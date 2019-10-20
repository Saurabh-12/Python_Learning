# Common Mistake #1: Misusing expressions as defaults for function arguments

def FunctionWithDefaultArgument(bar=[]):        # bar is optional and defaults to [] if not specified
     bar.append("baz")    # but this line could be problematic, as we'll see...
     return bar
 
 # 1st call print ['baz']
print(FunctionWithDefaultArgument())
# 2nd call print ['baz', 'baz'] , that is not expected 
print(FunctionWithDefaultArgument())
# 3rd Time print ['baz', 'baz', 'baz'] that is not expected 
print(FunctionWithDefaultArgument())

# Why ?????.... What is the mistake 
'''  Answer is that the default value for a function argument is only evaluated once,
 at the time that the function is defined. Thus, the bar argument is initialized to its 
 default (i.e., an empty list) only when foo() is first defined, 
 but then calls to foo() (i.e., without a bar argument specified) will continue to use 
 the same list to which bar was originally initialized.'''
 
print("............."*5)
# Solution
def FunctionWithDefaultArgs(bar=None):
    if bar is None:
        bar = []
    bar.append("baz")
    return bar
 # 1st call print ['baz']
print(FunctionWithDefaultArgs())
# 2nd call print ['baz'] 
print(FunctionWithDefaultArgs())
# 3rd Time print ['baz']
print(FunctionWithDefaultArgs())

# Common Mistake #2: Using class variables incorrectly
class A:
    x = 1
class B(A):
    pass
class C(A):
    pass
print("............."*5)
print(A.x, B.x,C.x)  # O/P 1 1 1 as expected

print("............."*5)
B.x = 2
print(A.x, B.x,C.x)  # O/P 1 2 1 as expected

print("............."*5)
A.x = 3
print(A.x, B.x,C.x) #O/P 3 2 3 ??? wrong....expected was  3 2 1 Why ???
# We only changed A.x. Why did C.x change too?
# Solution 
''' In Python, class variables are internally handled as dictionaries and 
follow what is often referred to as Method Resolution Order (MRO). 
So in the above code, since the attribute x is not found in class  C, 
it will be looked up in its base classes'''
# Thus, references to C.x are in fact references to A.x. This causes a Python problem unless it’s handled properly

#Common Mistake #3: Specifying parameters incorrectly for an exception block
try:
    l = ["a", "b"]
    int(l[2])
#except ValueError, IndexError:  # To catch both exceptions, right? But this is wrong way...
except(ValueError, IndexError) as e: 
    pass

# Common Mistake #4: Modifying a list while iterating over it
print("............."*5)
odd = lambda x : bool(x % 2)
numbers = [n for n in range(10)]
for i in range(len(numbers)):
    if odd(numbers[i]):
        print(numbers[i])
        #del numbers[i]  # BAD: Deleting item from a list while iterating over it

# Common Mistake #5: Confusing how Python binds variables in closures
print("............."*5)
def create_multipliers():
    return [lambda x : i * x for i in range(5)]

for multiplier in create_multipliers():
    print(multiplier(2))
# Expected O/P :
#  0
#  2
#  4
#  6
#  8
# But You get O/p 
# 8
# 8
# 8
# 8
# 8
''' Why ??? 
This happens due to Python’s late binding behavior which says that the values of variables used in closures 
are looked up at the time the inner function is called. So in the above code, 
whenever any of the returned functions are called, the value of i is looked up in the surrounding 
scope at the time it is called (and by then, the loop has completed, so i has already been assigned its final value of 4).
'''
# Solution
print("............."*5)
def create_multipliers():
    return [lambda x, i=i : i * x for i in range(5)]

for multiplier in create_multipliers():
    print (multiplier(2))
# We are taking advantage of default arguments here to generate anonymous 
# functions in order to achieve the desired behavior

# Common Mistake #7: Creating circular module dependencies


