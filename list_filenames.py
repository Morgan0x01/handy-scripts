from os import walk, getcwd

cwd = getcwd()

f = []

for (dirpath, dirnames, filenames) in walk(cwd):
    # f.extend(filenames)
    f.extend(dirnames)
    break

print('\n'.join(f))