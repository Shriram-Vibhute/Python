st1 = {2, 4, 3, 6, 5}
st2 = {10, 20, 50, 40, 60}

# Union Set
union_set = st1.union(st2) # Gives a new set without updating the exsisting set
print(union_set)

update_set = st1.update(st2) # Dose not return -> only update exsisting set
print("st1: ", st1)
# print(update_set)

# Intersection Set
st1 = {2, 4, 3, 6, 5}
st2 = {4, 2, 6, 9, 3}

Intersection_set = st1.intersection(st2) # Return a new set
print(Intersection_set)
for i in Intersection_set:
    print(i)

st1.intersection_update(st2) # Update the original set
print(st1)

# Symmetric Difference -> (A U B) - (A n B)
st1 = {2, 4, 3, 6, 5}
st2 = {4, 2, 6, 9, 3}

symm_diff = st1.symmetric_difference(st2)
print(symm_diff)

st1.symmetric_difference_update(st2)
print(st1)

# Difference Method
st1 = {2, 4, 3, 6, 5}
st2 = {4, 2, 6, 9, 3}

diff_set = st1.difference(st2)
print(diff_set)

st2.difference_update(st1)
print(st2) # Element which were remained in st2

st1.difference_update(st2)
print(st1) # Elements which were remained in st1

# Disjoint Sets
st1 = {2, 4, 3, 6, 5}
st2 = {4, 2, 6, 9, 3}

print(st1.isdisjoint(st2)) # True -> not a single element is common in both the sets (A n B) = null

print(st1.issuperset(st2))
print(st1.issubset(st2))

# Some Other Methods
a = {2, 4, 3, 6, 5}

a.add(100)
print(a)

a.remove(100) # give an error if element is not present in set
print(a)

a.discard(100) # Doesnt give an error if element is not present in set
print(a)

a.pop() # Removes last element -> but it is unpredectiable

# del a -> deletes the set

# a.clear() -> Clear all the elements inside a set