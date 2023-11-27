import os


# Sometimes we only want to act on certain files or paths. To do so, we can utilize
# Python string methods like startswith() and endswith() to filter files. For example:

path = os.getcwd()

for filepath in os.listdir(path):

    # If this is a CSV file.
    if filepath.endswith('.csv'):
        print(filepath, 'is a CSV!')


# Modify the code below such that it only prints a file's path if it is a ".txt" 
# file AND starts with "test":

path = os.getcwd()


