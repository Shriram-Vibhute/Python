def calculate(ans,operand,operator):
    print("value of operator : ", type(operator))
    if operator == 1:
        ans += operand
    elif operator == 2:
        ans -= operand
    elif operator == 3:
        ans *= operand
    elif operator == 4:
        if ans != 0:
            ans /= operand
    elif operator == 5:
        if ans != 0:
            ans %= operand
    elif operator == 6:
        if ans != 0: 
            ans //= operand
    elif operator == 7:
        return ans       
    else:
        print("Error")
    return ans

ans = input("Type your value : ")
ans = int(ans)
while(True):
    print("Choose operation by typing the corrosponding opstion number\n1. +\n2. -\n3. *\n4. /\n5. %\n6. // \n7. Total\n8. EXIT")
    b = input("Operation : ")

    b = int(b)
    if b == 8:
        print("Thank You")
        break
    elif b == 7: 
        print("Total : ", ans)
        break
    elif b < 1 or b > 8:
        print("Operation out of Bound")
        break
    
    a = input("Type your value : ")
    a = int(a)

    if (ans == 0 or a == 0) and (b == 4 or b == 5 or b == 6):
        print("Divide by 0 Error")
        break
    else:
        ans = calculate(ans, a, b)
