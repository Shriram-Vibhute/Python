class student:
    name = "Shriram Vibhute"
    college = "PCCOE"
    roll_no = "128"

    def print_data(self):
        # print("self -> ", self) -> same as this keyword in c++ -> pointing to the the object by which the function os called
        print(self.name, self.college, self.roll_no)
    
uk = student()
uk.name = "Jack Sparrow"
uk. college = "JSPM"
uk.print_data()

shri = student()
shri.print_data()