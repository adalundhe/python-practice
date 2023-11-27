import os

# We can combine os.path.exists() with os.mkdir() to create our missing directory. Uncomment and 
# modify the code below, then insert a call to os.mkdir() such that if a folder
# called "new_folder" does not exist as a subdirectory of the current directory, it is created:

path = os.path.join(
    os.getcwd(),
    "new_folder"
)

assert os.path.exists(path)
