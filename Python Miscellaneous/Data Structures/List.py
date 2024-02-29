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

# Given two numbers r1 and r2 (which defines the range), write a Python program to create a list with the given range (inclusive). 
"""
    Input : r1 = -1, r2 = 1
    Output : [-1, 0, 1]

    Input : r1 = 5, r2 = 9
    Output : [5, 6, 7, 8, 9]
"""
low = int(input("Enter the Lowest no. : "))
high = int(input("Enter the Highest no. : "))
lst = list() # Creaed a empty list
while low <= high:
    lst.append(low)
    low += 1
print(lst)

# with list comprehensions
low = int(input("Enter the Lowest no. : "))
high = int(input("Enter the Highest no. : "))
lst = list(i for i in range(low, high + 1))
print(lst)

# Using Recursion
def createList(low, high, List):
    # Base Condition
    if low > high:
        return

    # Recursive Relation
    List.append(low)
    createList(low+1, high, List)

def main():
    low = int(input("Enter the Lowest no. : "))
    high = int(input("Enter the Highest no. : "))  
    List = list() 
    createList(low, high, List)
    print(List)
main()

# Using lambda functions
low = int(input("Enter the Lowest no. : "))
high = int(input("Enter the Highest no. : "))
List = list(map(lambda x : x, range(low, high + 1)))
print(List)


# zip function in python
test_list = [1, 4, 5, 6, 7]
a = zip(test_list, range(len(test_list)), range(0, 10, 2))
print(list(a))


tp = [1,2,3,4,5]
l1, l2, l3, l4, l5 = tp
print(l1, l2, l3, l4, l5)

l1 = [1,2,3]
l2 = [100, 200]
l1.append(l2)
print(l1)