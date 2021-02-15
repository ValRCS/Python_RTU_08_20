# 2nd_Task
 
word = input("1st player enter your word: ")
hid_word = ""
for c in word:
    if c.isalpha():
        hid_word += "*"
    elif c.isdecimal():
        hid_word += "0"
    else:
        hid_word += " "
    # if c == " ":
    #     hid_word += " "
    # else:
    #     hid_word += "*"
print(hid_word)
 
letter = input("2nd player enter your letter: ")
guess = ""
for c in word:
    if c == " ":
        guess += " "
    elif c == letter:
        guess += letter
    elif c in "0123456789": # so same as c.isdecimal() but we can customize this!
        guess += "0"
    else:
        guess += "*"
print(guess)