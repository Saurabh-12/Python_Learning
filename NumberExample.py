mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

import cmath

x = 4
y = 5

z = complex(x,y)
print(z)
print(z.real)
print(z.imag)
print(cmath.sqrt(z))

mylist = []
mylist.append(1)
mylist.append(2.0898989)
mylist.append("hello")

print(mylist[2])

for x in mylist:
    print(x)
numbers = [1, 2, 4]
strings = ["hello", "Saurabh"]
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]
numbers.append(3)
strings.append("kumar")
numbers.insert(2,1)
strings.insert(2,"sau")


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)