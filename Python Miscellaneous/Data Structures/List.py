# Creating a list
a = input("Enter the numbers seperated by space (eg. 1 2 3..) : ")
a = a.split()
for i in range(0, len(a)):
    a[i] = int(a[i])
print(a)

# List Comprehensions
a = list(int(input(f"Enter the {i + 1}th value")) for i in range(0, 10) if i <= 5)


# Addition of elements -> append(), insert(), extend()
a = [1,2,3]
a.append(4) # Adds only one element at end of the list
print(a)
a.insert(2, 100) # Adds only one element at required position (pos, val)
print(a)
temp = ["a", "b", "c"] 
dummy = [True, False]
a.extend(temp) # Adds multiple values at the end of the list -> Also used to concat two lists
print(a)

# Deletion of elements -> pop(), remove(), del list[index]
a = [1,2,3,4,5]
print(poped_item := a.pop(4))
print(removed_item := a.remove(3)) # Returns None
del a[2]
print(a)