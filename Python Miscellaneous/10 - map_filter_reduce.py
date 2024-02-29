# Map function
List = [1,2,3,4,5]
square_list = list(map(lambda x : x * x, List)) # map function returns an object
print(square_list)

# filter function
filtered_list = list(filter(lambda i: i < 4, List))
print(filtered_list)

# reduce function
import functools
reduced_val = functools.reduce(lambda num1, num2: num1 + num2 / (num1 * num2), List)
print(float('{0:1.4}'.format(reduced_val)))