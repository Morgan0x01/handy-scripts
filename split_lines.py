#!/usr/bin/env python3

import os
import sys

try:
    os.mkdir('SplitFast')
except:
    pass
cwd = os.getcwd()
fname = input("file name: ")
fformat = input("Output file format(e.g .csv, .txt): ").strip('.')
amount = int(input("Enter amount of lines per file(e.g. 10000: "))

count = 1
filenum = 1
with open(cwd + '\\' + fname, 'r', encoding='utf8', errors='ignore') as file:
    file_content = file.read() # read raw bytes from file stream
    file_content_array = file_content.split('\n')
    content_length = len(file_content_array)
    print(f"{content_length} total lines.")
    if content_length < amount:
        print("Error: File content length less than split amount")
        sys.exit()
    parts = content_length / amount
    count = 0
    start = 0
    end = amount
    while count <= parts:
        chunk = file_content_array[start:end]
        new = "\n".join(chunk)
        try:
            with open(cwd + '\\SplitFast\\part_' + str(count+1) + '.' + fformat, 'a', encoding='utf8') as outfile:
                outfile.write(new)
        except:
            try:
                os.mkdir("SF_ERRORS")
                with open(cwd + '\\SF_ERRORS\\part_' + str(count+1) + '.' + fformat, 'a', encoding='utf8') as outfile:
                    outfile.write(line)
            except:
                pass
        start = end
        end += amount
        count += 1
print("Done!")