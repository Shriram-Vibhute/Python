d = dict() # Creating an empty dictonary

L = [['a', 1], ['b', 2], ['a', 3], ['c', 4]]
# Que -> values are in the form of lists so that if the current key is already present in the dictonary then you can add the value corrosponding to it in that list

for i in range(len(L)):
    if L[i][0] not in d:
        d[L[i][0]] = [L[i][1]]
    else:
        d[L[i][0]].append(L[i][1])

print(d)

# Another Method
List = [(1,2), (2,3)]
print(d := dict(List))

# update method
l1 = {
    'name': "dextre",
    'id': 123
}
l2 = {
    "name": "Jon Snow",
    'id': 23
}
l2.update(l1) # Here the data of l2 is going to be updated to the data of l1 - for those values which having the same keys in both the dictonaries (INTERVIEW QUESTION)
print(l1)

# Using zip function
roll_no = [10, 20, 30, 40, 50]
names = ['Ramesh', 'Mahesh', 'Kamlesh', 'Suresh', 'Dinesh']
print(d := dict(zip(roll_no, names)))

# Enumerate function
l = list("shriram")
d = dict()
for i, val in enumerate(l):
    d[i] = val
print(d)

# Uisng pipe operator / merge operator / inplace merge operator
veg1 = {0:'Carrot', 1:'Raddish'}
veg2 = {2:'Brinjal', 3:'Potato'}
veg1 = veg1 | veg2 # |= inplace merge operator
print(veg1)