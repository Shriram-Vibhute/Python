# Memoization using decorators
memory = {}

def memoizer(func):
    def checker(num):
        if num not in memory:
            print("Memoized Just now")
            memory[num] = func(num)
            return memory[num]
        else:
            print("Memoized Call")
            return memory[num]
    return checker

@memoizer
def fact(num: int) -> int:
    if num == 1:
        return 1
    
    return num * fact(num - 1)

# UnMemoized Call
print(fact(5))
# Memoized Call
print(fact(5))
print(fact(4))
print(fact(3))
print(fact(2))
# all the function calls called through decorator the memory ones

# Memoization will not done when you call each function explicitely like this 
print(memoizer(fact)(5))
print(memoizer(fact)(4))