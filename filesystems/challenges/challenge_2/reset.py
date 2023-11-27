import os
import subprocess


def reset_challenge():
    current_directory = os.getcwd()
    
    output_filepath = os.path.join(
        current_directory,
        'output.txt'
    )

    if os.path.exists(output_filepath):
        os.remove(output_filepath)

    subprocess.run(
        'touch -d 1952-01-01T00:00:01Z data_3.txt',
        shell=True
    )
    subprocess.run(
        'touch -d "1970-01-01T00:00:01Z" data_2.txt',
        shell=True
    )
    subprocess.run(
        'touch -d "2020-06-28T03:03:01Z" data_1.txt',
        shell=True
    )
    subprocess.run(
        'touch -d "2023-11-26T20:38:00Z" data_4.txt',
        shell=True
    )
    subprocess.run(
        'touch -d "2023-11-26T20:38:01Z" data_5.txt',
        shell=True
    )


reset_challenge()