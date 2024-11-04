# # Reading and Writing Files and Folders
# # file - a named location on disk to store related information
# # file - a container for data
# # file - sequence of bytes - logical units of information
# # byte is a unit of digital information in computing and telecommunications
# # byte - 8 bits
# # bit - binary digit - 0 or 1

# # plain text file - human readable
# # means it can be opened with a text editor for example visual studio code, notepad utt

# # in our current folder we have frost.txt
# # this is a poem by Robert Frost
# # Two Roads - Robert Frost
# # favorite of John F. Kennedy


# # let's start with getting our current working directory
# # if something does not work it could be caused by the wrong working directory
# # so let's check it
# import os # this is a standard library module that provides a portable way of using operating system dependent functionality
# # i can print current working directory
# print(f"Current working directory: {os.getcwd()}")

# # let's get a list of all files that have *.txt extension in current working directory
# txt_files = [file for file in os.listdir() if file.endswith('.txt')]
# print(f"txt_files: {txt_files}")
# # there is a newer way using pathlib module
# from pathlib import Path # newer way to work with files and folders
# # let's use glob
# txt_files = [file for file in Path.cwd().glob('*.txt')] # looks in current working directory
# print(txt_files)
# # we could look in all sub folders by rglob
# txt_files_recursive = [file for file in Path.cwd().rglob('*.txt')] # looks in current working directory and all subdirectories
# # how many files do we have?
# print(f"txt_files_recursive: {len(txt_files_recursive)}")
# # first 5 files
# print(f"txt_files_recursive: {txt_files_recursive[:5]}")

# # similarly I could find all *.txt files in C: drive
# # could take a bit of time
# # txt_files_c_drive = [file for file in Path('C:/').rglob('*.txt')] # looks in C: drive and all subdirectories

# # absolute path versus relative path
# # C: is an absolute path points to C drive
# # Path.cwd() returns absolute path to current working directory
# # however current working directory can change relative to where the program is run

# # first file
# first_file = txt_files[0]
# print(f"first_file: {first_file}")
# # file stub
# file_stub = Path(first_file).stem
# print(f"file_stub: {file_stub}")
# # file extension
# file_extension = Path(first_file).suffix
# print(f"file_extension: {file_extension}")
# # created time
# created_time = Path(first_file).stat().st_ctime
# print(f"created_time: {created_time}") # since 1970 in milliseconds
# # human readable time
# from datetime import datetime
# created_time_human = datetime.fromtimestamp(created_time)
# print(f"created_time_human: {created_time_human}")

# print("About to open file name", first_file)
# # let's read the file
# # open the file
# with open(first_file, 'r') as file:
#     # read the file
#     file_content = file.read()
# # print the file content
# print(file_content)

# if i know the name I could open without any other imports
# with open('frost.txt') as file: # read is default mode
#     file_content = file.read() # reads into a single string
# # file gets closed automatically
# # print first 100 characters
# print(file_content[:100])
# # last 100 characters
# print(file_content[-100:])

# turns out — is not standard ascii character, so we need to specify encoding
# Ascii code table: https://www.asciitable.com/

# solution we specify encoding - usually utf-8

with open('frost.txt', encoding='utf-8') as file: # read is default mode
    content = file.read() # reads into a single string
    # file is still open here
    # typically we read the file and then close it
# file gets closed automatically here!
# print last 100 characters
print(content[-100:])

# python supports many encodings
# full list: https://docs.python.org/3/library/codecs.html#standard-encodings

# we use with to avoid forgetting to close the file
# with is so called context manager
# if I did not use with I would have to use following
# file = open('frost.txt', encoding='utf-8')
# content = file.read()
# file.close()

# now back to content
# we could get lines from content by using split on new line character
lines = content.split('\n') # split by new line character
# has an effect of removing new line character
# print how many lines in poem
print(f"Number of lines in poem: {len(lines)}")

# often we do not want to lose newlines because we will write it back
# then we use readlines method when file is open

# let's open again
with open('frost.txt', encoding='utf-8') as file: # read is default mode
    # file is a file stream object
    lines = file.readlines() # reads into a list of strings
    # stream is open but empty at this point 
    # we would have to use seek to go back to beginning but rarely needed
    # lines keep new line characters

# print first 5 lines
print(lines[:5])

# now let's filter out empty lines
# we could use list comprehension or use empty list
non_empty_lines = []
for line in lines:
    if line.strip(): # if line is not empty after stripping whitespace
        non_empty_lines.append(line)
# how many non empty lines
print(f"Number of non empty lines: {len(non_empty_lines)}")

# now let's get rid of lines which start with a number
# at this point I know all rows have some text
# let's check first character of each line
lines_starting_without_number = []
for line in non_empty_lines:
    if not line[0].isdigit(): # if line does not start with a digit
        lines_starting_without_number.append(line)

# how many lines starting without number
print(f"Number of lines starting without number: {len(lines_starting_without_number)}")
# print last 3 lines starting without number
print(lines_starting_without_number[-3:])

# now we are ready to write the poem back to a file
new_file_name = 'frost_filtered.txt'
# open the file for writing
# for that we use mode='w' flag
# w will create a new file or overwrite existing file
# again file is just a variable name for our outgoing stream
with open(new_file_name, mode='w', encoding='utf-8') as file:
    # write the lines back to the file
    for line in lines_starting_without_number:
        file.write(line) # so we write line by line, not optimal but simple