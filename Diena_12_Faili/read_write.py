# # # # # # # # # # # # # # Reading and writing files
# # # # # # # # # # # # # # https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# # # # # # # # # # # # # # https://realpython.com/read-write-files-python/
# # # # # # # # # # # # # # file - set of continuos bytes for storing data - various formats
# # # # # # # # # # # # # # libraries for many common formats (CSV, JSON, etc)
# # # # # # # # # # # # # # plain text files - encodings and line endings could be different
# # # # # # # # # # # # # # usually we have Unicode today (encoding using UTF-8)
# # # # # # # # # # # # # # creating file object (file stream)
# # # # # # # # # # # # # # closing file automatically with with contextcd
import os
# import string  # useful string constants
# from datetime import datetime as dt  #datetime has datetime submodule(klase)
# from pathlib import Path # this is newer for path manipulation

print(os.getcwd()) # current working directory

# # # # # # # # # # # # # # # # with - context manager
# path = os.path.join(os.getcwd(), 'Diena_12_Faili', 'frost.txt')
# print(path)  # this is absolute path to file - unique for each file
# # # # # # # also absolute path using newer Path library class
# # also_path = Path().resolve() / 'Diena_12_Faili' / 'frost.txt'
# # print(also_path) # this is absolute path to file - unique for each file

# # # # # # # # # # # # # # using absolute path and manual file closing.. two things we usually want to avoid
# fstream = open('C:/Users/val-wd/Github/Python_RTU_08_20/Diena_12_Faili/frost.txt') 
# # fstream = open(path) # we open a file stream
# # text = fstream.read() # read all of the stream into string variable
# # # # # problem is that close might not be called or we forget to close it
# # fstream.close() # very important to close the file as quickly as possible
# # # # # we can start working with the string from the file
# # print(text[:100])  # first 100 chars
# # print(text[-100:]) # last 100 chars

# # # # we can use context manager to open and close file automatically
# # # path could be string or Path object
# # with open(path) as fstream:  # fstream could be called anything
# #     # start block where file is open and we can access the stream as fstream
# #     text = fstream.read() # we read everything into a string
# #     # file is still open here
# # # file is closed automatically here
# # print(text[:250])  # printing first 250 chars

# # # # for advanced users
# # # # we can make our own with context managers
# # # # https://stackoverflow.com/questions/1984325/explaining-pythons-enter-and-exit


# # # # # # # # # # # # # # we use with to guarantee closing of files
# # # # # # # # # # ## Absolute path will be different for pretty much everyone (different user name for one)
# # # # # # # # # # # Diena_12_Faili\frost.txt
# # # # # # # # # # # C:\Users\liga\Github\Python_RTU_08_20\Diena_12_Faili\frost.txt
# # # # # # # # # # # with open('C:/Users/liga/Github/Python_RTU_08_20/Diena_12_Faili/frost.txt') as f:
# # # # # # # # # # # on Windows \ needs to be escaped as \\ because used for \n \t etc
# # # # # with open("C:\\Users\\liga\\Github\\Python_RTU_08_20\\Diena_12_Faili\\frost.txt") as f: # f could be fstream etc
# # # # #     print(f.read()) 
# # # # #     # file is still open here
# # # # # # file is closed already
# # # # # # # # # # # #       # create a file object, default is read mode


# # # relative path might not be unique for each user
# # # depends on current working directory
print(os.getcwd())
relative_path = 'Diena_12_Faili/frost.txt'  # if we are in our project root
print(relative_path)

# with open(relative_path) as f:
#     print(f.read())
# i could have opened the file without context manager
# fstream = open(relative_path, 'r') # we open a file stream r is default not required
# text = fstream.read() # read into string
# fstream.close() # very important to close the file as quickly as possible
# much safer to use context manager
print(os.getcwd())
os.chdir("Diena_12_Faili") # so we change our working directory to one level deeper
print(os.getcwd())
relative_path = 'frost.txt'
with open(relative_path) as fstream:  # fstream could be called anything
    # start block where file is open and we can access the stream as fstream
    text = fstream.read() # we read everything into a string
    # we will see there are exceptions when working with trully big files
    # important point stream is at the end of the file here
    # if we want to read again we need to reset the stream
    # this is rarely needed but possible
    # fstream.seek(0) # we reset the stream to the beginning of the file
    # i could read the file stream again here
    # why? typicall file operations are read once and then closed
    # file operations are slow compared to memory operations

    # file is still open here
# file is automatically closed here
print(text[:100])  # first 100 chars

# again we could use absolute path
# absolute_path = "D:\\Github\\Python_RTU_08_20\\Diena_12_Faili\\frost.txt"
# with open(absolute_path) as fstream:  # fstream could be called anything
#     # start block where file is open and we can access the stream as fstream
#     text = fstream.read() # we read everything into a string
#     # file is still open here
# # file is automatically closed here
# print(text[:100])  # first 100 chars

# # # # # # # # # # # # Relative Paths
# # # # # # # # # # # # # if current directory is one level above our desired      
# # # # # # # # with open('Diena_12_Faili/frost.txt') as f:  # create a file object, default is read mode 
# # # # # # # #     print(f.read())
# # # # # # # # # # # # # important! f is closed here already!!! it's a good thing

# # # # # # so now frost.txt is in the same folder as this file
# # # # # # recommended way it to use context manager so file is closed automatically

# # # this is a relative path just like in the previous example
# # with open('frost.txt') as f:  # create a file object, default is read mode 
# #     print(f.read())
# # #     # file is still open here
# # # # # # file is closed already

# # # # # absolute_path = "C:\\Users\\liga\\Github\\Python_RTU_08_20\\Diena_12_Faili\\frost.txt"

# # # # # # # # # # # # one way of getting to current path is simply change in terminal where we start
# # with open('frost.txt') as f:  # create a file object, default is read mode 
# #     print(f.read())  # so keep in mind this might not be best for HUUGe files
# #     print("File is still open here")
# #     print("Trying again")
# #     print("Should have ----- new poem below -----")
# #     print(f.read())  # no error but where is the content ?
# #     print("Lets try again")
# #     # we can control where exactly in file we want to read the data from
# #     f.seek(0)  # put the needle of the record to beginning
# #     print(f.read(20)) # so read 20 symbols from current needle position
# #     print(f.read(10))  # so this is the method you can use for fine reading
# #     print(f.seek(50)) # so jumpe the needle to 50 from 0
# #     print(f.read(15)) # so read from 51 to 65
# #     # we might use this manual seek and read if we have strange format
# # # # # # # # # # # #     # f is still open here
# # # # # # # # # # # #     f.seek(0)
# # # # # # # # # # # #     res = f.read()  # not very efficient use of course , might have read it all in beggining
# # # # # # # # # # # # # # # # # # # # # # # # # f will be closed here already
# # # # # # # # # # # # # # print(f.read()) # this will be error 
# # # # # # # # # # # # # # # # # # # # # # # # without with I would have to call f.close()
# # # # # # # # # # # # print(res)

# # # # # # # # # one level up just add more ../ for more levels 
# with open("../LICENSE") as f:  # .. means one level up
#     print(f.read())

# my_files = os.listdir("./") # current dir
# print(my_files)
# # # # # # print(os.listdir("C:/"))

# # # # # # # one_level_up = os.listdir("../.")
# # # # # # # print(one_level_up)

# # # # # # # # # more modern is Path - better compatibility across OSes Windows/Mac/Linux
# # # # # # # # # so going through current directory recursively getting all objects ending with .txt and making sure they are files
# text_files = [f for f in Path(".").rglob("*.txt") if f.is_file()]  #rglob is recursive goes through subfolders
# print(text_files)
# # # # # # # # # # # # from one level up recursively all text files in my project (one level up)
# text_files = [f for f in Path("../.").rglob("*.txt") if f.is_file()]
# print(text_files)
# # # # # # # # # # # from one level up just all text files in that level just glob
# # # glob will only look in that particular directory
# # # in this case we look one folder up
# text_files = [f for f in Path("../.").glob("*.txt") if f.is_file()]
# print(text_files)

# # # # # # Path().resolve() means current working directory
# current_text_files  = [f for f in Path().resolve().glob("*.txt") if f.is_file()] 

# print(current_text_files)
# # # # # # my_path = Path("frost.txt")  # so this will create correct name on all 3 OSes
# # # # # # print(my_path)

# with open("frost.txt") as f:
#     txt = f.read()
# # file is closed here
# print(txt)
# # # # # # # # # # # # # # # # # # # list of supported encodings
# # # # # # # # # # # # # # # # # # # https://docs.python.org/3/library/codecs.html#standard-encodings
# # # # # # # # # # # # # # with open('Diena_12_Faili/frost.txt', encoding="utf-8") as f:  # create a file object
with open('frost.txt', encoding="utf-8") as f:  # create a file object
    res = f.read()  # it is quite possible that for large files we do not want it all at once
print(res)
print(res[-30:])
# # # # # # # # # # # # # # so we can load War and Peace in memory but maybe a huge log file which could be 1TB will not fit

with open("frost.txt", encoding="utf-8") as fstream:
    lines = fstream.readlines() # reads all lines defined with newline

print(lines) # this is a list
# # # # # # # # # notice how \n is present

# lets find all rows which start with letter T
# for line in lines:
#     if line.startswith("T"):
#         print(line, end="") # end="" means do not add new line

# for larger file you could do this on the fly
rows_with_t = []
with open("frost.txt", encoding="utf-8") as fstream:
    for line in fstream: # saves memory, only loads one line at a time
        if line.startswith("T"): # could be any condition
            rows_with_t.append(line)
            # print(line, end="") # end="" means do not add new line
            # printing is expensive, so we can save to list and print later
# file is closed here
print(rows_with_t)

# how to write to file
# mode can be r, w, a, x, t, b, +, U
# r - read text file
# w - write text file
# a - append to text file

from datetime import datetime # datetime has a datetime class

with open("my_may2_file.txt", mode="w", encoding='utf-8') as fout: # fout could be any name
    fout.write("Hello World\n")
    fout.write("This is fun! 😀 <- smiley - \U0001f600\n")
    # lets add a timestamp
    fout.write(f"Current time is {datetime.now()}\n")
# so each time we open file in write mode it will overwrite it

# lets add timestamp to file name - month, day, hour, minute, second
# so we will have unique file name each time
# lets use f-strings
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

file_name = f"my_file_{datetime.now():%m_%d_%H_%M_%S}.txt"
print(file_name)

with open(file_name, mode = 'w', encoding='utf-8') as fout:
    fout.write("Hello World\n")
    fout.write("This is fun! 😀 <- smiley - \U0001f600\n")
    fout.writelines(rows_with_t) # writelines writes a list of strings
    # lets add a timestamp
    fout.write(f"Current time is {datetime.now()}\n")

# i can add more text to the file with append mode
with open(file_name, mode = 'a', encoding='utf-8') as fout:
    fout.write("appended text\n")
    # i could use print to write to file as well
    print("appended text as well", file=fout) # no need for \n
    # timestamp
    print(f"Current time is {datetime.now()}", file=fout) # no need for \n
    # however print is slower than write


# how to read a large file and write to another file
out_file_name = f"filtered_{datetime.now():%m_%d_%H_%M_%S}.txt"
print(f"Will save to {out_file_name}")
# we can open two files at once they both can be very large - 1TB even
with open("frost.txt", encoding="utf-8") as fin, open(out_file_name, mode="w", encoding="utf-8") as fout:
    # lets find rows that start with "And" and save them
    for line in fin: # this will read one line at a time
        if line.startswith("And"):
            fout.write(line)

# how to find particular files in a folder?
# let's use pathlib
from pathlib import Path # this is a modern way to work with files and folders
# https://docs.python.org/3/library/pathlib.html
# let's find all text files in current folder
# we look for txt files that start with frost then have 0 or more characters and end with txt
current_text_files = [f for f in Path().resolve().glob("frost*.txt") if f.is_file()]


print(current_text_files)
# first file
print("First", current_text_files[0])
# last file
print("Last", current_text_files[-1])

# lets open first file and print first 5 lines
with open(current_text_files[0], encoding="utf-8") as f:
    for i, line in enumerate(f): # this will be useful for large files
    # we could have read all lines and then printed first 5
        if i == 5: 
            break
        print(line, end="")


# i can also fine files recursively in subfolders
# lets find all .py files in parent folder then Diena_11_modules_packages_std
# https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob
# rglob will find in subfolders as well
# .. means go up one folder
py_files = [f for f in Path("..").resolve().rglob("**/Diena_11_modules_packages_std/*.py") if f.is_file()]
print(py_files)

# lets find all files that have words LICEN  in file name going up one folder
# https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob
license_files = [f for f in Path("..").resolve().rglob("*LICEN*.txt") if f.is_file()]
print(license_files)
# # # # # # # # # # # # # # # # so with open('file.txt') as f: # we are opening file in read mode

# # # # so we use encoding to read the file in correct encoding
# # # # with open("frost.txt", encoding="utf-8") as fstream:
# # # #     lines = fstream.readlines() # reads all lines defined with newline
# # # # print(lines[-5:]) # last 5 rows

# # # # # reading everything in memory can be problematic for say 1TB files...

# # # # # # # # # # # # # # with open('Diena_12_Faili/frost.txt', encoding="utf-8") as f:  # create a file object
# with open('frost.txt', encoding="utf-8") as f:  # create a file object
#     for line in f:  # so this will work even on huge files as long as each line ends with \n
#         # now i can do something with each line
#         print(line)  # of course for big files we will not want to print
#         print(line, end="")  # of course for big files we will not want to print
#         print(line.rstrip())  # get rid of all whitespace on right side
#         print(line.rstrip("\n"))  # most precise
# # # # # # # # # # # # # #         # quick and dirty and generally okay possible last line has no \n
#         print(line[:-1]) # possibly cut last char from last line

# # # # # # # # # # # # with open('frost.txt', encoding="utf-8") as f:  # create a file object
# # # # # # # # # with open('frost.txt', encoding="utf-8") as f:  # create a file object
# # # # # # # # #     mylines = f.readlines()  # could also read a few lines with f.readline()

# # # # # # # # # print(mylines[:5])  # print first five lines

# # # # # # # # # # # # # with open('Diena_12_Faili/frost.txt', encoding="utf-8") as f:  # create a file object
# # # # # # # # # # # # #     # could also read a few lines with f.readline()
# # # # # # # # # # # # #     mylines = [line[:-1] for line in f]
# # # # # # # # # # # # #     # 99.9%  of time newline ends with /n

# # # # # # # # # # # # # print(mylines[:5])

# # # # # # # # # # # # # # # # with open('frost.txt', encoding="utf-8") as f:  # create a file object
# # # # # # # # # # # # # # # #     # could also read a few lines with f.readline()
# # # # # # # # # # # # # # # #     mylines = [line.rstrip() for line in f]
# # # # # # # # # # # # # # # #     # 99.9%  of time newline ends with /n

# # # # # # # # # # # # # # # # print(mylines[:5])

# # # # # # # # # # # # super precise only strip newlines from right side
# # # # # # # # # # # with open('frost.txt', encoding="utf-8") as f:  # create a file object
# # # # # # # # # # #     # could also read a few lines with f.readline()
# # # # # # # # # # #     mylines = [line.rstrip('\n') for line in f]
# # # # # # # # # # #     # 99.9%  of time newline ends with \n

# # # # # # # # # # # print(mylines[:5])

# needle = "roads" # what i want to find
# needle_2 = "way"
# # # # # # # # # # # # with open('Diena_12_Faili/frost.txt', encoding="utf-8") as f:  # create a file object
# with open('frost.txt', encoding="utf-8") as f:  # create a file object
#     # filtered_lines = [line for line in f if needle in line] # we can add more filters here
# # #     # we can do the same as above in long syntax
#     filtered_lines = []
#     for line in f:
#         if needle in line or needle_2 in line: # we can do more complex logic here
#             filtered_lines.append(line)
# # #     # our file stream is exhausted but still open
# # #     # f is still open here but we are at the end of this stream
# # #     # f.seek(0)  # so we can read again rare that we want this
# # #     # #
# # # file s
# print(filtered_lines)
# # # # # # # # # # # # # # # # #         # could also read a few lines with f.readline()
# # # # # # # # # # # # # #     # remember that going through file again would require f.seek(0)
# # # # # # # #     # filtered_lines_num = [(i, line.rstrip('\n'))
# # # # # # # #     #                   for i, line in enumerate(f, start=1) if "roads" in line]

# # # # # print(filtered_lines) # this is a list
# # # # # # # # # # i want to save my filtered lines
# # # # # # # # # # mode = w will overwrite old fiile, no error
# now = dt.now()  #timestampe fixed here
# print(now)
# # # # # # # # # # # timestamp in file name
# # file_path = Path("frost_cleaned_june15th.txt")
# file_path = Path(f"frost_{needle}_{now.month}_{now.day}_{now.hour}_{now.minute}_{now.second}.txt")
# # print(file_path)
# # # alternative way to get timestamp is here: https://stackoverflow.com/questions/10607688/how-to-create-a-file-name-with-the-current-date-time-in-python
# # # # # there are other ways of formatting as well
# print(file_path)
# print(file_path.stem) #without extension this is offer by Path
# print(file_path.suffix)

# # # often we want to save the file but not overwrite
# if file_path.is_file(): # this is offered by Path from standard library module pathlib
#     print(f"Sorry {file_path} exists, so not going to overwrite") # should be very rare once a year ...
# else:
#     with open(file_path, mode="w", encoding="utf-8") as fout:  # mode w will overwrite old fiile, no error
#         print(f"Writing {len(filtered_lines)} lines into {file_path}")
#         fout.writelines(filtered_lines)  # all items should have \n at the end except last one
#         print(f"Done writing {len(filtered_lines)} lines into {file_path}")
#         # file is still open I can write some more
#         fout.write("*********\n")
#         fout.write("\n".join(filtered_lines))  #here last item will not have \n
#         stripped_lines = [line.rstrip() for line in filtered_lines]
#         fout.write("\n".join(stripped_lines)) # now I will not have \n at the end of lines

# # # # # # # with open('frost.txt', encoding="utf-8") as f:  # create a file object
# # # # # # #     # filtered_lines = [line for line in f if needle in line]
# # # # # # # # # # # # # # # #     # so only get 3rd and 4th token from each line if they are actual tokens to be gotten
# # # # # # #     # filtered_lines = [line.split()[2:4] for line in f if len(line.split()) > 3]
# # # # # # #     # filtered_lines = [line.rstrip('\n')
# # # # # # #     #                   for line in f if line.startswith("And")]  # possible to use regex from re
# # # # # # #     # filtered_lines = [line for line in f if line[0] in string.digits] # so only lines which start with digits
# # # # # # # # # # # # # # # # #     #     # possible to use regex from re
# # # # # # # # # # # # # # # # #     #     filtered_lines = [line for line in f if line.startswith("And")]
# # # # # # # # # # # # # # # # #     # for more difficult filtering:
# # # # # # #     filtered_lines = []
# # # # # # #     for line in f:
# # # # # # #         if line.startswith("And"):
# # # # # # #             filtered_lines.append(line.rstrip())
# # # # # # # print(filtered_lines)
# # # # # # # # print(filtered_lines)
# # # # # # # # # # # # print(filtered_lines_num)

# # # # # # # # # # # # # # # # how to write a file?
# # # # # # # # # # # # # # # # with mode = "w" file will be created or overwritten
# # # # # # with open('frost-filtered.txt', mode="w", encoding="utf-8") as f:
# # # # # #     f.write("My filtered file\n")
# # # # # #     f.write("\n"*2)
# # # # # #     f.writelines(filtered_lines)  # remember to check if you need \n
# # # # # #     f.writelines([line+"\n" for line in filtered_lines]) # including last one
# # # # # #     f.write("*"*40+"\n")
# # # # # #     f.write("\n".join(filtered_lines)) # without newline in last line
# # # # # #     f.write("*"*40+"\n")
# # # # # #     f.write("".join(filtered_lines)) # without newline in last line
# # # # # #     print("Done with everything", file=f)  # remember by default print will add newline
# # # # # # # # # # # # # # # # # # file should be closed here, crucial for writing
# # # # # # # # # # # import datetime
# # # # # # # # # # # # mode="a" is for append to the file
# # # # now = dt.now()
# # # # file_path = "frost_cleaned_nov5.txt"
# # # # print("Now will append to ", file_path)

# # # # # different ways of writing/appending to an existing file
# # # # with open(file_path, mode="a", encoding="utf-8") as f:
# # # #     f.write("\n"+"*"*40+"\n")
   
# # # #     f.write(str(now)+"\n")  #wrote a timestamp into a file
# # # #     for n in range(5):
# # # #         f.write(f"{n}\n")
# # # #     my_list = list("abba")
# # # #     f.write("\n".join(my_list))  #another way how to add list elements in new lines
# # # #     f.write("\n")
# # # #     for line in filtered_lines:
# # # #         f.write(line+"\n")
# # # #     print("Printing into faile", file=f)  # this requires that f is open of course
# # # #     # print should be slower than write, because print formats more

# # # # # # # # # print(now.day, now.year, now.minute, now.second)
# # # # # # # # now = dt.now()
# # # # # # # # fname = f"fails_{now.month}_{now.day}_{now.hour}_{now.minute}_{now.second}.txt"

# # # # # # # # # # # fname = f"fail_{now.ctime()}.txt" # : will mess the file name
# # # # # # # # # # with open(fname, mode="w", encoding="utf-8") as f:
# # # # # # # # # #       f.writelines(filtered_lines)
# # # # # # # # # # # # # # # we will append to file
# with open(file_path, mode="a", encoding="utf-8") as f:
#     f.write("\n*******\n")
#     f.write("Starting to append\n")
#     f.write(str(dt.now())+"\n")
#     f.writelines(filtered_lines)
#     f.write("*"*40+"\n")
# # # # # # # print(file_path)
# # # # # # # # # # # # # # # open two files one for reading one for writing
# # # # # # # # # # # # # # # this could be very useful for working with very large files > more than your RAM
# # # # # # # # # # # with open('Diena_12_Faili/frost.txt', encoding="utf-8") as fin, open('frost-filtered.txt', mode="w", encoding="utf-8") as fout:

# with open('frost.txt', encoding="utf-8") as fin, open("frost_out_june15th.txt", mode="w", encoding="utf-8") as fout:
#     for line in fin:  # for each line in incoming file
#         if line.startswith("And"):  # check some condition could be very complicated
# # # #             # we could do more text processing here 
#             fout.write(line)  # write into outgoing file
# # # # so here both files will be closed and ready to be used

# # # # # # # # # # with open('frost.txt', encoding="utf-8") as fin, open('frost-yelling.txt', mode="w", encoding="utf-8") as fout:
# # # # # # # # # #     for line in fin:  # for each line in incoming file
# # # # # # # # # #         fout.write(line.upper()) # keeping also the newlines

# # # # # # # # # # # we can open files without with 
# # # # # # # # # # f = open('frost.txt', encoding="utf-8")
# # # # # # # # # # for line in f:
# # # # # # # # # #     print(line)
# # # # # # # # # # f.close() # need to close manually

# # # # # # # # # # with open('frost.txt', encoding="utf-8") as fin, open('frost-yelling.txt', mode="w", encoding="utf-8") as fout:
# # # # # # # # # #     for line in fin:  # for each line in incoming file
# # # # # # # # # #         if line[0] == "\n": # if line starts with "\n" means it is is just one character line
# # # # # # # # # #             fout.write("*"*40+"\n")
# # # # # # # # # #         else:
# # # # # # # # # #             fout.write(line.upper()) # keeping also the newlines
# # # # # # # # # # # both files are closed here


# # # # # # # # # # # we can also open files in binary 
# # # # # # # # # # with open('frost.txt', mode='rb') as fbin:
# # # # # # # # # #     res = fbin.read()

# # # # # # # # # # print(res) # usually we would not print binary because there could be unprintable symbols there..

# # # # # # # # # # # # we can convert bytes to integer (floats tooo) sākot no Python 3.2
# # # # # # # # # # my_int_big = int.from_bytes(res[:4], byteorder="big")
# # # # # # # # # # my_int_little = int.from_bytes(res[:4], byteorder="little")
# # # # # # # # # # print(my_int_big, my_int_little)


# # # # # # # # # # with open("print-tests.txt", encoding='utf-8', mode="w") as f:
# # # # # # # # # #     print(f"Just some text random stuff", file=f) 


# # # # # # # # print(f"Will combine {len(current_text_files)}")
# # # # # # # print(current_text_files)
# # # # # # # big_file_path = Path("big_text.txt")
# # # # # # # # # careful since we are going to add to itself same directory
# # # # # # # all_but_big = [f for f in current_text_files if f != big_file_path]
# # # # # # # print(len(current_text_files), len(all_but_big))

# # # # # # # with open(big_file_path, mode="w", encoding="utf-8") as fout:
# # # # # # #     fout.write(f"\n\n{now}\n\n".join([open(f, encoding="utf-8").read() for f in all_but_big]))