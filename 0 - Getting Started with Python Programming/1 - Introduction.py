if __name__ == "__main__":
    # Print a simple greeting message
    print("hello world")
    
    # Define a variable with value 56
    a = 56
    
    # Print the result of adding 45 to the variable 'a'
    print(a + 45)

    # Uncommenting the following lines will cause errors due to type mismatch:
    # Concatenation of string with an integer (not allowed)
    # print("Shriram" + 56)  # This will raise a TypeError
    
    # Adding a string and an integer (not allowed)
    # b = "shriram" + 13  # This will also raise a TypeError

    # Demonstrating the print function's parameters:
    # 'sep' parameter specifies the separator between the printed values
    # 'end' parameter specifies what to print at the end of the statement
    print("Hello Python", "Hello C++", sep=" seperator ", end="end")
    
    # Print a new line
    print("Second Line")

    # Quick Quiz:
    # The print function does not return any value (returns None), so
    # 'a' will be assigned the value None. Then 'print(a)' will output None.
    a = print(type(print(5)))  # Output: <class 'NoneType'>
    print(a)  # Output: None
