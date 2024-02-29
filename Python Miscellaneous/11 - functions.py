"""
    First class functions
    A function is an instance of the Object type.
    You can store the function in a variable.
    You can pass the function as a parameter to another function.
    You can return the function from a function.
    You can store them in data structures such as hash tables, lists, …
"""
# passing function as a parameter -> Higher Order Function
def dummy(text: str) -> str:
    return text.upper()

def string_merge(func, txt):
    return "The uppercased text is -> " + func(txt)

func = string_merge
print(func(dummy, "Dexter"))

# Returns a new Function -> Closure
def func(txt: str):
    def convert(dummy: str) -> str:
        return txt + dummy

    return convert

clsr = func("Hello")
print(clsr(" Python"))