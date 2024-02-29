# self keyword and constructor __init__
class animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def print(self):
        print(f"name : {self.name} | color : {self.color}")

a = animal("Tyson", "Brown")
a.print()

# ________________________________________________________________________________________________

# Getters, Setters and Private members 
class employee:
    def __init__(self, name, id, role, password):
        self.name = name
        self.id = id
        self.role = role
        self.__password = password # Private member not as strictly private though.
    
    # Each getter functon must have only one setter function
    # Changing the name using getters and setters
    @property # Getter decorator
    def value_corrector(self):
        return self._employee__password
    
    @value_corrector.setter # Setter function
    def value_corrector(self, new_password):
        self._employee__password = new_password

e1 = employee("Jonnathan", 17, "ML Engineer", "Jonny123")
e1.value_corrector = "Dex123" # Clling those functions
print(e1._employee__password)

#_______________________________________________________________________________________________________

# Access Modifiers
