class phone:
    def __init__(self):
        self.name = "Apple"
        self.id = "14 pro max"
    
    @staticmethod
    def accessories():
        print("Phone Cover + Headphones")

a = phone()
a.accessories()
phone.accessories()