###################################################
# Uzdevums:

wildcard = "*"
blank = " "
text = input("Ievadiet minamo vārdu ")
t_number=int(len(text))
# new_text = t_number*"*"
text_buffer = ""
for i in text: # i go through text one character at a time
    if i == blank:
        print(blank, end="")
        text_buffer += blank # same as text_buffer = text_buffer + " "
    else:
        print(wildcard, end="")
        text_buffer += wildcard
print() # new line is automatically added
print(text_buffer)
# print(new_text)
char = input("Ievadiet burtu ")
for i in text:
    if i != blank and i != char:
        i = "*"
    print(i, end="")
######################################################