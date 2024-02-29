# Chaining of decoraters

def f1(func):
    def new_func(num):
        func()
        print(num)
        return num * num
    return new_func

# 3 Ways to call these functions

# Way 1 -> Decorators
@f1
def new_func():
    print("The new num is : ")

# Way 2 -> First Class functions
# a = f1(new_func)
# print(a(14))

# print(f1(new_func)(14))
    

    
# Parameterized Decorators
def decorator_func(x, y):

	def Inner(func):

		def wrapper(*args, **kwargs):
			print("I like Geeksforgeeks")
			print("Summation of values - {}".format(x+y) )

			func(*args, **kwargs)
			
		return wrapper
	return Inner


# Not using decorator 
def my_fun(*args):
	for ele in args:
		print(ele)

# another way of using decorators
decorator_func(12, 15)(my_fun)('Geeks', 'for', 'Geeks')