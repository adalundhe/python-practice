import os
import time
import pathlib


# Using string matching to filter files is frail and will result in code often breaking with odd
# edge cases. To address these issues, Python offers the:
#
# pathlib
#
# module to handle path parsing. Let's examine our code from the previous exercise.

path = os.getcwd()

for filepath in os.listdir(path):
    if filepath.startswith("test") and filepath.endswith(".txt"):
        print('There is a text file at: ', filepath)

# As we noted before, startswith() and endswith() DO NOT accept wildcard matches. However,
# a pathlib Path instance's rglob() method does!

path = pathlib.Path(
    os.getcwd()
)

for filepath in path.rglob("test*.txt"):
    print(filepath, "is a TXT file starting with 'test'!")

# Pathlib objects have the additional advantages of allowing us access to a file's 
# name, filetype/stem, and stat() info:


for filepath in path.rglob("test*.txt"):
    print(filepath, "is a TXT file starting with 'test'!")
    print("File is", filepath.stem)
    print("File name", filepath.name)
    print("Access Time", filepath.stat().st_atime)


# Knowing what we know now, extend the code below such that only .txt files
# starting with "test" and having been accessed (having an access time newer than)
# within the past 60 days.

current_directory = os.getcwd()
# Recall the math from Module 6 and modify this to calculate 60 days ago in Epoch seconds.
time_threshold = time.time()


