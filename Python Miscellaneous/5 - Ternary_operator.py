# Simple use in if else
print(1 if (1 > 3) else 2 if (3 > 4) else 3)

# Tuples
a, b = 10, 20
print((a, b)[a > b])

# Dictonary
print({True: a, False: b}[a > b])

# lambda functions
print((lambda: a, lambda: b)[a > b]())