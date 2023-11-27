import os

# SOLUTION:
#
# We know from Module 4: os.path.exists() how to check whether a path exists. The primary
# catch here is to make sure we place the call to os.mkdir() in the correct block of an
# if/else statement, or otherwise use the right conditional checks:

path = os.path.join(
    os.getcwd(),
    "new_folder"
)

path_exists = os.path.exists(path)

if not path_exists:
    os.mkdir(path)

path_exists = os.path.exists(path)

assert path_exists

# NOTE: Calls to os.mkdir() will NOT recursively create directories. That is to say,
# if you were to try to run:
#
# os.mkdir(
#     os.path.join(
#         os.getcwd(),
#         "myfolder",
#         "new_folder"
#     )
# )
#
# The script would fail, as "myfolder" does not exist. 