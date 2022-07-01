#!/usr/bin/env python3
import os
import sys
import time
from urllib.parse import quote

try:
    os.mkdir('URL_eNCoDed')
except:
    pass
cwd = os.getcwd()

def url_encode(content):
    url_encoded_string = ''
    for char in content:
        if int(ord(char)) > 32 and int(ord(char)) < 126: # ASCII Printable characters Range
            url_encoded_string += f"%{format(ord(char),'x').upper()}"
            continue
        else:
            url_encoded_string += quote(char)
            continue

    return url_encoded_string

def output(filename, output_content):
    with open(f"{cwd}\\URL_eNCoDed\\{filename}", 'a', encoding='utf-8') as output_:
        output_.write(output_content)

def main():
    input_file = input("Enter file to URL encode: ")
    with open(input_file, 'r', encoding='utf-8') as file_:
        content = file_.read()

    url_encoded_string = url_encode(content)

    output('URL_encoded.txt', url_encoded_string)
    print(url_encoded_string)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted, exiting", end="")
        for i in "...":
            time.sleep(0.1)
            print(i, end='')
        sys.exit(1)