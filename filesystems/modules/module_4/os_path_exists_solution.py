import os


# SOLUTION:
# 
# There are several ways to go about solving the above. The simplest is to just hardcode the
# "new_folder" directory name into the path string. However, if we want to take into account 
# that this script could be run elsewhere, we could again combine os.getcwd() and os.path.join():

path = os.path.join(
    os.getcwd(),
    "current_directory"
)

path_exists = os.path.exists(path)
if path_exists:
    print(f"Directory {path} exists!")

else:
    print(f'"Directory {path} not found!')