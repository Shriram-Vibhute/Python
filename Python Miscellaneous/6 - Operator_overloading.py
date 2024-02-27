class oploading:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, new_class):
        # Add operator -> overloaded
        return self.num + new_class.num

    def __sub__(self, new_calss):
        # Sub operator -> overloaded
        return self.num - new_calss.num
    
    def __mul__(self, new_class):
        # mul operator -> overloded
        return self.num * new_class.num

    def __truediv__(self, new_class):
        return self.num / new_class.num

obj1 = oploading(False)
obj2 = oploading(True)
print(obj1 / obj2)