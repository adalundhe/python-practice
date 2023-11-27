import os

def run_checks():
    assert os.path.exists('dir_a'), 'Please create dir_a at the current path'
    assert os.path.exists('dir_a/dir_b'), 'Please create dir_b as a subidrectory of dir_a at the current path'
    assert os.path.exists('dir_a/dir_b/dir_c'), 'Please create dir_c as a subidrectory of dir_a/dir_b at the current path.'
    assert os.path.exists('dir_a/data_a.txt'), 'Please create data_a.txt inside dir_a'
    assert os.path.exists('dir_a/dir_b/data_b.txt'), 'Please create data_b.txt inside dir_b'
    assert os.path.exists('dir_a/dir_b/dir_c/data_c.txt'), 'Please create data_c.txt, inside dir_c'

    print('OK!')

run_checks()