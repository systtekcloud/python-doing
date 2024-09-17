import os
from datetime import datetime

directory = 'batch-files-two'

filenames = os.listdir(directory)

for filename in filenames:
    filepath = os.path.join(directory, filename)
    # print(filename)

    current_date = datetime.now().strftime("%Y-%m-%d")
    new_filename = f'{filename[:1]}-{current_date}.txt'
    # print(new_filename)

    new_filepath = os.path.join(directory, new_filename)
    os.rename(filepath, new_filepath)

    print(f"Renamed {filename} to {new_filename}")

print("File renaming complete")