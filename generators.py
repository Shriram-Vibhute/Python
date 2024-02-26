import time
def generator():
    for i in range(6):
        time.sleep(1)
        print(i + 1)
    
    yield 1
gen = generator()
next(gen)
# next(gen) -> this function will run till the end of the last yield statment after it throws an error

gen2 = generator()
next(gen2) # You can create another instance to run the code again