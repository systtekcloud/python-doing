import os
from datetime import datetime

directory = 'batch-files-one'

filenames = os.listdir(directory)

for filename in filenames:
    filepath = os.path.join(directory, filename)
    print(filename)

    with open(filepath, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        print(word_count)

    day = datetime.now().strftime("%A")
    new_filename = f'{filename[:1]}-{word_count}-{day}.txt'
    print(new_filename)

    new_filepath = os.path.join(directory, new_filename)
    os.rename(filepath, new_filepath)

    print(f"Renamed {filename} to {new_filename}")