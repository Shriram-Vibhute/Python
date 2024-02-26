class Vector:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self):
        return f"{self.a}i + {self.b}j + {self.c}k"
    
    # Operator Overloading with dunder methods
    def __add__(self, cls):
        return Vector(self.a + cls.a, self.b + cls.b, self.c + cls.c)
    
    def __sub__(self, cls):
        return Vector(self.a - cls.a, self.b - cls.b, self.c - cls.c)
    
    # def __mul__(slef, cls):
    # def __truediv__(slef, cls)

    def __gt__(self, cls):
        return ("You Fool, You Fool")

    # def __lt__() -> <
    # def __eq__() -> ==

    # Cannot overloaded with this
    # @classmethod
    # def addOperator(cls1, cls):
    #     return Vector(cls1.a + cls.a, cls1.b + cls.b, cls1.c + cls.c)
        
v1 = Vector(1,2,3)
v2 = Vector(4,5,6)
v3 = v1 + v2
v4 = v1 - v2

print(v3 > v4) # Giving another meaning to > operator 😁

print(v3 + v4)