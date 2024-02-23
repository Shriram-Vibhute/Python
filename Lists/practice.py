# List Comphrensitions
lst = [i*i for i in range(0, 11) if i%2 == 0]
# Pattern -> Expression + loop + condition
print(lst)

# List Methods -> Lists are mutable so most of the methods updates the originl list
lst = [i for i in range(1, 6)]
print(lst) # -> 1,2,3,4,5
print(lst.index(3)) # Return the index of 1st occurance of value - 2

lst.append(lst[lst.index(lst[len(lst)- 1])] + 1) # Lol 😂
print(lst)

lst2 = lst
# now lst and lst2 are same -> 
print(lst is lst2)
lst[0] = "shriram"
print(lst2[0])

# Doing the same with single variables
a = 3
b = a
a = 4
print(b)

# REMEMBER -> WHILE THE ASSINING THE (LISTS, TUPLES, MAP, SET) THE REFERANCES ARE SHARED AND NOT THE VALUES -> SO IF YOU CHANGE ONE VALUE FROM EITHER OF THEN THEN THAT CHANGE WILL GET REFLECTED TO THE BOTH

# This is not the case in single variables -> as only the value will get copied.in this case

# a = 9
# b = 10
# a.copy(b) -> AttributeError -> No attribute for int
# print(a) 

a = [1,2,3]
b = a.copy() # -> This is not like a.copy(b) error

# List Concination
#a + b
a.extend(b)
print(a)

# Other Methods
a = [1,2,3,4,5]
print(a.pop(4))
print(a)

a.insert(2, 45)
print(a)