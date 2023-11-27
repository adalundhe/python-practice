import os
import time

# SOLUTION:
#
# Breaking down this problem into its component parts, we should first focus on making
# sure that we're accurately listing each file in the directory:

# path = os.getcwd()

# for found_file in os.listdir(path):
#     print(found_file)

# From here, we need to use our newfound knowledge of os.stat() and similar time math to 
# the above example to write a conditional statment checking if a file's access time was more
# than 90 days ago:

path = os.getcwd()
days_ago_limit = time.time() - (3600 * 24 * 90)

for found_file in os.listdir(path):
    file_info = os.stat(found_file)
    file_last_accessed = file_info.st_atime

    if file_last_accessed > days_ago_limit:
        print('FILE: ', found_file, 'CREATED AT: ', file_last_accessed)


# If you want to get fancy, you can use the Python filter() builtin, along with a list()
# cast to optimize the code:

print('\n\nTHIS IS THE FANCY VERSION\n')

days_ago_limit = time.time() - (3600 * 24 * 90)
new_files = list(
    filter(
        lambda file_path: os.stat(file_path).st_atime > days_ago_limit,
        os.listdir(
            os.getcwd()
        )
    )
)

for new_file in new_files:
    print('FILE: ', new_file, 'CREATED AT: ', os.stat(new_file).st_atime)
    