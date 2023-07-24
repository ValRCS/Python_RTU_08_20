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

# you will have to determine encoding of file yourself
# Python supports wide variety of encodings
# utf-8 is most common
# full list: https://docs.python.org/3/library/codecs.html#standard-encodings

# let's read text as lines
# for text line means sequence of characters ending with \n
# so we can use readlines() method

file_name = frost_files[0]
print("Opening file:", file_name)
with open(file_name, mode="r", encoding="utf-8") as f:
    lines = f.readlines() # line keep \n
    # file still open
# here file is closed automatically
print("File closed:", file_name)

#print first 5 lines
print(lines[:5])

# we could strip newlines if we want
stripped_lines = [line.strip() for line in lines] # or rsrtip()
print(stripped_lines[:5])

# let's keep rows which start with letter H
# we can use startswith() method
# we can use list comprehension

h_lines = [line for line in stripped_lines if line.startswith("H")]
print(h_lines[:5])

# so let's write those lines to a new file
# we can use write() method or write lines with writelines() method

# let's create a new file
# new_file_name = "data\\frost_h_lines.txt" # this is windows specific
# let's use Path instead
new_file_name = Path("data") / "frost_h_lines.txt" # so Path class overloads / operator
# print if file exists
print("File exists:", new_file_name.exists()) # could use if statement to check

print("Creating file:", new_file_name)
with open(new_file_name, mode="w", encoding="utf-8") as f: # note w mode
    # in w mode file is overwritten if it exists
    # file still open
    f.writelines(h_lines) # no newlines - not what we want most likely
    # file still open
    f.write("\n") # add newline	
    # file still open
    f.writelines([line + "\n" for line in h_lines]) # add newlines including last line
    # file still open
    # lets write some * to separate lines
    f.write("*" * 50 + "\n")
    # file still open
    f.write("\n\n".join(h_lines)) # add two newlines excluding last line
    # if we want to add newline at the end we need to add it manually
    # file still open
# here file is closed automatically
print("File closed:", new_file_name)

# let's add a timestampt to file name
# we can use datetime module
from datetime import datetime
# let's get current time
now = datetime.now()
# let's format it nicely
now_str = now.strftime("%m_%d_%H_%M") # adjust as needed could add Y and s as well
# let's create new file name
new_file_name = Path("data") / f"frost_h_lines_{now_str}.txt"
print("Creating file:", new_file_name)
with open(new_file_name, mode="w", encoding="utf-8") as f: # note w mode
    f.write("\n".join(h_lines)) # add newlines

# let's append to file
# so appending is adding to the end of file no matter what
# we can use a mode a
# let's add some more lines to new_file_name
with open(new_file_name, mode="a", encoding="utf-8") as f: # note a mode
    f.write("\n" + "*" * 50 + "\n")
    # let's add some date and time
    f.write(now.strftime("%Y-%m-%d %H:%M:%S") + "\n")

# for large files we might want to work with file line by line
# this will work even on 10TB file as long as each row/line fits in memory
# we can use for loop
# let's open first file again
with open(frost_files[0], mode="r", encoding="utf-8") as f: #mode - r is default, not really needed
    # now I have a file object f representing stream of bytes
    for row in f:
        # add your own logic to process row
        if row.startswith("H"):
            print(row.strip()) # without strip we would have 2 newlines
            # i could add this to some list or dictionary or set


# for large files we can also read and write two files at the same time

# let's let's open file_name for reading and new_file_name for writing
# theortically we could open in dual mode for writing and reading at once
# but it is not recommended
# all flags are here: https://docs.python.org/3/library/functions.html#open

# here we use \ to split long line
with open(file_name, mode="r", encoding="utf-8") as f_in:
    with open(new_file_name, mode="w", encoding="utf-8") as f_out:
        # now I have a file object f_in representing stream of bytes incoming
        # now I have a file object f_out representing stream of bytes outgoing
        for row in f_in: # here I will iterate over f_in
            # add your own logic to process row
            if row.startswith("H"): # add as many conditions as you want
                f_out.write(row)
    # here f_out is closed automatically
    # i could still do someting with f_in but I would need to seek(0) first
# here f_in is closed automatically

# so opening file in binary format is similar - we use b mode

# let's open first file again
with open(frost_files[0], mode="rb") as f: #mode - r is default, not really needed
    # now I have a file object f representing stream of bytes
    # let's read into memory
    data = f.read() # read all bytes
    # file still open
# here file is closed automatically

# let's look at first 50 bytes
print(data[:100])

# print xc4 in binary and also decimal
print(bin(0xc4), int(0xc4))
# print(bin(0xc4),) # 0b11000100
# print \x81 in binary
print(bin(0x81), int(0x81)) # 0b10000001
# but 'ā' is 257 in utf-8	
print(chr(257)) # ā
# so how utf-8 encodes Unicode see: https://www.johndcook.com/blog/2019/09/09/how-utf-8-works/
# so unicode value is from last 5 bits of first byte and last 6 bits of second byte
# so 0xc4 0x81 is 0b11000100 0b10000001
# so 0b00001000 0b00000001
# let's print int value of (0b00001000 0b00000001)
print(int(0b100000001)) # 257




