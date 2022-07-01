#!/usr/bin/env python3
import time
import sys

def main():
    final_result = ''
    domain_list = input('Enter domain list file: ')
    role_names_file = input('Enter role names list file (e.g info, support): ')

    with open(domain_list, 'r') as domain_list:
        domains = domain_list.readlines()

        with open(role_names_file, 'r') as role_names:
            role_names = role_names.readlines()

            for role_name in role_names:
                # final_result += f'{role_name}@'.join(domains)
                role_name = role_name.strip()
                final_result += f'\n{role_name}@' + f'{role_name}@'.join(domains)

    with open('role_gen.txt', 'w') as outfile:
        outfile.write(final_result[1:])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted, exiting", end="")
        for i in "...":
            time.sleep(0.01)
            print(i, end="")
        sys.exit(1)