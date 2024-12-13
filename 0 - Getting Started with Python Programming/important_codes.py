# Important Codes

if __name__ == "__main__":
    # Taking Multiple Inputes
    a, b, c = input("Enter the value in one line separated by space : ").split(' ')

    # Operators - Identity Operator
    print("\nIdentity Operators:")
    print("f is g:", f is g)          # True, because integers are immutable and 'f' and 'g' point to the same object
    print("f is not g:", f is not g)  # False

    h = [1, 2, 3]
    i = [1, 2, 3]

    print("h is i:", h is i)           # False, because 'h' and 'i' are different objects even if they have the same content
    print("h is not i:", h is not i)   # True

    # Typecasting
    print(str('False')) # False

    # Datatypes and Variables
    e = {
        "name": "Dexter",
        "college": "ABCD",
        'age': 69,
        True: "Whether redundant keys are possible to store in this",
        True: "Keys are in any form",
        None: 10
    } # None type key
