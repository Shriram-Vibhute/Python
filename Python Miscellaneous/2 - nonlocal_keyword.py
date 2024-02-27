a = 10
b = 20
def sum():
    # global a, b -> You can access the global variable without explicetely mentioning this statment. - This statment is for updating the thse valuse globally
    
    print(a, b)
    salt = int(input("Enter the value you wnat to add: "))

    def salt_addition():
        nonlocal salt
        return a + b + salt
    
    return salt_addition()

print(sum())