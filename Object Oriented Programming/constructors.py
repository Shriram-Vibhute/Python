class student:
    # id = 3423
    # name = "jndjsfdf"
    # address = "kf"
    # Theare is no need of creating this variables

    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
    
    def print(self):
        print(self.id, self.name, self.address)

shri = student(34, "klmdf", "fkdfmskfm")
shri.print()
