class employee:
    # These are class variables
    company_name = "Apple"
    company_size = 1000

    def __init__(self, name, identity):
        # These are instance variables
        self.name = name
        self.identity = identity
    
    def showDetails(self):
        print(f"name: {self.name} | identity: {self.identity} | company name: {self.company_name}")
    
e = employee("dexter", "Softwere Developer")

# Two ways run a method
# e.showDetails()
# employee.showDetails(e)

e.showDetails()
e2 = employee("Harry", "Softwere Engineer")
e2.company_name = "Googel"
print(e.company_name)
print(e2.company_name)
