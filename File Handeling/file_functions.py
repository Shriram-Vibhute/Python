f = open('main.txt', 'r')

# Reading lines -> line by line
data = f.read() # reads the entire data
print(data)

while True:
    data = f.readline()
    if not data:
        break
    print(data)

print(f.readlines()) # Returns a list of all data seperated by new lines -> length of list = number of lines in file

f = open('main.txt', 'w')

# new way to write just like multy line string creation
f.write('''jfn
alk
aldf
f
kadfef
''')

lines = ['if\n', 'jfb\n', 'fbsfefkj']
f.writelines(lines)

f.write("jrngjng \n jisndfjkfng \n jsnfgkjnfg\n iwfkjsnfj")

f.close()
