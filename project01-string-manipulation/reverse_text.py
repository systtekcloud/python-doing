import os

file = './file/words.txt'
file_name = os.path.basename(file)
file_location = os.path.dirname(file)
file_path = os.path.join(file_location, file_name)
reverse_file = './file/reverse_words.txt'


print(file_name)
print(file_location)
print(file_path)

def process_file():
  with open(file_path, 'r') as file:
    content = file.read()
    words = content.split()
    reversed_words = []

  for word in words:
    word = word[::-1]
    reversed_words.append(word)

  reversed_text = " ".join(reversed_words)

  with open(reverse_file, 'w') as file:
    file.write(reversed_text)

  

process_file()
