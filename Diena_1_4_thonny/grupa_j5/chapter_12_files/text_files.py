# reading and writing text files

# what is a file?
# a file is a named location on a storage medium
# represents a sequence of bytes

# file operations
# open a file - select mode of operation
# read or write (perform operations)
# close the file
# closing is important because it frees up resources and 
# makes the file available for other applications

# another concept relative vs absolute path

# absolute path - full path to the file - unique

# relative path - relative to the current working directory

# current working directory - the directory from which the program is running

# usually we want relative paths because they are shorter and more portable

# first let's get current working directory

import os # standard library module
print(os.getcwd()) # get current working directory

# looks like our current working directory is directory of whole project
# we have requirements.txt, .gitignore, .git, .idea, etc.

# let's read requirements.txt file

# we will use context manager to automatically close the file!!
with open('requirements.txt', 'r') as f:
    print(f.read())
    # file is stil open here
# file is closed here!

# i could save the data to a variable
with open('requirements.txt', 'r') as f:
    requirements = f.read()
    # file is stil open here
# file is closed here!
print(type(requirements))
print(requirements)

# i could also read the file line by line - useful for large files
with open('requirements.txt', 'r') as f:
    lines = f.readlines() # returns a list of lines
# print first 5 lines
print(lines[:5])

# looks like a unicode decode error
# let's try to open the file with utf-8 encoding
# with open('requirements.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines() # returns a list of lines
# # print first 5 lines
# print(lines[:5])

# ok let's try opening LICENSE file
with open('LICENSE', 'r', encoding='utf-8') as f:
    lines = f.readlines() # returns a list of lines
# print first 5 lines
print(lines[:5])