# As the name suggests the idea is to keep in array only the items that satisfy a certain condition.

def more_than_15(x):
    return x>15
data = [3, 17, 12, 19,7,20,11]

print(list(filter(more_than_15,data)))
