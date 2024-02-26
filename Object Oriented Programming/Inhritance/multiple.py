class animal:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print(self.name)
    
    def animal_funk(self):
        print("This is animal class")
        
class Dog:
    def __init__(self, dog_name):
        self.dog_name = dog_name
    
    def show(self):
        print(self.dog_name)
    
    def dog_funk(self):
        print("This is dog class")
        
# The order of inheritance matters (Dog, animal)
class Tyson(Dog, animal):
    def __init__(self, name, dog_name):
        
        # How to resolve
        # super().__init__(self.name)
        # super().__init__(self.dog_name)
        
        self.name = name
        self.dog_name = dog_name
        
        
    def show(self):
        print("name", self.name)
        print("name", self.dog_name)
        
t = Tyson('dg', 'dg_name')
t.show()
print(Tyson.mro)

t.animal_funk()
t.dog_funk()    