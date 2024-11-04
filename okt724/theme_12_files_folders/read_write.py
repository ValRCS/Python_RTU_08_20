# Reading and Writing Files and Folders
# file - a named location on disk to store related information
# file - a container for data
# file - sequence of bytes - logical units of information
# byte is a unit of digital information in computing and telecommunications
# byte - 8 bits
# bit - binary digit - 0 or 1

# plain text file - human readable
# means it can be opened with a text editor for example visual studio code, notepad utt

# in our current folder we have frost.txt
# this is a poem by Robert Frost
# Two Roads - Robert Frost
# favorite of John F. Kennedy


# let's start with getting our current working directory
# if something does not work it could be caused by the wrong working directory
# so let's check it
import os # this is a standard library module that provides a portable way of using operating system dependent functionality
# i can print current working directory
print(f"Current working directory: {os.getcwd()}")

# let's get a list of all files that have *.txt extension in current working directory
txt_files = [file for file in os.listdir() if file.endswith('.txt')]
print(f"txt_files: {txt_files}")
# there is a newer way using pathlib module
from pathlib import Path # newer way to work with files and folders
# let's use glob
txt_files = [file for file in Path.cwd().glob('*.txt')] # looks in current working directory
print(txt_files)
# we could look in all sub folders by rglob
txt_files_recursive = [file for file in Path.cwd().rglob('*.txt')] # looks in current working directory and all subdirectories
# how many files do we have?
print(f"txt_files_recursive: {len(txt_files_recursive)}")
# first 5 files
print(f"txt_files_recursive: {txt_files_recursive[:5]}")

# similarly I could find all *.txt files in C: drive
# could take a bit of time
# txt_files_c_drive = [file for file in Path('C:/').rglob('*.txt')] # looks in C: drive and all subdirectories

# absolute path versus relative path
# C: is an absolute path points to C drive
# Path.cwd() returns absolute path to current working directory
# however current working directory can change relative to where the program is run

# first file
first_file = txt_files[0]
print(f"first_file: {first_file}")
# file stub
file_stub = Path(first_file).stem
print(f"file_stub: {file_stub}")
# file extension
file_extension = Path(first_file).suffix
print(f"file_extension: {file_extension}")
# created time
created_time = Path(first_file).stat().st_ctime
print(f"created_time: {created_time}") # since 1970 in milliseconds
# human readable time
from datetime import datetime
created_time_human = datetime.fromtimestamp(created_time)
print(f"created_time_human: {created_time_human}")

print("About to open file name", first_file)
# let's read the file
# open the file
with open(first_file, 'r') as file:
    # read the file
    file_content = file.read()
# print the file content
print(file_content)