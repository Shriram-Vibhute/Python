while (True): 
    a = int(input("Enter Your Age : "))

    match a:
        case 0:
            break
        case 18:
            print("You are just starting to drive, Your speed must be under 60kmph")

        # case _: -> This is default Case
  
        case _ if(a < 17):
            print("You are underage, You cannot drive")

        case _ if a > 18 and a < 60:
            print("You can drive")
        
        case _ if(a >= 60):
            print("Take precautions while driving")
        