str = "Python is my favourit programming language"
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

# 2. Formating Method - AKA(f-strings)
str = "{} is my favourit programming language and {} as well"
print(str.format("python", "C++"))
str = "{1} is my favourit programming language and {0} as well"
print(str.format("python", "C++"))

# Other
str = "Python is my favourite programming language"
print(str.find("p"))
print(str.index("p")) # Gives error if arg in not present in an string

print('#'.join(str))

print(str.count('p')) # Case Sensitivity matters

# Rounding of the numbers using f strings
a = 1.2874567324
a = '{0:.4f}'.format(a)
print(a)