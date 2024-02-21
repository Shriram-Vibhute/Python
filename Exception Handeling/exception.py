# # There is no multiple try, catch and finally in one error handeling block like
# # try:
# #    block of code
# # try:
# #    another block of code

# try:
#     a = int(input("Enter the number : "))
#     print(a)
# except Exception as e:
#     print("Your previous value is not a valid integer")
#     print("error message: ", e)
#     try:
#         b = int(input("Enter another number : "))
#         print(b)
#     except:
#         print("Got an error here as well")

# finally:
#     print("Finally will always get executed")

# # Error Handeling in function -> Interview Question
# def func():
#     try:
#         a = int(input("Enter the number : "))
#         return a
#     except Exception as e:
#         print("Your previous value is not a valid integer")
#         print("error message: ", e)
#         b = int(input("Enter the number : "))
#         return b

#     finally:
#         print("Finally will always get executed")
#     # if we dont use finally ->
#     # the rest of the block will near get executed

# # Handeling special type of errors using multiple exception values
# try:
#     # Here the line at which 1st error will et occured this error object type will get executed
#     # RAISING VALUE ERROR
#     a = int(input("Enter the value : "))

#     # RAISING INDEX ERROR
#     b = [5,6,7]
#     print(b[5])

#     # RISING TYPE ERROR
#     def func(a, b):
#         return a + b
#     func("err", 5)

# except ValueError:
#     print("ValueError")
# except IndexError:
#     print("IndexError")
# except TypeError:
#     print("TypeError")

# # RAISONG CUSTOM ERRORS
# # a = int(input("Enter the value: "))
# a = input("Enter the value: ")
# if a == 'quit':
#     print("quit")
# else:
#     try:
#         a = int(a)
#     except:
#         print("error")


