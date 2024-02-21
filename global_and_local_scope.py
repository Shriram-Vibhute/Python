a = 4
b = 5

def swap():
    global a, b # here you are dealing with global a and b
    temp = a
    a = b
    b = temp

swap()
print(a, b)

# NOTE -> This is not actually considered as a good practice because the task which you want to perform will always done inside a function end to end