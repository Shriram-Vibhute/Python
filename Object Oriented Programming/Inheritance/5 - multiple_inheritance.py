class Animal:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id
        print(self.name)
        print(self.id)
    def display(self):
        print(self.name, self.id)

class Dog(Animal):
    def __init__(self, name, id) -> None:
        super().__init__(name, id)
    def display(self):
        print('Dog')

class Cat(Animal):
    def __init__(self, name, id) -> None:
        super().__init__(name, id)
    def display(self):
        print('Cat')

class Sound(Cat, Dog):
    def __init__(self, name, id) -> None:
        super().__init__(name, id)
        Dog.__init__(self, name, id)
    
    def display(self):
        super().display()
        Dog.display(self)

s = Sound('Hi', 1)
s.display()