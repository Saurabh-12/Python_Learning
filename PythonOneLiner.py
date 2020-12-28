#Palindrome check
phrase = 'deleveled'
isPalindrome = phrase == phrase[::-1]
print(isPalindrome) #>> true

#Set creation
squares = { x**2 for x in range(6) if x < 4 }
print(squares) #>> {0, 1, 4, 9}

#List mapping
l = list(map(int, ['1', '2', '3']))
print(l) #>> [1, 2, 3]

# List creation 
list_1 = [('Hi '+ y) for y in ['sks', 'mks','pks']]
print(list_1) #>> ['Hi sks', 'Hi mks', 'Hi pks']

#Write string to file
with open('file.txt', 'a') as f: f.write('hello world')
print(list(open('file.txt'))) #>> ['sks1\n', 'sks2\n', 'sks3\n', 'sks4\n', 'hello world!!!']

# Read file into array of lines
c = [line.strip() for line in open('file.txt')]
print(c) #>> ['sks1', 'sks2', 'sks3', 'sks4']

#Delete multiple elements
#slicing syntax can also be used to delete multiple list elements at once
a = [1,2,3,4,5]
del a[::2]
print(a) #>> [2, 4]

# Sum over every second element of a list
a = [1,2,3,4,5,6]
s = sum(a[1::2])
print(s) #>> 12

# Multiple variable assignment
a, b, *c = [1,2,3,4,5]
print(a,b,c) #>> 1 2 [3, 4, 5]

# Swap two variables
a = 1; b = 2
a, b = b, a
print(a,b) #>> 2 1

# Sum of Even Numbers In a List
a = [1,2,3,4,5,6]
s = sum([num for num in a if num%2 == 0])
print(s)

# Creating Lists
lst = [i for i in range(0,10)]
print(lst) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# or 
lst = list(range(0,10))
print(lst)

# Mapping Lists or TypeCasting Whole List
print(list(map(int,['1','2','3']))) #[1, 2, 3]
print(list(map(float,[1,2,3]))) # [1.0, 2.0, 3.0]
print([float(i) for i in [1,2,3]] )# [1.0, 2.0, 3.0]

# Printing Patterns
n = 5
print('\n'.join('😀' * i for i in range(1, n + 1)))

# Prime Number
print(list(filter(lambda x:all(x % y != 0 for y in range(2, x)), range(2, 13))))

# Find Max Number
findmax = lambda x,y: x if x > y else y 
print(findmax(5,14))




