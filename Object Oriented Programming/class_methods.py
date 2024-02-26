class student:
    name = "Shriram Vibhute"
    college = "PCCOE"
    roll_no = "128"

    @classmethod # By default 1st argument in the function is considered as class name -> no need to pass it explictly
    def print_data(class_name, newName):
        class_name.name = newName
    
s = student()
student.print_data("Dexter")
print(s.name)
print(student.name)
        # Do this without classmethod decorator