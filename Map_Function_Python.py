# The map() function takes in another function as a parameter, alongside an array of some sort. 
# The idea is to apply a function (the one passed in as an argument) to every item in the array.
# This comes in handy for two reasons:
#     * You don’t have to write a loop
#     * It’s faster than a loop

# Example I will declare a function called num_func() that takes one number as a parameter. 
# That number is squared and divided by 2 and returned as such. 
# Note that the operations were chosen arbitrarily, you can do anything you want inside the function:

def num_fun(x):
    return x**2/2

data = [1,2,3,4,5,6,7,8,9,10]
print(list(map(num_fun,data)))
# There’s nothing groundbreaking here, but it’s a good thing to avoid loops whenever possible

