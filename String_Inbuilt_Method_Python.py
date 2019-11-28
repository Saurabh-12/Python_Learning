'''
A string is a sequence of characters. T
he built-in string class in Python represents strings based upon the Unicode international character set
All the string methods always return new values and do not change or manipulate the original string.
'''

# 1. center( ) : center aligns a string
words = "Saurabh"
print(words.center(15, " "))

# 2. count( ) returns the count or the number of times a particular value appears in a string
str1 = "Kuamr Sharma Saurabh Kumar Sharma Saurabh kumar Saurabh Sharma"
print(str1.count('Saurabh'))
print(str1.count('Saurabh',9,36))

# 3. The find()method returns the lowest index of a particular substring in a string
print(str1.find('Saurabh'))
print(str1.rfind('Saurabh')) # rfind highest index

# 4. The swapcase() method returns a copy of the string with all its uppercase letters 
# converted into lower case and vice versa
str2 = "Saurabh Kumar Sharma"
print(str2.swapcase())

# 5. startswith( ) and endswith( )
print(str2.startswith('Kumar'))
print(str2.endswith("Sharma"))

# 6. split( )
fruits = "Apple, Mango, Grapes, Banana"
print(fruits.split())
print(fruits.split(","))
print(fruits.split(",", maxsplit=2))

# 7. String Capitalization
'''
capitalize( )
The capitalize() method capitalizes only the first character of a string.
            string.capitalize()
upper( )
The upper() method capitalizes all the letters of the string.
           string.upper()
string.title( )
The title() method capitalizes all the first letters of the given string.
          string.title()
'''
str3 = "Hey how are you"
print(str3.capitalize())
print(str3.upper())
print(str3.lower())
print(str3.title())

#8. The zfill() method adds zeros(0) at the beginning of the string
print('7'.zfill(2))
print('8'.zfill(3))

#9.The strip() method returns a copy of the string with the leading and trailing characters removed. 
# Default character to be removed is whitespace
str4 = "#...........Section 3.2.1 issue #32.................."
print(str4.strip('.#!' ))
print(str4.lstrip('.#!' ))
print(str4.rstrip('.#!' ))

