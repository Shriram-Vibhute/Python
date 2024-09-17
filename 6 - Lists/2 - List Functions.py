# List Comphrensions
l = [int(input("Enter the number: ")) for i in range(0, 5)]
m = [i for i in range(0, 5)]

# Changing List Items

# Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) # banana will get overrided by watermelon

# The whole 1 and 2 index items will be replaced by one watermelon
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# insert function - To insert a new list item, without replacing any of the existing values
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Add List Items

# append - at last
l.append(10) # updates the original array
print(l)

# extend - Append all elements from another list or iterable
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) 

# Removing Elements
thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana") # Take element as arg not an index and removes the 1st occurance
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) # Take index as arg - if not given then removes the last element
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear() # Remove all the elements
print(thislist)

# Sorting
def myfunc(n):
  return abs(n - 50)

thislist = [51, 49, 100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) # How close the number to 50

thislist = ["apple", "banana", "cherry"]
thislist.sort(key=str.lower()) # ByDefault the sort function is case sensetive 

l.sort()
l.sort(reverse=True) # sort in dereasing order

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

print(l.index(40)) # error -> index out of bound

print(l.count(2)) # Count all the occurances of 2

# Referance binding
k = l
k[0] = "Dexter"
print(l) # -> Both arrays get updated here

k = l.copy()
print(k)

k = l + m
print(k)    

k = l * 2
print(k)

print(2 * [1,1,1])