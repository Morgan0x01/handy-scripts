#!/usr/bin/env python3
# combine text files in folder
from os import walk, getcwd

cwd = getcwd()

f = []

for (dirpath, dirnames, filenames) in walk(cwd):
    f.extend(filenames)
    # f.extend(dirnames)
    break

contents = []

for file_ in f:
    if '.txt' in file_:
        with open(file_, 'r') as input_:
            input_ = input_.read()
            contents.append(input_)
            
with open('combined.txt', 'a') as output:
    output.write('\n'.join(contents))
