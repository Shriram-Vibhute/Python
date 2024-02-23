# Keyword arbitory arguments

def sum(a, b, c):
    print(a + b + c)
sum(b = 45, a = 67, c = 100) # Specifying the the name of variables along with value and passing them as an arguments -> Order does not matters

# Passing arguments as a List
from functools import reduce

def sum_2(*lst):
    # using reduce HOC
    temp_sum = lambda a, b: a + b
    return reduce(temp_sum, lst)
        
print(sum_2(1,2,3,4,5))

# Passing arguments as a Dictonary
def funk(**mpp):
    print(f"my name is {mpp["name"]}, and my surname is {mpp["surname"]}")
    # Que -> As dictonaries are not iterable then how can we iterate over them wrt keys and values

funk(name="Dexter", surname="Morgan")