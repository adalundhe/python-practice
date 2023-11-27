import os
import time


# The stat command is one of the most useful for getting file information in Linux.
# Python wraps stat with os.stat, offering a programmatic means of extracting file 
# information like size, access time, birth time, etc. Run the code below for an example:

file_name = "test_1.txt"
current_path = os.path.join(
    os.getcwd(),
    file_name
)

file_info = os.stat(current_path)

print('FILE', file_name)
print('CREATION TIME: ', file_info.st_ctime)
print('ACCESS TIME: ', file_info.st_atime)
print('BIRTH TIME: ', file_info.st_birthtime)
print('MODIFIED TIME: ', file_info.st_mtime)
print('FILE SIZE: ', file_info.st_size)

# Note that all file date/time info is UTC seconds epoch, AKA a floating point number of 
# seconds since midnight - January 1, 1970 UTC. The Python "time" module likewise uses
# UTC seconds epoch. For example, the below uses the time module to calculate the UTC
# seconds epoch value for 90 days ago. Note that there are 3600 seconds in an hour:

three_months_ago_seconds = time.time() - (3600 * 24 * 90)
print('90 days ago was: ', three_months_ago_seconds, 'seconds ago.')


# Using what we know above and what we've learned from previous exercises, modify the code
# below to list all files in the current directory, but only print out the access time of a file
# if it was created less than 90 days ago.

path = os.getcwd()

