age = int(input("Enter your age: "))
driving_licence = bool(input("Do you have Driving Licence : "))

match age:
    case 10:
        print("You are underage, you cannot drive")
    
    # case with if else condition
    case 18 if driving_licence:
        print("You can drive")
    
    case _ if age >= 18 and driving_licence:
        print("You can drive")
    
    case _ if age < 18:
        print("You cannot dive")