import shutil
import os

shutil.rmtree(
     os.path.join(
        os.getcwd(),
        'dir_a'
    ),
    ignore_errors=True
)