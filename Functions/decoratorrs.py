def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Good Night")
    return mfx

@greet
def add():
    print(1 + 1)

add()
# greet(add)()

# Greet function with arguments
def dec_addons(fx):
    def modified_function(*lst, **dicts):
        print("You are using decorators")
        fx(*lst, **dicts)
        print("Thanks for using decorators")
    return modified_function

@dec_addons
def sum(a, b):
    print(a + b)

sum(1,2)