# Creating a empty set
set1 = set() 
print(set1)

# Creating a set with strings
set1 = set("DexterMorgan")  
print(set1) 

# Creating a set with list
set1 = set(["Captain", "Jack", "Sparrow"]) 
print(set1) 

# Creating a set with list having duplicates
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])  
print(set1) 

set1 = set(['s', 'S'])
print(set1)

# Creating set from tuples is exactly same as list

# Cresting list from Dictonaries
set1 = set({
    'name': "Dexter",
    'id': 123
}.values()) 
print(set1)