set1 = {1,2,3,4,5}
# set1[2] = 34 -> Gives an error of not using assignment operator

# frozen sets -> immutable sets
temp = {1,2,3,4,5}
temp = frozenset(temp)

# Set data structure is used for esearching the element in the container -> hash set algo

set1 = {1,2,3}
set2 = {4,5,6}

# pipe operator - Interview Question
set1 |= set2
print(set1)

# Nice Example -> After every iteration of reduce function the return must be an iterable Data structure
from functools import reduce
test_set = {6, 4, 2, 7, 9}
up_ele = [1, 5, 10]
result_set = reduce(lambda res, ele: res.union(set([ele])), up_ele, test_set)

print("Set after adding elements : " + str(result_set))

# Reducing two lists symultenously
from functools import reduce
s1 = [1,2,3] # has to be reduced
s2 = [4,5,6,7,8,9] # Has to be updated

val = reduce(lambda res, elem: res + [elem], s2, s1)
print(val, s1, s2)