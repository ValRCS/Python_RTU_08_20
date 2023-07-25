# what is a file?

# file is a named location on disk to store related information
# it consists of bytes that are stored on a secondary storage device
# theoretically a file can be any length and can contain any kind of data
# file could even be stored in virtual memory - memory that is simulated by OS

# file is identified by a filename
# filename is a string of characters that uniquely identifies a file

# we have different types of files
# text files - contain readable characters (letters, numbers, symbols)
# binary files - contain data that has to be interpreted by a program
# for example, images, videos, audio files, zip, etc.

# let's start by reading some files
# first we need to know where are we currently

# we will use Path from pathlib module
# Path is a class that represents a path to a file or directory
# we can create Path object with Path('path_to_file_or_directory')
from pathlib import Path # so I import Path from pathlib module
# Path is supposed to be OS agnostic - no matter what OS you use it should work

# let's print current working directory
print("I am currently in", Path.cwd()) # cwd stands for current working directory

# let's check if there is a data folder in current working directory
# we can do it with Path.exists() method
print("Is there a data folder in current working directory?", Path('data').exists())
# we could use this for if statement

# let's get a list of all text files in data folder
# we can do it with Path.glob() method
# glob goes over all files in a specified directory and returns a generator
# glob returns a generator - so we need to convert it to a list
# generator is a lazy iterable - it doesn't store all values in memory
# generator gives you only one value at a time 
# generators are good for memory management
# generators are good for looping over large files
text_files = list(Path('data').glob('*.txt'))
print("Text files in data folder:", text_files)
# there is also rglob() method that goes over all files in a specified directory
#  and all subdirectories and their subdirectories, etc.
# r stands for recursive
# here data has not subdirectories so it doesn't matter
also_text_files = list(Path('data').rglob('*.txt'))
print("Text files in data folder:", also_text_files)
# compare length of text_files and also_text_files
print("Length of text_files:", len(text_files))
print("Length of also_text_files:", len(also_text_files))

# let's sort files by file size
sorted_text_files = sorted(text_files, key=lambda file: file.stat().st_size)
# print files and their sizes
for file in sorted_text_files:
    print(file, file.stat().st_size)

# let's find text file which has stop and frost in name
# let's just use glob
frost_files = list(Path('data').glob('stop*frost*.txt'))
print("Text files with frost in name:", frost_files)
# we will use first one
frost_file = frost_files[0]
print("Frost file:", frost_file)
# I could have just provided absolute or relative path to file by hand
# but I wanted to show you how to find files in a directory

# so gain relative paths are relative to current working directory
# absolute paths are unique regardless of current working directory

# generally we want to use relative paths - useful across different computers
# if something is not working check using absolute path

# our frost_file is relative but we can get absolute path
print("Absolute path to frost file:", frost_file.absolute())
# absolute method is provided by Path class
# we can get name, stem, suffix, parent, etc. of a file
print("Name of frost file:", frost_file.name)
print("Stem of frost file:", frost_file.stem)
print("Suffix of frost file:", frost_file.suffix)
print("Parent of frost file:", frost_file.parent)
# these are all goodies / attributes for objects created from Path class

# let's read frost file
# we will use open() function
# we will use context manager with open() function
# if we open file we also need to close it - context manager does it for us
# otherwise we would have to use close() method manually

# we will use with statement
# will not work with utf-8 encoded files which have non ASCII characters
# with open(frost_file, mode="r") as fstream:
#     text = fstream.read()
#     # file is still open here

# # file is closed here
# print(text)

# we need to provide encoding
# we can use utf-8 encoding

with open(frost_file, mode="r", encoding="utf-8") as fstream:
    text = fstream.read()
    # file is still open here   
# file is closed here
print(text)