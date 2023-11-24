import os

file_name = input('Input file name: ')

if os.path.isfile(file_name):

    with open(file_name, 'r') as file:
        print("File content:")
        for line in file:
            formatted_line = line.strip()
            print(formatted_line)
else:
    print("File not found.")