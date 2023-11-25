import os
import pathlib
import time

# SOLUTION
#
# We'll want to break our solution down into parts. First by making sure that 
# we're accurately calculating the time threshold of 60 days ago.

print('\n')
current_directory = os.getcwd()
# Recall the unit conversions is: 3600 seconds per hour * 24 hours per day * 60 days
time_threshold = time.time() - (3600 * 24 * 60)
print(time_threshold, 'is sixty days ago.\n')


# Next we'll need to use what we've just learned with pathlib Path objects and
# the rglob() method to make sure we're only finding .txt files starting with "test":

current_path = pathlib.Path(current_directory)

for found_file in current_path.rglob("test*.txt"):
    pass

# Then we'll need the file info for each filtered file. Recall that Path() objects
# have a stat() method that operates exactly like calls to os.stat():

current_path = pathlib.Path(current_directory)

for found_file in current_path.rglob("test*.txt"):
    file_info = found_file.stat()

# Finally, we need to add the conditional that checks that the modified time of the file at
# the found path is newer than our time threshold of 60 days:


current_path = pathlib.Path(current_directory)

for found_file in current_path.rglob("test*.txt"):
    file_info = found_file.stat()

    if file_info.st_mtime > time_threshold:
        print(found_file.name, 'is a .txt file starting with test modified at',file_info.st_atime)

print('\n')