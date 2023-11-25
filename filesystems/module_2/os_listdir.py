import os

# Next, let's combine this with another Python command, listdir, which lists all files and directories 
# at the provided string path. Uncomment and modify the code below, such that this script lists
# all files and folders in the current path.

found = os.listdir(
    path='<insert_current_directory_here>'
)

for path in found:
    print(path)
