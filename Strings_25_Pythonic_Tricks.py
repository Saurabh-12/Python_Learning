# Here are 25 top tips & tricks you might find useful!
# All these examples are using Python 3

# 1. Is a Substring in a String?
def sub_stringCheck(haystack: str="", needle:str="") -> bool:
    return needle in haystack

assest1 =  sub_stringCheck("the quick brown fox jumped over the lazy dog", "lazy") #== True
print(assest1)
assest2 = sub_stringCheck("the quick brown fox jumped over the lazy dog", "lazys") #== False
print(assest2)

# 2. Reverse a String
# Use a slice with a decreasing step to return the reversed string.
def string_reverse(forward: str = "") -> str:
    return forward[::-1]

print("hello",string_reverse("hello"))
print("goodbye", string_reverse("goodbye"))

# 3. Compare Two Strings for Equality
# Compare equality using == to see if two objects have an equal value.
# Compare identity using is to see if two objects are one and the same.
def are_equal(first_comparator: str = "", second_comparator: str = "") -> bool:
    return first_comparator == second_comparator

print(are_equal("thing one", "thing two")) #False
print(are_equal("a thing", "a " + "thing")) # True

# 4. Lowercase, Uppercase, Sentence Case and Title Case of a String
# Python has a number of in-built functions you can use to change the case of a string.

def to_uppercase(input_string:str) -> str:
    return input_string.upper()

def to_lowercase(input_string:str) -> str:
    return input_string.lower()

def to_sentencecase(input_string:str) -> str:
    return input_string.capitalize()

def to_titlecase(input_string:str) -> str:
    return input_string.title()

def to_swapcase(input_string:str) -> str:
    return input_string.swapcase()
  

print("THE END OF TIME ", to_uppercase("the end of time"))
print("the end of time ", to_lowercase("The End Of Time"))
print("The end of time ", to_sentencecase("The End of Time"))
print( "The End Of Time ", to_titlecase("the end of time"))
print("tHE eND oF tIME ", to_swapcase("The End Of Time"))

# 5. Concatenate Strings Efficiently
# Use join on an empty string to concatenate the parameters
def  concateString(*args) -> str:
  return "".join(args)

print("a b c : ", concateString("a", "b", "c"));

# 6. Is the String Empty or None?
def is_Null_Or_Empty(input_string : str = "") ->bool:
  if input_string: 
        if input_string.strip():
            return False
  return True

print(is_Null_Or_Empty(None)) #True
print(is_Null_Or_Empty("")) #True
print(is_Null_Or_Empty("   ")) #True
print(is_Null_Or_Empty("D")) #False
print(is_Null_Or_Empty("None")) #False

# 7. Trim Leading and Trailing Whitespace
def strip_it(input_string: str) -> tuple:
    return (input_string.lstrip(), input_string.rstrip(), input_string.strip())

left, right, full = strip_it("  A padded  string   ")
print(left)
print(right)
print(full )

# 8. Generate a String of Random Characters
# Use the secrets module to make random choices of characters to add to a string
import string
import secrets

def generate_random_string(length: int = 0) -> str:
    result = "".join(
        secrets.choice(string.ascii_letters + string.digits)
        for _ in range(length))
    return result

print(generate_random_string(20))

# 9. Read the Lines in a File to a List
# The file reader object f is being converted to a list implicitly here.
def file_to_list(filename: str = "") -> list:
    with open(filename, "r") as f:
        lines = list(f)
    return lines
print(file_to_list("workData.txt"))

# 10. Find the Substring Between Two Markers
import re

def between(first: str = "", second: str = "", input_string="") -> str:
    m = re.search(f"{first}(.+?){second}", input_string)
    if m:
        return m.group(1)
    else:
        return ""
print(between(input_string="adCCCTHETEXTZZZdfhewihu",
               first="CCC",
               second="ZZZ"))
# 11. Remove all Punctuation from a String
import string

def remove_punctuation(input_string: str = "") -> str:
    return input_string.translate(str.maketrans("", "", string.punctuation))

print(remove_punctuation("Hello!"))
print(remove_punctuation("He. Saw! Me?"))

# 12. Convert Between CSV and List

def from_csv_line(line: str = "") -> list:
    return line.split(",")
  
print(from_csv_line("a,b,c"))
  
# 13. take a list and return a CSV line
def from_list(line: list = []) -> str:
    ret = ", ".join(e for e in line)
    return ret

print(from_list(["a", "b", "c"]) )

# 14. Weave Two Strings
# Use zip_longest from the itertools module to zip two strings of unequal length
import itertools

def interleave(left: str = "", right: str = "") -> str:
    return "".join([i + j for i, j in itertools.zip_longest(left, right, fillvalue="")])
  
print(interleave("ABCD", "01"))

# 15. Remove Unwanted Characters from a String
# Use the replace function. Remember: We can’t change the value of a string in-place — strings are immutable.
def remove_unwanted(original: str = "",
                    unwanted: str = "",
                    replacement: str = "") -> str:
                    
    return original.replace(unwanted, replacement)

print(remove_unwanted(original="M'The Real String'", unwanted="M") )

# 16.  Find the Index Locations of a Character in a String
def find_char_locations(original: str = "", character: str = "") -> list:
    return [index for index, char in enumerate(original) if char == character]

print(find_char_locations("The jolly green giant.", "e"))

# 17. Translate a String to Leetspeak
def to_leetspeak(normal_speak:str="") -> str:
    leet_mapping = str.maketrans("iseoau", "1530^Ü")
    return normal_speak.translate(leet_mapping).title().swapcase()

print(to_leetspeak("the quick brown fox jumped over the lazy dogs"))

# 18. Use Base64 Encoding on Strings
# Base64 is a method to encode binary data as a string for transmitting in text messages.
import base64

def encode_b64(input_string: str = "") -> object:
    return base64.b64encode(input_string.encode("utf-8"))


def decode_b64(input_string: str = "") -> object:
    return base64.b64decode(input_string).decode("utf-8")

print(encode_b64("Saurabh"))
print(decode_b64(b"U2F1cmFiaA=="))

# 19. Encode and Decode UTF-8 URLs
"""
UTF-8 allows us to use extended, double-word characters — such as emojis. T
hese need to be encoded before they can be used in a URL
"""
import urllib.parse

def encode_url(url: str = "") -> str:
    return urllib.parse.quote(url)


def decode_url(url: str = "") -> str:
    return urllib.parse.unquote(url)

print(encode_url("https://saurabhsharma123k.blogspot.com/?title=❤❤❤"))
print(decode_url("https%3A//saurabhsharma123k.blogspot.com/%3Ftitle%3D%E2%9D%A4%E2%9D%A4%E2%9D%A4"))

# 20. Splitting Strings
strings = "Saurabh Sharma Blog have nice articles"
print(strings.split()) # return whitespace seprated list of string"

# 21. Checking for Anagrams
from collections import Counter
def is_anagram(s1, s2):
  return Counter(s1) == Counter(s2)
s1 = 'listen'
s2 = 'silent'
s3 = 'runner'
s4 = 'neuron'
print('\'listen\' is an anagram of \'silent\' -> {}'.format(is_anagram(s1, s2)))
print('\'runner\' is an anagram of \'neuron\' -> {}'.format(is_anagram(s3, s4)))

# 22. Checking for Palindromes
def is_palindrome(s):
  reverse = s[::-1]
  if (s == reverse):
    return True
  return False

s1 = 'racecar'
s2 = 'hippopotamus'

print('\'racecar\' a palindrome -> {}'.format(is_palindrome(s1)))
print('\'hippopotamus\' a palindrome -> {}'.format(is_palindrome(s2)))

#23. Find in String
var="Saurabh Kumar Sharma"
str="Sha"
print (var.find(str))
#24. Count : Returns the number of occurrences of substring ‘str’ in the String.
var='This is a good example'
str='is'
print(var.count(str))

# 25. Python replacing strings
a = "I saw a wolf in the forest. A lonely wolf."

b = a.replace("wolf", "fox")
print(b)

c = a.replace("wolf", "fox", 1)
print(c)



  
  

  



  
