f = open('main.txt', 'r') # file must be in current directory
# NOTE -> if file is not present then throw an error
print(f.read())
f.close()

f = open('main.txt', 'w') # Opening in write  mode
# NOTE -> if file is not present then its creats a file then write it -> not throw an error
f.write("The Pirats")
f.close()

f = open('main.txt', 'a') 
f.write("The Pirats") # how much time you gonna run it will get appended
f.close()

f = open('file2.txt', 'x') # Create mode -> error if already exists
f.close()

f = open('file2.txt', 'rt') # Opening a file in text mode
f.close()

f = open('file2.txt', 'rb') # Opening a file in binary mode
f.close()