import os
# SOLUTION:
#
# There are serveral methods we can use to create the directories. Our
# initial function accepts a string path, which we can split into a list.
 

def create_data_and_folders(path: str):
    folders = path.split('/')

    # Uncomment the below to see the list of folders
    # print(folders)

create_data_and_folders('dir_a/dir_b/dir_c')

# From here, we need to also get the path to the current directory. Recall
# that this can be done using os.getcwd():

def create_data_and_folders(path: str):
    folders = path.split('/')
    current_directory = os.getcwd()

    # Uncomment the below to see the current directory:
    # print(current_directory)

create_data_and_folders('dir_a/dir_b/dir_c')

# Now we need to break our problem into parts:
#
# 1. Iterate over the folders list.
# 2. Keep track of the current folder were're creating
# 3. Check if the folder exists firsts.
# 3. Create the folder at the current path if it does not exist.
# 4. Check if the data file exists.
# 5. Create the file if it does not exist.
#
# Let's get started with items (1) and (2):


def create_data_and_folders(path: str):
    folders = path.split('/')
    current_directory = os.getcwd()

    current_path = current_directory

    for folder in folders:
        current_path = os.path.join(
            current_path,
            folder
        )

        # Uncomment the below line to see the updated folder path
        # print(current_path)

create_data_and_folders('dir_a/dir_b/dir_c')

# Now we can tackle (3) and (4). Recall that os.path.exists() returns
# True if a path exists and False if it does not:

def create_data_and_folders(path: str):
    folders = path.split('/')
    current_directory = os.getcwd()

    current_path = current_directory

    for folder in folders:
        current_path = os.path.join(
            current_path,
            folder
        )

        if os.path.exists(current_path) is False:
            os.mkdir(current_path)

        # Uncomment the below line to verify the directory is created.
        # print(f'dir at {current_path} exists!', os.path.exists(current_path))

create_data_and_folders('dir_a/dir_b/dir_c')

# We need to perform some slight string parsing on the folder name to grab the 
# letter we need for the file. This can be done by again calling split(),
# passing the ('_') character, and then selecting the list item at index 1 (the 
# second list item).

def create_data_and_folders(path: str):
    folders = path.split('/')
    current_directory = os.getcwd()

    current_path = current_directory

    for folder in folders:
        current_path = os.path.join(
            current_path,
            folder
        )

        if os.path.exists(current_path) is False:
            os.mkdir(current_path)

        file_letter = folder.split('_')[1]

        # Uncomment the below to see the letter following the '_' for
        # each folder name
        # print('File letter is:', file_litter)

create_data_and_folders('dir_a/dir_b/dir_c')

# Finally, we need to use either string concatenation or (preferrably)
# string formatting to create our filename, combined with os.path.join()
# to assemble the full path. We can then pass our new data_file_path to
# os.path.exists(), creating the file if it does not exist:

def create_data_and_folders(path: str):
    folders = path.split('/')
    current_directory = os.getcwd()

    current_path = current_directory

    for folder in folders:
        current_path = os.path.join(
            current_path,
            folder
        )

        if os.path.exists(current_path) is False:
            os.mkdir(current_path)

        file_letter = folder.split('_')[1]

        data_file_path = os.path.join(
            current_path,
            f'data_{file_letter}.txt'
        )

        if os.path.exists(data_file_path) is False:
            data_file = open(data_file_path, 'w')
            data_file.close()

create_data_and_folders('dir_a/dir_b/dir_c')

