import os

def run_checks():
    current_directory = os.getcwd()
    output_path = os.path.join(
        current_directory,
        'output.txt'
    )

    assert os.path.exists(output_path), 'Please create a file called output.txt in the current directory'

    with open(output_path) as output_file:
        file_data = output_file.readlines()

        assert len(file_data) == 2, 'Please only write the names of the oldest and newest file to output.txt'

        oldest_file = file_data[0].strip()
        newest_file = file_data[1].strip()

        assert oldest_file == 'data_3.txt', 'Wrong oldest file!'
        assert newest_file == 'data_5.txt', 'Wrong newest file!'

    print('OK!')

run_checks()