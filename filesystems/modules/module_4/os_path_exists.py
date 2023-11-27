import os

# We might want to check if a file exists. We can do this with os by
# using os.path.exists, and passing the path we want to check for.
# Uncomment and modify the code below so that it checks if a directory
# called:
#
#   new_folder
# 
# exists as a subdirectory of the current directory (the place where we're running
# this script). The code should print "Directory new_folder not found!"

path = ""

path_exists = os.path.exists(path)

if path_exists:
    print(f"Directory {path} exists!")

else:
    print(f'"Directory {path} not found!')

 
