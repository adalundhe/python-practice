import os

# SOLUTION:
#
# The key modification here is to append the "example_directory" folder to the search_path variable.
# There are several ways of doing this, but the preferred way to do this when using the os module is
# via:
#
#   os.path.join()
#
# For example:

search_path = os.path.join(
   os.getcwd(),
   "example_directory"
)

example_directory_paths = os.listdir(
    path=search_path
)

for path in example_directory_paths:
    print("Found", path, "in example_directory!")

# Using os.path.join allows you to combined paths in a safe way without
# potential string format bugs, etc.