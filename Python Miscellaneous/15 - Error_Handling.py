try:
    age = int(input("Enter Your age: "))
except Exception as e:
    print(e)
    print("Error -> Value cannot be converted ")
    try:
        age = int(input("Enter the correct age"))
    except:
        print("Error -> Value cannot be converted ")
finally:
    print("Error handled")

def smoker():
    weight = int(input('Enter your weight : '))
    if weight >= 75:
        raise ValueError("You are not able to join this competition")
smoker()
    
