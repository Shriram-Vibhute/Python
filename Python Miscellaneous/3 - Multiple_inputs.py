# Method 1: split method
a, b, c = input("Enter the value in one line seperated by space : ").split()
# based on seperator in split function you have to give each input accordingly
print(int(a) + int(b) + int(c))

# Method 2: list comprehensions
a = list(int(input("Enter the value: ")) for i in range(5) if i != 4)
print(a)