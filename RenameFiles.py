#rename example.txt to example-yyyy-mm-dd.txt

import os
from datetime import datetime

directory = 'files'

filenames = os.listdir(directory)

for filename in filenames:
    filepath = os.path.join(directory,filename)
    year = datetime.now().strftime("%Y")
    month = datetime.now().strftime("%m")
    day = datetime.now().strftime("%d")
    new_filename =  f'{filename[:-4]}-{year}-{month}-{day}.txt'
    new_filepath = os.path.join(directory,new_filename)
    os.rename(filepath,new_filepath)
    print(f"Renamed {filename} to {new_filename}")