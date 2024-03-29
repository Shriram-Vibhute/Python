n = int(input("Enter the length of the list : "))

# List Comprehensions - Creating list at runtime
lst = [int(input("Enter the number : ")) for i in range(0, n) if i != 3]
print(lst)

# -ve indexing
print(lst[0: 5: 2]) # -> lst[len(lst) - 3]

# Quick Quiz -> Output
lst = [
    (1,2,5),
    (2,3,6),
    (3,4)
]
for first, second, third in lst:
    print(first, second, third)