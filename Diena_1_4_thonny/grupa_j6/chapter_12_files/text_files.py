# reading and writing text files

# what is a file after all?
# a file is a sequence of bytes
# represented on disk(storage) or in memory(ram)

# file operations
# open 
# opening has various modes
# r - read
# w - write
# a - append
# Full list of modes: https://docs.python.org/3/library/functions.html#open

# idea is when we open a file we get a file object - a stream of bytes
# then we perform operations on the stream
# finally we close the file - very important!
# we all know what happens when we don't close the file - can't do anything with it

# another concept is path
# path is a string that represents a location on disk
# we have absolute paths and relative paths

# absolute paths represent unique locations on disk
# example: C:\Users\user\Desktop\python\python_2020_11_16\grupa_j6\chapter_12_files\text_files.py

# relative paths represent locations relative to the current working directory
# example: text_files.py
# example: data/lorem_ipsum.txt etc

# absolute paths are OS specific and also depend on the file system
# they guarantee that we will find the file if it exists

# relative paths are OS agnostic and file system agnostic
# they are relative to the current working directory

# usually we want relative paths
# why?
# because we want to be able to move our code around

# so let's get our current working directory
import os
from datetime import datetime
print(os.getcwd()) # get current working directory
# i could change the current working directory
# os.chdir('..') # change current working directory up one level
os.chdir('data') # change current working directory to data
print(os.getcwd()) # get current working directory

# now let's open a file
# we will use context manager - with statement to automatically close the file
# we will use relative path
# by default open is read only
# with open("stopping_frost.txt") as fstream: # could call it f or fin etc
#     # fstream is a file object
#     # we can read from it
#     text = fstream.read()
#     # file is still open here
# # file is closed here - no need to close it manually!
# # first 100 characters
# print(text[:100])

# let me go back to our main directory
os.chdir('..') # change current working directory up one level
print(os.getcwd()) # get current working directory

# let's open a file in data directory
# with open("data/stopping_frost.txt") as fstream:
#     # i will read lines
#     lines = fstream.readlines() # so lines are separated by \n

# turns out Latvian letters are not automatically decoded!
# by default open uses ascii encoding

# solution - we specify encoding
# Python can't tell what encoding is used in the file!
# there are hundreds of encodings
# full list supported by Python: https://docs.python.org/3/library/codecs.html#standard-encodings


# so will specify encoding
with open("data/stopping_frost.txt", encoding='utf-8') as fstream:
    # i will read lines
    lines = fstream.readlines() # so lines are separated by \n
    # file still open here
# file is closed here - no need to close it manually!
# print first 5 lines
print(lines[:5])

# let's write back first 5 lines to a new file but include line numbers
# we will use relative path
# note that we will use write mode - w - write destroys the file if it exists
with open("data/stopping_frost_line_numbers.txt", mode='w', encoding='utf-8') as fstream:
    # file is open here
    # let's write a header
    fstream.write("First 5 lines of stopping_frost.txt\n")
    # alternative would be print
    print("print is a bit slower than write", file=fstream)
    # we will write line numbers
    for i, line in enumerate(lines):
        # we will write line number and line if it is not empty
        if line.strip():
            fstream.write(f"{i+1}. {line}")
    # file is still open here

# let's append a time stamp to the file
# we will use relative path
time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # you can format what you want
# notice mode - a - append at the end of the file!
# files can not be appended in the beginning or in the middle!
# if we need to do that we need to read the file, modify it and write it back
with open("data/stopping_frost_line_numbers.txt", mode='a', encoding='utf-8') as fstream:
    # file is open here
    fstream.write("\n" + "*"*20 + "\n")
    fstream.write(f"Time stamp: {time_stamp}\n")
    # file is still open here
# file is closed here

# let's look at a recipe to read and write large files line by line

# we will open a file for reading and another for writing
# we will use relative path
# could use one with
# with open("data/lorem_ipsum.txt", encoding='utf-8') as fin, open("data/lorem_ipsum_copy.txt", mode='w', encoding='utf-8') as fout:
# let's use two with
with open("data/stopping_frost.txt", encoding='utf-8') as fin:
    with open("data/stopping_frost_cleaned.txt", mode='w', encoding='utf-8') as fout:
        # both files are open is open here
        # we will read line by line from input file
        for line in fin:
            # we will write line by line to output file
            # if line starts with T we will write it
            if line.startswith("T"):
                fout.write(line)
        # both files are still open here
    # write file is closed here
# read file is closed here - both are closed

# above recipe will work on huge files (GBs) even if we have limited memory - as long as single row fits in memory

