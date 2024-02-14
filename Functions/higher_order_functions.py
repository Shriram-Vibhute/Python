# Higher order function in Python
def passFunction(passed_function):
    def innerFunction():
        passed_function()
    return innerFunction

def innerFunction():
    print("peace")

passFunction(innerFunction)() # syntex importnt