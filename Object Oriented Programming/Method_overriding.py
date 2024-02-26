class shape:
    def __init__(self, len, wid):
        self.len = len
        self.wid = wid
    
    def area(self):
        return self.len * self.wid

class circle(shape):
    def __init__(self, rad):
        super().__init__(rad, rad)
    
    def area(self):
        return 3.14 * super().area()

c = circle(3)
print(circle.area(c))