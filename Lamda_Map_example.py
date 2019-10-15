# Basically a Lambda function is a small, anonymous function
# Why anonymous? Simply because Lambdas are most often used to perform 
#small simple operations which dont require a formal function definition

def stupidFunction(x):
    return x**2+5

# Now See this function in Lamda
stupid_func = (lambda x : x ** 2 + 5)

# Print 
print([stupid_func(1), stupid_func(3), stupid_func(5)])

my_list = [2,1,0,-1,-2]
print(sorted(my_list))

# we can use a lambda function to define the key
print(sorted(my_list, key = lambda x : x**2))

# Map is simply a function used to apply
#  a function to some sequence of elements like a list
print(list(map(lambda x,y : x*y, [1,2,3], [4, 5, 6] )))

# Above Map function help below code  to beome one liner
x, y = [1, 2, 3], [4, 5, 6]
z = []
for i in range(len(x)):
    z.append(x[i] * y[i])
print(z)

