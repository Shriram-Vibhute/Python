f = open('file3.txt', 'r')

content = None
i = 1

while True:
    line = f.readline()
    if not line:
        break
    content = line.split(',')

    j = 0
    subs = ['Physics', 'Chemistry', 'Mathematics']

    for marks in content:
        print(f"The marks of roll no. {i} in {subs[j]} is {marks}")
        j+=1
    
    i+=1

f.close()
    