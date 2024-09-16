# Taking Single Input
a = input("Enter your name: ")  # takes user input and stores it as a string in 'a'
print("My name is", a)  # prints the entered name

x = input("Enter first number: ")  # takes user input for the first number, stored as a string in 'x'
y = input("Enter second number: ")  # takes user input for the second number, stored as a string in 'y'
print(x + y)  # concatenates the strings 'x' and 'y', prints the result

print(int(x) + int(y))  # converts 'x' and 'y' to integers and prints their sum

z = bool(input('Are you more than 18 years old? '))  # takes user input and converts it to a boolean (not directly useful as 'input' returns string)

# Taking Multiple Inputs
# Method 1: Using split method
a, b, c = input("Enter the value in one line separated by space : ").split(' ')  # splits the input string by spaces and assigns to 'a', 'b', 'c'
print(int(a) + int(b) + int(c))  # converts 'a', 'b', and 'c' to integers and prints their sum

# Method 2: List comprehensions
a = list(int(input("Enter the value: ")) for i in range(5) if i != 4)  # list comprehension to get 4 integer inputs, skips the 5th input
b = [int(input(f'Enter the {i} value: ')) for i in range(5)]  # list comprehension to get 5 integer inputs
print(a)  # prints the list 'a'