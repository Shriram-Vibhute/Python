# update()
# clear()

a = {
    'name': 'dex',
    'age': 69,
    'college': 'PCCOE'
}

b = a.pop('name')  # if key is not present the n gives key error
print(b) # Return a value of poped item
print(a)

del a[9]
print(a) # Same gives key error

b = a.popitem() # pops the last element

del a # delets the entire dictonary