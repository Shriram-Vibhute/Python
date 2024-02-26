class student:
    cp = 78
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def print(self):
        print(self.name, self.id)
    
s = student("jack sparrow", 90)

# dir method and __dir__ attribute
print(dir(s))
print('\n\n')
print(s.__dir__()) # Return a "LIST" containing all the variables and method associated with that class instance

# __dict__ attribute
print(s.__dict__) # Returns a "DICTONARY" contaning all the instance variables associated with the class instance by which __dict__were called

# HELP METHOD
print(help(student)) # Documentation of class
"""
Help on class student in module __main__:
class student(builtins.object)
 |  student(name, id)
 |
 |  Methods defined here:
 |
 |  __init__(self, name, id)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  print(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
-- More  --
"""