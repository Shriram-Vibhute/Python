f = open("abc.txt", 'r')
for data in f.readlines():
    print(data)
f.close()

f = open("abc.txt", 'w')
f.writelines(['abc\n', 'def\n', 'ghi'])
f.close()

f = open('abc.txt', 'r')
f.seek(5)
print(f.readline())
print(f.tell())
f.close()

# r+ -> read - write mode symultenously
f = open('abc.txt', 'r+')
f.truncate(10)
f.read()
f.close()