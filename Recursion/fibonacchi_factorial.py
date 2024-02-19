def fibonacchi(n):
    if n == 1 or n == 0:
        return 1
    # Function Body
    return fibonacchi(n-1) + fibonacchi(n-2)

print(fibonacchi(4))

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))