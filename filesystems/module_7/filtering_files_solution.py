import os


# SOLUTION:
#
# We need to make two modifications to our example in order to only print out
# .txt files starting with "test". First, we need to modify the existing endswith()
# check to determine wheterh a file ends with the ".txt" extension. Then, we need to
# add a call to:
#
# filepath.startswith()
#
# ot check whether the path starts with "test"

path = os.getcwd()

for filepath in os.listdir(path):
    if filepath.startswith("test") and filepath.endswith(".txt"):
        print('There is a text file at: ', filepath)


# NOTE: It is IMPORTANT to note that startswith() and endswith() DO NOT ACCEPT
# WILDCARD MATCHES (* character). For example, if we modify our call to:
#
# filepath.startswith("test")
#
# to:
#
# fileapth.startswith("test*")
#
# Our code will fail to print any of the correct matching paths, as there are no
# paths containing a "*" character.