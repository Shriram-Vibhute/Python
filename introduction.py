if __name__ == "__main__":
    print("hello world")
    a = 56
    print(a + 45)

    # print("Shriram" + 56); -> Only similar type variables will get added
    # b = "shriram" + 13 -> This will also give an error

    # print functions parameters
    print("Hello Python", sep = " seperator ", end = "end")
    # The parameters also contains -> file and flush
    print("Second Line")
    # default -> end = \n sep = " "

    # Quick Quiz -> Output of below code
    a = print(type(print(5))) 