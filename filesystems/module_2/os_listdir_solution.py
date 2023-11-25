import os

# SOLUTION
#
# We can replace the path argument to os.listdir() with a call to os.getcwd() to achieve our
# desired result:

found = os.listdir(
    path=os.getcwd()
)

for path in found:
    print("Found:", path)

# You could also simply replace the string with ".". However, this makes code more difficult to 
# understand or read.

