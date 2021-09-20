# # # # # # Reading and writing files
# # # # # # https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# # # # # # https://realpython.com/read-write-files-python/
# # # # # # file - set of continuos bytes for storing data - various formats
# # # # # # libraries for many common formats (CSV, JSON, etc)
# # # # # # plain text files - encodings and line endings could be different
# # # # # # usually we have Unicode today (encoding using UTF-8)
# # # # # # creating file object (file stream)
# # # # # # closing file automatically with with contextcd
import os
# import string
from datetime import datetime as dt
from pathlib import Path # this is newer for path manipulation

print(os.getcwd())

# # # # # # # # with - context manager

# # # using absolute path and manual file closing.. two things we usually want to avoid
# # fstream = open('C:/Users/liga/Github/Python_RTU_08_20/Diena_12_Faili/frost.txt') 
# # text = fstream.read() # read into string 
# # fstream.close() # very important to close the file
# # print(text[:100])


# # # # # # we use with to guarantee closing of files
# # ## Absolute path will be different for pretty much everyone (different user name for one)
# # # Diena_12_Faili\frost.txt
# # # C:\Users\liga\Github\Python_RTU_08_20\Diena_12_Faili\frost.txt
# # # with open('C:/Users/liga/Github/Python_RTU_08_20/Diena_12_Faili/frost.txt') as f:
# # # on Windows \ needs to be escaped as \\ because used for \n \t etc
# # with open("C:\\Users\\liga\\Github\\Python_RTU_08_20\\Diena_12_Faili\\frost.txt") as f: # f could be fstream etc
# #     print(f.read()) 
# #       # create a file object, default is read mode

# # # Relative Paths
# # # # if current directory is one level above our desired      
# # with open('Diena_12_Faili/frost.txt') as f:  # create a file object, default is read mode 
# #     print(f.read())
# # # important! f is closed here already!!! it's a good thing
# # os.chdir("Diena_12_Faili") # so we change our working directory to one level deeper
# # # one way of getting to current path is simply change in terminal where we start
# with open('frost.txt') as f:  # create a file object, default is read mode 
#     print(f.read())  # so keep in mind this might not be best for HUUGe files
# # #     print("File is still open here")
# # #     print("Trying again")
# # #     print("Should have ----- new poem below -----")
# # #     print(f.read())  # no error but where is the content ?
# # #     print("Lets try again")
# # #     f.seek(0)  # put the needle of the record to beginning
# # #     print(f.read(20)) # so read 20 symbols from current needle position
# # #     print(f.read(10))  # so this is the method you can use for fine reading
# # #     print(f.seek(50)) # so jumpe the needle to 50 from 0
# # #     print(f.read(15)) # so read from 51 to 65
# # #     # f is still open here
# # #     f.seek(0)
# # #     res = f.read()  # not very efficient use of course , might have read it all in beggining
# # # # # # # # # # # # # # # # f will be closed here already
# # # # # print(f.read()) # this will be error 
# # # # # # # # # # # # # # # without with I would have to call f.close()
# # # print(res)

# with open("../LICENSE") as f:
#     print(f.read())

# my_files = os.listdir("./") # current dir
# print(my_files)
# print(os.listdir("C:/"))

# one_level_up = os.listdir("../.")
# print(one_level_up)

# text_files = [f for f in Path("./").rglob("*.txt") if f.is_file()]
# print(text_files)
# # from one level up recursively all text files
# text_files = [f for f in Path("../.").rglob("*.txt") if f.is_file()]
# print(text_files)
# # from one level up just all text files in that level just glob
# text_files = [f for f in Path("../.").glob("*.txt") if f.is_file()]
# print(text_files)
current_text_files  = [f for f in Path("./").glob("*.txt") if f.is_file()] 
print(current_text_files)
# my_path = Path("frost.txt")
# print(my_path)

# with open(my_path) as f:
#     txt = f.read()

# print(txt)
# # # # # # # # # # # list of supported encodings
# # # # # # # # # # # https://docs.python.org/3/library/codecs.html#standard-encodings
# # # # # # with open('Diena_12_Faili/frost.txt', encoding="utf-8") as f:  # create a file object
# with open('frost.txt', encoding="utf-8") as f:  # create a file object
#       res = f.read()  # it is quite possible that for large files we do not want it all at once
# print(res)
# # # # # print(res[-30:])
# # # # # # # so we can load War and Peace in memory but maybe a huge log file which could be 1TB will not fit

# with open("frost.txt", encoding="utf-8") as fstream:
#     lines = fstream.readlines() # reads all lines defined with newline

# print(lines) # this is a list
# notice how \n is present

# # # # # # # # so with open('file.txt') as f: # we are opening file in read mode

# # # # with open('Diena_12_Faili/frost.txt', encoding="utf-8") as f:  # create a file object
# with open('frost.txt', encoding="utf-8") as f:  # create a file object
#     for line in f:  # so this will work even on huge files as long as each line ends with \n
#         print(line)  # of course for big files we will not want to print
#         print(line, end="")  # of course for big files we will not want to print
#         print(line.rstrip())  # get rid of all whitespace on right side
#         print(line.rstrip("\n"))  # most precise
# # # # # #         # quick and dirty and generally okay possible last line has no \n
#         print(line[:-1]) # possibly cut last char from last line

# # # # with open('frost.txt', encoding="utf-8") as f:  # create a file object
# with open('frost.txt', encoding="utf-8") as f:  # create a file object
#     mylines = f.readlines()  # could also read a few lines with f.readline()

# print(mylines[:5])  # print first five lines

# # # # # with open('Diena_12_Faili/frost.txt', encoding="utf-8") as f:  # create a file object
# # # # #     # could also read a few lines with f.readline()
# # # # #     mylines = [line[:-1] for line in f]
# # # # #     # 99.9%  of time newline ends with /n

# # # # # print(mylines[:5])

# # # # # # # # with open('frost.txt', encoding="utf-8") as f:  # create a file object
# # # # # # # #     # could also read a few lines with f.readline()
# # # # # # # #     mylines = [line.rstrip() for line in f]
# # # # # # # #     # 99.9%  of time newline ends with /n

# # # # # # # # print(mylines[:5])

# # # # super precise only strip newlines from right side
# # # with open('frost.txt', encoding="utf-8") as f:  # create a file object
# # #     # could also read a few lines with f.readline()
# # #     mylines = [line.rstrip('\n') for line in f]
# # #     # 99.9%  of time newline ends with \n

# # # print(mylines[:5])

needle = "roads" # what i want to find
# # # # # with open('Diena_12_Faili/frost.txt', encoding="utf-8") as f:  # create a file object
with open('frost.txt', encoding="utf-8") as f:  # create a file object
    filtered_lines = [line for line in f if needle in line]
# # # # # # # #         # could also read a few lines with f.readline()
# # # # #     # remember that going through file again would require f.seek(0)
# # #     # filtered_lines_num = [(i, line.rstrip('\n'))
# # #     #                   for i, line in enumerate(f, start=1) if "roads" in line]

# i want to save my filtered lines
# mode = w will overwrite old fiile, no error
# now = dt.now()

# # timestamp in file name
# file_path = Path(f"frost_{needle}_{now.month}_{now.day}_{now.hour}_{now.minute}_{now.second}.txt")
# if file_path.is_file():
#     print(f"Sorry {file_path} not going to overwrite") # should be very rare once a year ...
# else:
#     with open(file_path, mode="w", encoding="utf-8") as fout:
#         print(f"Writing {len(filtered_lines)} lines into {file_path}")
#         fout.writelines(filtered_lines)

# # # # # # # #     # so only get 3rd and 4th token from each line if they are actual tokens to be gotten
# # # # #     # filtered_lines = [line.split()[2:4] for line in f if len(line.split()) > 3]
# # # # #     # filtered_lines = [line.rstrip('\n')
# # # # #     #                   for line in f if line.startswith("And")]  # possible to use regex from re
# # # # #     filtered_lines = [line for line in f if line[0] in string.digits] # so only lines which start with digits
# # # # # # # # #     #     # possible to use regex from re
# # # # # # # # #     #     filtered_lines = [line for line in f if line.startswith("And")]
# # # # # # # # #     # for more difficult filtering:
# # # # # # # #     filtered_lines = []
# # # # # # # #     for line in f:
# # # # # # # #         if line.startswith("And"):
# # # # # # # #             filtered_lines.append(line.rstrip())

print(filtered_lines)
# # # # print(filtered_lines_num)

# # # # # # # # how to write a file?
# # # # # # # # with mode = "w" file will be created or overwritten
# with open('frost-filtered.txt', mode="w", encoding="utf-8") as f:
#     f.write("My filtered file\n")
#     f.write("\n"*2)
#     f.writelines(filtered_lines)  # remember to check if you need \n
#     f.writelines([line+"\n" for line in filtered_lines]) # including last one
#     f.write("*"*40+"\n")
#     f.write("\n".join(filtered_lines)) # without newline in last line
#     f.write("*"*40+"\n")
# # # #     f.write("".join(filtered_lines)) # without newline in last line
# # # # # # # # # # file should be closed here, crucial for writing
# # # import datetime
# # # # mode="a" is for append to the file
# now = dt.now()
# with open('frost-filtered.txt', mode="a", encoding="utf-8") as f:
#     f.write("\n"+"*"*40+"\n")
   
#     f.write(str(now)+"\n")
#     for n in range(5):
#         f.write(f"{n}\n")
#     for line in filtered_lines:
#         f.write(line+"\n")

# print(now.day, now.year, now.minute, now.second)
now = dt.now()
fname = f"fails_{now.month}_{now.day}_{now.hour}_{now.minute}_{now.second}.txt"

# # # fname = f"fail_{now.ctime()}.txt" # : will mess the file name
# # with open(fname, mode="w", encoding="utf-8") as f:
# #       f.writelines(filtered_lines)
# # # # # # # we will append to file
# # # # # # # with open('frost-filtered.txt', mode="a", encoding="utf-8") as f:
# # # # # # #     f.writelines(filtered_lines)

# # # # # # # open two files one for reading one for writing
# # # # # # # this could be very useful for working with very large files > more than your RAM
# # # # with open('Diena_12_Faili/frost.txt', encoding="utf-8") as fin, open('frost-filtered.txt', mode="w", encoding="utf-8") as fout:
# with open('frost.txt', encoding="utf-8") as fin, open(fname, mode="w", encoding="utf-8") as fout:
#     for line in fin:  # for each line in incoming file
#         if line.startswith("And"):  # check some condition could be very complicated
# # # #             # we could do more text processing here 
#             fout.write(line)  # write into outgoing file
# # # # so here both files will be closed and ready to be used

# # with open('frost.txt', encoding="utf-8") as fin, open('frost-yelling.txt', mode="w", encoding="utf-8") as fout:
# #     for line in fin:  # for each line in incoming file
# #         fout.write(line.upper()) # keeping also the newlines

# # # we can open files without with 
# # f = open('frost.txt', encoding="utf-8")
# # for line in f:
# #     print(line)
# # f.close() # need to close manually

# # with open('frost.txt', encoding="utf-8") as fin, open('frost-yelling.txt', mode="w", encoding="utf-8") as fout:
# #     for line in fin:  # for each line in incoming file
# #         if line[0] == "\n": # if line starts with "\n" means it is is just one character line
# #             fout.write("*"*40+"\n")
# #         else:
# #             fout.write(line.upper()) # keeping also the newlines
# # # both files are closed here


# # # we can also open files in binary 
# # with open('frost.txt', mode='rb') as fbin:
# #     res = fbin.read()

# # print(res) # usually we would not print binary because there could be unprintable symbols there..

# # # # we can convert bytes to integer (floats tooo) sākot no Python 3.2
# # my_int_big = int.from_bytes(res[:4], byteorder="big")
# # my_int_little = int.from_bytes(res[:4], byteorder="little")
# # print(my_int_big, my_int_little)


# # with open("print-tests.txt", encoding='utf-8', mode="w") as f:
# #     print(f"Just some text random stuff", file=f) 

print(f"Will combine {len(current_text_files)}")

# careful since we are going to add to itself same directory
with open("big_text.txt", mode="w", encoding="utf-8") as fout:
    fout.write("\n\n".join([open(f, encoding="utf-8").read() for f in current_text_files]))