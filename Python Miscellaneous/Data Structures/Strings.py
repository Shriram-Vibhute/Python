# Quick Quiz -> Which case will reverse the string and why ?
a = "Dexter Morgan"

# case 1
print(a[0:len(a):-1])

# case 2
for i in range(0, len(a), -1):
    print(a[i], sep="", end="")

# case 3
print(a[::-1])

# case 4
reversed_str = "".join(reversed(a))
print(reversed_str)


# String Formating
# Using % operator - just like c language
print("Geeks : %d, Portal : %2.9f" % (1000, 05.333))
print("Total students : %3d, Boys : %2d" % (240, 120)) # print integer value
print("%7.3o" % (25)) # print octal value
print("%10.3E" % (356.08977)) # print exponential value

# format method
print("Hello {1:2.3f}, ok {0:3d}".format(134, 6.83274))

# f-strings
a = 34
b = 5.9384
print(f"Hello {a:2d}, ok {b:.7f}")

# string methods -> center(50, '#'), rjust(50, '#'), ljust(50, '#')


# String updating
# Using slice and join methods -> The surname is wrongly printed you have to hange the surname with Sparrow
a = "Dexter Morgan"
sub1 = a[0:7]
print(sub1)
new_surname = input("Enter your surname : ")
print(a := sub1 + new_surname)


lst = ['a','b','c']
str = ''.join(lst)
print(str, lst)

# Using -> list conversion and updating -> Character updation
a = "Dexter Morgan"
a = list(a)
a[4] = 'C'
print(a := ''.join(a))


# The string deleting is also same as string updating -> conversion into list / slice the string and join them