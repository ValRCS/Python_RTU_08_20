# Reading and writing files
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://realpython.com/read-write-files-python/
# file - set of continuos bytes for storing data - various formats
# libraries for many common formats (CSV, JSON, etc)
# plain text files - encodings and line endings could be different
# creating file object (file stream)
# closing file automatically with with context
# import os
# print(os.getcwd())

# with open('frost.txt') as f:  # create a file object
#     print(f.read())
# # f will be closed here already

# # list of supported encodings
# # https://docs.python.org/3/library/codecs.html#standard-encodings
# with open('frost.txt', encoding="utf-8") as f:  # create a file object
#     print(f.read())

# with open('frost.txt', encoding="utf-8") as f:  # create a file object
#     for line in f:
#         print(line)

# with open('frost.txt', encoding="utf-8") as f:  # create a file object
#     mylines = f.readlines()  # could also read a few lines with f.readline()

# print(mylines[:5])

with open('frost.txt', encoding="utf-8") as f:  # create a file object
    # could also read a few lines with f.readline()
    mylines = [line[:-1] for line in f]
    # 99.9%  of time newline ends with /n

# print(mylines[:5])

# with open('frost.txt', encoding="utf-8") as f:  # create a file object
#     # could also read a few lines with f.readline()
#     mylines = [line.rstrip() for line in f]
#     # 99.9%  of time newline ends with /n

# print(mylines[:5])

# super precise
# with open('frost.txt', encoding="utf-8") as f:  # create a file object
#     # could also read a few lines with f.readline()
#     mylines = [line.rstrip('\n') for line in f]
#     # 99.9%  of time newline ends with \n

# print(mylines[:5])

with open('frost.txt', encoding="utf-8") as f:  # create a file object
    # could also read a few lines with f.readline()
    # filtered_lines = [line.rstrip('\n') for line in f if "roads" in line]
    filtered_lines = [line.rstrip('\n')
                      for line in f if line.startswith("And")]  # possible to use regex from re
    # for more difficult filtering:
    # filtered_lines = []
    # for line in f:
    #     if line.startswith("And"):
    #         filtered_lines.append(line)

print(filtered_lines)

# how to write a file?
# with mode = "w" file will be created or overwritten
with open('frost-filtered.txt', mode="w", encoding="utf-8") as f:
    f.writelines(filtered_lines)
# file should be closed here

with open('frost-filtered.txt', mode="a", encoding="utf-8") as f:
    for line in filtered_lines:
        f.write(line)

# we will append to file
with open('frost-filtered.txt', mode="a", encoding="utf-8") as f:
    f.writelines(filtered_lines)

# open two files one for reading one for writing
# this could be very useful for working with very large files > more than your RAM
with open('frost.txt', encoding="utf-8") as fin, open('frost-filtered.txt', mode="w") as fout:
    for line in fin:
        if line.startswith("And"):
            fout.write(line)
