import os

path = os.path.abspath(os.path.dirname(__file__)) + r"\bai1.txt"

file_path = 'bai1.txt'

if not os.path.exists(file_path):
    with open(file_path, 'w') as file:
        file.write(file_path)

print('List of names:')

with open(file_path, 'r') as file:
    for line in file:
        formatted_name = line.strip()
        print('-', formatted_name)