# Reading and writing files
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://realpython.com/read-write-files-python/
# file - set of continuos bytes for storing data - various formats
# libraries for many common formats (CSV, JSON, etc)
# plain text files - encodings and line endings could be different
# creating file object (file stream)
# closing file automatically with with context
import os
print(os.getcwd())

# with - context manager
# with open('frost.txt') as f:  # create a file object
#     print(f.read())  # so keep in mind this might not be best for HUUGe files
#     print("Trying again")
#     print(f.read())
#     print("Lets try again")
#     f.seek(0)  # put the needle of the record to beginning
#     print(f.read(20))
#     print(f.read(10))  # so this is the method you can use for fine reading
#     # f is still open here
#     f.seek(0)
#     res = f.read()  # not very efficient use of course , might have read it all in beggining
# # # f will be closed here already
# # without with I would have to call f.close()
# print(res)

# # list of supported encodings
# # https://docs.python.org/3/library/codecs.html#standard-encodings
# with open('frost.txt', encoding="utf-8") as f:  # create a file object
#     print(f.read())

# so with open('file.txt') as f: # we are opening file in read mode

# with open('frost.txt', encoding="utf-8") as f:  # create a file object
#     for line in f:  # so this will work even on huge files
#         # print(line)  # of course for big files we will not want to print
#         print(line.rstrip())
#         print(line.rstrip("\n"))  # most precise
#         # quick and dirty and generally okay possible last line has no \n
#         print(line[:-1])

# with open('frost.txt', encoding="utf-8") as f:  # create a file object
#     mylines = f.readlines()  # could also read a few lines with f.readline()

# print(mylines[:5])  # print first five lines

# with open('frost.txt', encoding="utf-8") as f:  # create a file object
#     # could also read a few lines with f.readline()
#     mylines = [line[:-1] for line in f]
#     # 99.9%  of time newline ends with /n

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

# with open('frost.txt', encoding="utf-8") as f:  # create a file object
#     # could also read a few lines with f.readline()
#     # filtered_lines = [(i, line.rstrip('\n'))
#     #                   for i, line in enumerate(f, start=1) if "roads" in line]
#     # filtered_lines = [line.rstrip('\n')
#     #                   for line in f if line.startswith("And")]  # possible to use regex from re
#     # possible to use regex from re
#     filtered_lines = [line for line in f if line.startswith("And")]
# for more difficult filtering:
# filtered_lines = []
# for line in f:
#     if line.startswith("And"):
#         filtered_lines.append(line)

# print(filtered_lines)

# how to write a file?
# with mode = "w" file will be created or overwritten
# with open('frost-filtered.txt', mode="w", encoding="utf-8") as f:
#     f.writelines(filtered_lines)  # remember to check if you need \n
# file should be closed here

# with open('frost-filtered.txt', mode="a", encoding="utf-8") as f:
#     f.write("\n"+"*"*40+"\n")
#     for line in filtered_lines:
#         f.write(line)

# we will append to file
# with open('frost-filtered.txt', mode="a", encoding="utf-8") as f:
#     f.writelines(filtered_lines)

# open two files one for reading one for writing
# this could be very useful for working with very large files > more than your RAM
with open('frost.txt', encoding="utf-8") as fin, open('frost-filtered.txt', mode="w") as fout:
    for line in fin:  # for each line in incoming file
        if line.startswith("And"):  # check some ondition
            fout.write(line)  # write into outgoing file
# so here both files will be closed and ready to be used
