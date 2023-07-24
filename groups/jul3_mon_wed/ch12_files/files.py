# reading and writing text files

# what is a file?
# essentially file is a sequence of bytes
# it could be text file or binary file
# represented in a storage medium or memory
# we can think of file as stream of bytes

# text file is a sequence of characters - encoding is important
# binary file is a sequence of bytes - encoding is not important
# technially we could read any text file as binary file
# and permissions also could be issue

# we will focus on text files
# we want to open
# read
# write
# append - files you do not insert in the middle or start!
# close

# we will use open() function
# it returns a file object
# generally we do not want to worry about closing files manually
# so we use with statement - it will close file for us
# with is so called context manager
# we use with when we want something to happen before and after some action

# first we need to find out our current working directory
# we can use os module for that
import os
print(os.getcwd()) # get current working directory

# there is more modern module for working with files - pathlib
# we will use Path class from pathlib
from pathlib import Path
# so again let's check current working directory
print(Path.cwd()) # get current working directory
# Path provides OS independent way of working with files and directories

# let's check if there is a data folder in current working directory
# we can use exists() method
print("data folder exists in current dir?", Path("data").exists()) # True

# let's check what text files are in data folder
# we can use glob() method - it returns generator - so might need to convert to list
text_files = list(Path("data").glob("*.txt"))
# let's print first 5 files
print(text_files[:5]) # [WindowsPath('data\\file1.txt'), WindowsPath('data\\file2.txt')]
# let's sort files by modification time
# we can use stat() method - it returns os.stat_result object

# let's sort files by modification time

text_files = sorted(text_files, key=lambda f: f.stat().st_mtime)
# let's print first 5 files and their modification times
for f in text_files[:5]:
    # let's print file name and modification time in human readable format
    # convert st_mtime to datetime object
    # then convert datetime object to string
    # then print
    print(f, Path(f).stat().st_mtime, Path(f).stat().st_mtime_ns)
    # convert ns to normal date time
    # TODO look at datetime module

# of coure we could sort by name, size, etc

# let's find out text files that have frost in their name

frost_files = [f for f in text_files if "frost" in f.name]
# i could have use glob() method again
# frost_files = list(Path("data").glob("*frost*.txt"))

# there is also rglob for recursive search through subfolder and subsubfolders etc

# so Path objects offer various methods for working with files and directories
# so stem, suffix, parent, name, etc#
# let's print stem, suffix, parent, name for frost_files
for f in frost_files:
    print(f.stem, f.suffix, f.parent, f.name)
# we could have done this with split() method but Path is safer and supports all OS

# so we will open first of frost_files
# first let's print absolute of first file
print(frost_files[0].absolute())
# absolute means unique path to file in this case
# relative would be relative to current working directory
# python takes both absolute and relative paths
# for projects across multiple computers we want to use relative paths

# so let's open first file
# we will get an error because we have utf-8 encoding !
# with open(frost_files[0], mode="r") as f: #mode - r is default, not really needed
#     # now I have a file object f representing stream of bytes
#     # i could read all of them at once
#     text = f.read() 
#     text_again = f.read() # nothing to read!
#     # file still open 
# # here file is closed automatically

# # let's print first 50 characters
# print(text[:50])
# print("*" * 50)
# # let's print first 50 characters again
# print(text_again[:50])

# # let's read file again using encoding for utf-8
with open(frost_files[0], mode="r", encoding="utf-8") as f: #mode - r is default, not really needed
#     # now I have a file object f representing stream of bytes
#     # i could read all of them at once
    text = f.read()
    # if we really want to read again we could use seek() method
    # rarely used - we usually read once
    f.seek(0) # reset file pointer to beginning of file
    # we could have seeked at asome other position as well
    # possibly this could be useful for binary files and some rare encoding issues
    text_again = f.read() # nothing to read without seek(0)!
    # file still open
# # here file is closed automatically

# # let's print first 50 characters
print(text[:50])
print("*" * 50)
# # let's print first 50 characters again
print(text_again[:50])
# so we worked with file stream and it was exhausted after first read
# analogy with record player - we can only play record once
# we could play it again if we rewind it
# hard drives we have heads to read data - so we can read again


