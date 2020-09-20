# Reading and writing files
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://realpython.com/read-write-files-python/
# file - set of continuos bytes for storing data - various formats
# libraries for many common formats (CSV, JSON, etc)
# plain text files - encodings and line endings could be different
# creating file object (file stream)
# closing file automatically with with context
import os
print(os.getcwd())

with open('frost.txt') as f:  # create a file object
    print(f.read())
# f will be closed here already

# list of supported encodings
# https://docs.python.org/3/library/codecs.html#standard-encodings
with open('frost.txt', encoding="utf-8") as f:  # create a file object
    print(f.read())

with open('frost.txt', encoding="utf-8") as f:  # create a file object
    for line in f:
        print(line)

with open('frost.txt', encoding="utf-8") as f:  # create a file object
    mylines = f.readlines()  # could also read a few lines with f.readline()

print(mylines[:5])

with open('frost.txt', encoding="utf-8") as f:  # create a file object
    # could also read a few lines with f.readline()
    mylines = [line[:-1] for line in f]
    # 99.9%  of time newline ends with /n

print(mylines[:5])

with open('frost.txt', encoding="utf-8") as f:  # create a file object
    # could also read a few lines with f.readline()
    mylines = [line.rstrip() for line in f]
    # 99.9%  of time newline ends with /n

print(mylines[:5])

# super precise
with open('frost.txt', encoding="utf-8") as f:  # create a file object
    # could also read a few lines with f.readline()
    mylines = [line.rstrip('\n') for line in f]
    # 99.9%  of time newline ends with \n

print(mylines[:5])
