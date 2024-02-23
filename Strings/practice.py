str = "Python is my favourit progrsmming language"

# Multiline strings
multy_line_srings = """
    Hello Python
"""
print(multy_line_srings)

# str[5] = 45 -> TypeError - Strings are immutable

# String Slicing
lst = str.split(' ') # Converts the string into list having the elements which are seperated by ' '(arg to split) in main string
print(lst)

print(str[0:12:5]) # From 0 to 11 shift of 5
print(str[0:-5]) # -ve index slicing -> len(str) - 5

print(len(str))

# string methods
# 1. Modifying Strings
print(str.upper())
print(str.lower())
print(str.islower())
print(str.isupper())
print(str.title()) # 1st letter of each word inside a string is capitalise
# str = "mY nAME is sHRIRAM" -> My Name Is Shriram
print(str.istitle())
print(str.capitalize())
print(str.swapcase())

print(str.replace('Python', 'C++')) # This also returns new string
print(str)

# 2. Formating Method
str = "{} is my favourit programming language and {} as well"
print(str.format("python", "C++"))
str = "{1} is my favourit programming language and {0} as well"
print(str.format("python", "C++"))

# Other
str = "Python is my favourite programming language"
print(str.find("p"))
print(str.index("p")) # Gives errorif arg in not present in an string
