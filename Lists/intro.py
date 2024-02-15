n = int(input("Enter the length of the list : "))

# List Comprehensions - Creating list at runtime
lst = [int(input("Enter the number : ")) for i in range(0, n) if i != 3]
print(lst)

# -ve indexing
print(lst[-3]) # -> lst[len(lst) - 3]