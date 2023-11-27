import os
import time
# This challenge uses what you've learned in Filesystems Modules 1-8.
#
# OBJECTIVE:
#
# Given the files in this directory, write a script that identifies the oldest
# file based on access time, the newest file based on access time, calculates the 
# difference between their ages (and prints the info to consle), and the difference 
# between the current time and the newest file (and prints the info to console). 
# The script should then write the names of the oldest and newest files to a 
# file called:
# 
# output.txt 
#
# with each name on a different line, i.e.:
# 
# <oldest_file_name>.txt
# <newest_file_name>.txt
# 
# Be warned, some files might have surprise information!
#
# HELP:
#
# For this exercise, recal that there are Linux utilities the Python os module
# wraps that allow us to discern information about the age of various aspects
# of a file. Also recall that UTC epoch starts at midnight, January 1, 1970.
# What happens if a file has information from before that? 
# 
# We recommend using the Python sorted() built in cast to a list():
# 
# sorted_data = list(sorted(...))
#
# for any sorting. Don't forget to run the tests to help if you're stuck! If 
# you need to reset this exercise, run the reset script.


def file_timings():
    files = [
        'data_1.txt',
        'data_2.txt',
        'data_3.txt',
        'data_4.txt',
        'data_5.txt'
    ]


file_timings()