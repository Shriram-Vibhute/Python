# Everything in a python is created by object
a = 10
a = 5.875685 # Ptython is dunamically typed language
print(type(a))
b = None # object of NoneType
print("The type of b is : ", type(b))
print(type('shrrjfgj'))
c = [1, "dexter", {"age": 21}, 4.6] # lists are mutable
d = (1, "dexter", {"age": 21}, 4.6) # typles are immutable
e = {
    "name": "Dexter",
    "college": "ABCD",
    'age': 69,
    True: "Whether redundent keys are possible to store in this",
    True: "Keys are in any form"
}
print(type(e))
print(e[True]) # whichever is the last occurence will print that value corrosponding to that key