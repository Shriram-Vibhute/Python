# All the elements in the set will print in any order -> Interpereters choice
st = {"dexter", 4.3847, 5, 'r', True}
print(st)
for i in st:
    print(i)


st = {'5','4','3','2','1'}
print(st)
for i in st:
    print(i)


st = {23,87, -1, 98, -4, 345, 0}
print(st)
for i in st:
    print(i)

# Empty Set
st = {} # -> This gives you class dictonary
print(type(st))

st = set() # -> Thats how we create an empty set