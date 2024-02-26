class student:
    cp = 78
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def print(self):
        print(self.name, self.id)

class jack(student):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = "lang"

s = jack("jack sparrow", 90, "Python")
print(s.name)