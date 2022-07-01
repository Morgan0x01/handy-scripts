#!/usr/bin/env python3
import random
import sys
import time
import datetime

def main():
    file_input = input("\nEnter file to randomize lines: ")
    start_time = time.time()
    with open(file_input, 'r', encoding='utf8') as file_:
        print(f"\n[{datetime.datetime.now().strftime('%H:%M:%S')}] Opened file")
        content = file_.read()
        print(f"\n[{datetime.datetime.now().strftime('%H:%M:%S')}] Read file")
        content_array = content.split('\n')
        random.shuffle(content_array)
        final = '\n'.join(content_array)


    with open(f"{file_input.split('.')[0]}_randomized_lines.txt", 'a', encoding='utf8') as outfile_:
        outfile_.write(final)
    
    end_time = time.time()
    total_time_taken = end_time - start_time
    print(f'\nTotal time taken: {total_time_taken} seconds')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted, Exiting', end='')
        for i in '...':
            time.sleep(0.1)
            print(i, end='')
        sys.exit(1)