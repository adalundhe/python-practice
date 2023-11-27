import os

# The Python OS module allows you to perform many of the functions you'd use Bash
# commands for via Python code. This includes things like getting current or changing 
# directories, getting file info, creating directories, etc.

# Let's get start with an example of how to get the current directory. Go ahead and
# run the code below via:
#
#  python os_and_paths.py
#
# 

current_directory = os.getcwd()
print('Current directory is: ',current_directory)

# Note that this prints out the directory of where we're running our script. 

