class Student:
    college = 'PCCOE'
    District = 'Pune'

    def __init__(self, name, id, branch):
        self.name = name
        self.id = id
        self.branch = branch
    
    @classmethod
    def cust_constructor(cls, string):
        name, id, branch = string.split('-')
        return cls(name, id, branch)
    
    def print(self):
        print(self.name, self.id, self.branch)

class Boys(Student):
    def __init__(self, name, id, branch, sports):
        super().__init__(name, id, branch)
        self.sports = sports
    
    def print(self):
        super().print()
        print(self.sports)

class Girls(Student):
    def __init__(self, name, id, branch, sports):
        super().__init__(name, id, branch)
        self.sports = sports
    
    def print(self):
        super().print()
        print(self.sports)

class Batch(Boys, Girls):
    def __init__(self, name, id, branch, sports, batch):
        # To correctly initialize, ensure super() handles the call chain
        super().__init__(name, id, branch, sports)
        self.batch = batch
    
    def print(self):
        # Use super().print() to follow the correct MRO
        super().print()
        print(self.batch)

# Creating an instance of Batch
b1 = Batch('Payal', '10', 'CS-AIML', 'Dance', 1)
b1.print()