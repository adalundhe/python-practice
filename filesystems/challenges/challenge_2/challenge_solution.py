import os
import time
# SOLUTION:
#
# This challenge focuses on using os.stat() and time.time(), as well as being
# careful about stat information that involves files being created/accessed/modified
# before UTC epoch (midnight - January 1, 1970) which results in the floating point 
# UTC times for said file information being negative.
#
# We need to begin by collecting the stat information for each file in the current 
# directory and storing it. Recall that you can access the access time of a file by
# using os.stat() and then accesing the:
#
# .st_atime
#
# attribute:

def file_timings():
    files = [
        'data_1.txt',
        'data_2.txt',
        'data_3.txt',
        'data_4.txt',
        'data_5.txt'
    ]

    current_directory = os.getcwd()

    file_info = {
        file: os.stat(
            os.path.join(
                current_directory,
                file
            )
        ).st_atime for file in files
    }


    # Uncomment this to see the stored file name/access time k/v pairs:
    # print(file_info)

file_timings()

# We can choose a dictionary to make storing the correct file/time mappings
# easy, however note that this does make the call to sorted more tricky,
# as we'll have to convert the data structure to a list of tuples for proper
# sorting:

def file_timings():
    files = [
        'data_1.txt',
        'data_2.txt',
        'data_3.txt',
        'data_4.txt',
        'data_5.txt'
    ]

    current_directory = os.getcwd()

    file_info = {
        file: os.stat(
            os.path.join(
                current_directory,
                file
            )
        ).st_atime for file in files
    }

    sorted_file_data = list(
        sorted(
            file_info.items(),
            key=lambda file_data: file_data[1]
        )
    )

    # Uncomment this to see the sorted file name/access time pairs:
    # print(sorted_file_data)

file_timings()

# With the file name, timing pairs now sorted, we need to next grab
# the first item and last item in our list of file name/time pairs. Note
# that you can use destructuring with Python tuples to more efficiently
# access the name/time data for the oldest/newest name/time paris.

def file_timings():
    files = [
        'data_1.txt',
        'data_2.txt',
        'data_3.txt',
        'data_4.txt',
        'data_5.txt'
    ]

    current_directory = os.getcwd()

    file_info = {
        file: os.stat(
            os.path.join(
                current_directory,
                file
            )
        ).st_atime for file in files
    }

    sorted_file_data = list(
        sorted(
            file_info.items(),
            key=lambda file_data: file_data[1]
        )
    )

    oldest_file_name, oldest_file_time = sorted_file_data[0]
    newest_file_name, newest_file_time = sorted_file_data[-1]

    # Uncomment the below to see the oldest file name/time
    # print('The oldest file is:', oldest_file_name, 'with an access time of', oldest_file_time)

    # Uncomment the below to see the newest file name/time
    # print('The oldest file is:', newest_file_name, 'with an access time of', newest_file_time)

file_timings()

# From here, recall that we can get the current time by callng:
#
# time.time()
#
# We can then use traditional math operators to calculate the differences in
# time. However, note that our oldest file has a creation date of 01/01/1952
# at midnight, which is before UTC epoch of midnight - 01/01/1970. Thus, we'll
# need to use the Python abs() builtin to correctly calculate the time differences
# involving the oldest file.

def file_timings():
    files = [
        'data_1.txt',
        'data_2.txt',
        'data_3.txt',
        'data_4.txt',
        'data_5.txt'
    ]

    current_directory = os.getcwd()

    file_info = {
        file: os.stat(
            os.path.join(
                current_directory,
                file
            )
        ).st_atime for file in files
    }

    sorted_file_data = list(
        sorted(
            file_info.items(),
            key=lambda file_data: file_data[1]
        )
    )

    oldest_file_name, oldest_file_time = sorted_file_data[0]
    newest_file_name, newest_file_time = sorted_file_data[-1]

    current_time = time.time()

    oldest_and_newest_time_diff = newest_file_time - abs(oldest_file_time)
    current_and_newest_time_diff = current_time - newest_file_time

    # Uncomment the below to see the oldest and newest file age difference:
    # print('The oldest file:', oldest_file_name, 'and newest file:', newest_file_name, 'have an age difference of:', oldest_and_newest_time_diff, 'seconds')

    # Uncomment the below to see the newest file name/time
    # print('The newest file:', newest_file_name, 'is:', current_and_newest_time_diff, 'seconds old')

file_timings()

# Finally, we just need to write the name of the oldest file, then the newest 
# file to a file called output.txt:

def file_timings():
    files = [
        'data_1.txt',
        'data_2.txt',
        'data_3.txt',
        'data_4.txt',
        'data_5.txt'
    ]

    current_directory = os.getcwd()

    file_info = {
        file: os.stat(
            os.path.join(
                current_directory,
                file
            )
        ).st_atime for file in files
    }

    sorted_file_data = list(
        sorted(
            file_info.items(),
            key=lambda file_data: file_data[1]
        )
    )

    oldest_file_name, oldest_file_time = sorted_file_data[0]
    newest_file_name, newest_file_time = sorted_file_data[-1]

    current_time = time.time()

    oldest_and_newest_time_diff = newest_file_time - abs(oldest_file_time)
    current_and_newest_time_diff = current_time - newest_file_time

    print('The oldest file:', oldest_file_name, 'and newest file:', newest_file_name, 'have an age difference of:', oldest_and_newest_time_diff, 'seconds')
    print('The newest file:', newest_file_name, 'is:', current_and_newest_time_diff, 'seconds old')

    with open('output.txt', 'w') as output_file:
        output_file.write(f'{oldest_file_name}\n')
        output_file.write(f'{newest_file_name}\n')

# Uncomment this to run the full solution.
file_timings()
