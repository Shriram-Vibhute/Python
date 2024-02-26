# Where and why these magic methods were used

class student:
    def __init__(self, name):
        self.name = name
    
    def __len__(self):
        return len(self.name)
    
    def __str__(self):
        return f"This is self method"
    def __repr__(self):
        return f"This is rfer method"
    
    def __call__(slef):
        return "This funtion make object behaves like a function"

s = student('Dexetr') # init dunder will be run

print(len(s)) # length

print(str(s)) # if str method is not present in class then repr method will get executed
print(repr(s))

print(s())