# we can go over string and build a new string

text = "Hello World"
buffer = ""
for character in text:
    if character == 'o':
        buffer = buffer + '0'
    else:
        buffer = buffer + character
    print(buffer)

# this approach could help you solve 2nd task from Diena_1_4_thonny\grupa_j5\chapter_5_strings\string_buffer.py
print("Finished")
print(buffer)