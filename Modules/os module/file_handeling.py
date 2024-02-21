import os

if not os.path.exists("data"):
    os.mkdir("data") # Makes new folder
# if you run the programm more than once time then it gives ans error of -> FileExistError also it does not create that folder multiple times

print(os.curdir) # curdir is a property and not a function

for i in range(1, 101):
    os.mkdir(f"data/day {i}") # This also gives FileExistError while running it twice -> THe files ar ealready exist

    # mkdir will only creste folder/directory and not file like this
    # os.mkdir(f"data/day {i}/index.html")
    # os.mkdir(f"data/day {i}/index.js")

# Renname the file
for i in range(1, 101):
    os.rename(f"data/day {i}", f"data/Tutorial {i}")

# listing all the folders inside a folder
folders = os.listdir("data") # Returns a list of folders which in in given path
print(folders)