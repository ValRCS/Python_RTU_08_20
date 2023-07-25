# so reading files in binary mode means we get raw bytes, not strings
# let's use Path and we will read the file in binary mode

from pathlib import Path
# file name will be stopping_frost.txt again
file_name = Path('data') / "stopping_frost.txt" 
print(file_name) 

# So above exampe shows how you Path overloads / operator
# we will still use the with statement
# but we will open the file in binary mode

with open(file_name, mode='rb') as file: # again file is arbitrary name
    # we will read the file in binary mode
    byte_data = file.read() # we will read the file in binary mode
    # file is stil open
# file is closed now

# we will print the type of byte_data
print(type(byte_data)) # <class 'bytes'>
# let's print first 50 bytes
print(byte_data[:50]) # b'Whose woods these are I think I know.\nHis house is'

# let's look at next 50 bytes
print(byte_data[50:100]) # 
# for Latvian symbols we see that each symbol is represented by 2 bytes
# utf-8 is variable length encoding
# for ASCII it uses only 1 byte
# for most languages it uses 2 bytes
# for Emoji it uses 4 bytes

# let's decode the bytes into string if we know the encoding
print(byte_data[50:100].decode('utf-8')) # Whose woods these are I think I know.

# let's look at binary values of  \xc4 and \x81
# \x is used to represent hexadecimal values
print(bin(0xc4), int('c4', 16)) # 0b11000100 196
# how about \x81
print(bin(0x81), int('81', 16)) # 0b10000001 129
# now we know it is ā
# its unicode value is 257
print(ord('ā'), chr(257)) # ā

# so how do we go from 196 and 129 to 257 ?
# more in blog: https://www.johndcook.com/blog/2019/09/09/how-utf-8-works/
# Unicode Transformation Format (UTF) is a character encoding standard

# so let's get last 5 bits from 196 and last 6 bits from 129
# 196 is 11000100
# 129 is 10000001
# so binary value of 257 is 100000001
# convert 257 to binary
print(bin(257)) # 0b100000001

# we also have byte array
# let's create a byte array
byte_array = bytearray(byte_data)
# let's print first 50 bytes
print(byte_array[:50]) # b'Whose woods these are I think I know.\nHis house is'

# so what's the difference between bytes and bytearray?
# bytes are immutable
# bytearray are mutable # so sort of like list of bytes
# some byte_array methods
# append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
# very similar to list methods
# but there is also fromhex method