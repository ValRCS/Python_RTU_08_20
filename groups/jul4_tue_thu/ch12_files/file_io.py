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

from datetime import datetime # we will use datetime to print current date and time

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

with open(frost_file, mode="r", encoding="utf-8") as fstream: # name is arbitrary
    text = fstream.read()
    # file is still open here   
    another_text = fstream.read() # this will not work exactly as expected
    # file is open but stream is exhausted - we cannot read anything useful
    # to fix it we need to seek to the beginning of the file
    fstream.seek(0) # seldom used because usually we read file only once
    yet_another_text = fstream.read() # this will work
    # file is still open here
    # we can even seek specific position in the file
    # analogy with record player and needle on it
    # fstream.seek(100) # seek to 100th byte in the file
    # this can be useful if you have some encoding issues and you know where to look
# file is closed here
print(text)
# print stars
print("*" * 80)
print(another_text)
# again stars
print("*" * 80)
print(yet_another_text)

# there is also a way to read all lines in a file

with open(frost_file, mode="r", encoding="utf-8") as f: # again name is arbitrary
    lines = f.readlines() # this will read all lines in a file
    # what's a line? it's a sequence of characters that ends with a newline character
    # note: readlines keeps newline characters in the end of each line
    # file is still open here
# file is closed here

# let's print first 5 lines
for line in lines[:5]:
    print(line, end="") # end="" means don't print newline character
    # we do not need to print newline character because it's already in the line

# let's print last 5 lines directly
print("Last 5 lines:", lines[-5:])

# if i do not need newlines i can always use strip() method or even rstrip()
# or even rstrip("\n") - remove only newline characters at the right end of the string
# avoid line[:-1] - it will not work if there is no newline character at the end of the line

clean_lines = [line.rstrip() for line in lines]
# print first 5 clean lines
print("First 5 clean lines:", clean_lines[:5])
# only problem with clean lines we will need to put back newline characters
#  if we want to write them to a file

# finally we have a way to read large files line by line
# even those files that would not fit in memory
# we can use for loop to iterate over lines in a file

with open(frost_file, mode="r", encoding="utf-8") as f: # again name is arbitrary
    # so we can iterate over lines in a file
    # without opening whole file in memory
    for line in f:
        # do something with line
        # if line starts with "The" print it
        if line.startswith("The"):
            print(line, end="")

# let's write some text to a file
# we will use with statement again
# we will use open() function again
# we will use write() method
# mode will be "w" - write
# WARNING - w will overwrite file if it exists!

with open("data/test.txt", mode="w", encoding="utf-8") as f_out: # again name is arbitrary
    # file is open here
    f_out.write("This is a test file.\n")
    f_out.write("This is a second line.\n")
    # file is still open here
    # let's write last 5 lines from frost file
    f_out.writelines(lines[-5:])

    # we could even use print function to write to a file
    print("\nPrinted text to test file.", file=f_out)
    # i added \n because it was missing in last line of lines[-5:]
    # print to file is less used because it is slower than write
    # file is still open here
# file is closed here

# how do you check if file exists?
# we can use Path.exists() method
file_path = Path("data/test.txt")
print("Does test file exist?", file_path.exists())

# how do you check if file is a file?
# we can use Path.is_file() method
print("Is test file a file?", file_path.is_file())
# how do you check if file is a directory?
# we can use Path.is_dir() method
print("Is test file a directory?", file_path.is_dir())
# let's check if data folder is a file
print("Is data folder a file?", Path("data").is_file())
# let's check if data folder is a directory
print("Is data folder a directory?", Path("data").is_dir())

# so now let's check if file exists and we will append to it

if file_path.exists():
    print(f"Appending to {file_path}.")
    # we will use mode "a" - append
    # a will append to file if it exists and create it if it doesn't
    # so technically we do not need to check if file exists in this case
else:
    print(f"Creating {file_path}.")
    # we will use mode "w" - write
    # w will overwrite file if it exists and create it if it doesn't
    # so technically we do not need to check if file exists in this case

with open(file_path, mode="a", encoding="utf-8") as f_out: # again name is arbitrary
    # let's add some stars
    f_out.write("*" * 80 + "\n")
    # let's add current date and time
    f_out.write(f"Current date and time: {datetime.now()}\n")

# what other flags are there?
# Python Docs: https://docs.python.org/3/library/functions.html#open

# so append only appends at the end of the file
# why? historically it was faster to append to the end of the file
# we can not insert in the middle of the file in a classic way

# so what do we do if we want to insert in the middle of the file?
# we can simply write new file and then rename it

# so how about renaming files
# we can use Path.rename() method
# we will rename test.txt to test2.txt unless test2.txt already exists
# if test2.txt already exists we will delete it first
# we will use Path.unlink() method to delete file
# we will use Path.exists() method to check if file exists
if Path("data/test2.txt").exists():
    Path("data/test2.txt").unlink() # delete file
    # docs for unlink: https://docs.python.org/3/library/pathlib.html#pathlib.Path.unlink

Path("data/test.txt").rename("data/test2.txt")

# one more example on how to read and write huge files that do not fit in memory

big_file = Path("data/stopping_frost.txt") # not really a big file but it will do
# we will use with statement
# we will use open() function
# we will use read() method
# we will use write() method for output file
big_output_file = Path("data/stopping_frost_clean.txt")

# this recipe will work on any size file as long as single line fits in memory
with open(big_file, mode="r", encoding="utf-8") as f_in:
    with open(big_output_file, mode="w", encoding="utf-8") as f_out:
        for row in f_in:
            if row.startswith("The"):
                # do something with row
                # just an example
                # let's remove newline characters
                row = row.rstrip()
                # let's remove punctuation
                row = row.replace(",", "").replace(".", "")
                # let's convert to lower case
                row = row.lower()
                # let's write to output file
                f_out.write(row + "\n")
        # both files still open but file stream for f_in is exhausted
    # f_out is closed but f_in is still open
    # i could theoretically seek and start reading from the beginning of the f_in again
# both files are closed

# more on encoding
# we can't tell encoding of a file just by looking at it
# we need some information about encoding from outside

# Python supports wide range of encodings
# Python Docs: https://docs.python.org/3/library/codecs.html#standard-encodings
    