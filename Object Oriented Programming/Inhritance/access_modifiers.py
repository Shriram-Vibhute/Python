# By default all the veriables / mthods are public
class employee:
    def __init__(self):
        self.name = "Harry"
        self.id = "232"
        self.__password = "341231" # This is considered as private attribute -> not accessed, modified and not inhereated

harry = employee()
print(harry._employee__password) # This is called "Name Mangiling" -> Private menbers, unless they are assumed as private, will not be accessed by traditional way (. followed by attribute name)