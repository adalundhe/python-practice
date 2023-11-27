import os

# Now let's build upon listdir(). Uncomment and modify the code below so that it only lists
# the files in:
#
#   example_directory
#

search_path = "<insert_path_here>"

example_directory_paths = os.listdir(
    path=search_path
)

for path in example_directory_paths:
    print("Found", path, "!")

