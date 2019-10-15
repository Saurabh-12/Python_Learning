x = int(input())
""" if x >= 10:
    print("Horse")
elif 1 < x < 10:
    print("Duck")
else:
    print("Baguette") """

# if else onliner 
print("Horse" if x >= 10 else "Duck" if 1 < x < 10 else "Baguette")

""" It’s really that easy! Going through your old code 
you’ll find tons of places where a simple conditional if / else statement
 can be simplified to a one-liner. """