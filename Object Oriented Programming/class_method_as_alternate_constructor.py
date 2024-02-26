class student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    @classmethod
    def altConstructor(class_name, string):
        name = string.split("-")[0]
        id = int(string.split("-")[1])
        return class_name(name, id) # Creating a new instance by calling a constructor
    
s1 = student("jonny", 17)
s2 = student.altConstructor("jack-12")

print(f"name: {s2.name} | id: {s2.id}")