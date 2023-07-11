## 2. "Uzrakstīt programmu teksta simbola atpazīšanai"
# Lietotājs(pirmais spēlētājs) ievada tekstu.
#
# Tiek izvadītas tikai zvaigznītes burtu vietā. Pieņemsim, ka cipari nebūs, bet atstarpes gan var būt
#
# Lietotājs(tātad otrs spēlētājs) ievada simbolu.
#
# Ja burts ir tad tas burts attiecīgajās vietās tiek parādīts, visi pārējie burti paliek par zvaigznītēm.
#
# Kartupeļu lauks -> ********* *****
#
# ievada a -> *a****** *a***
#
# Principā tas ir labs iesākums karātavu spēlei.
 
# print("Enter a text")
# some_text = input()
# star = "*"
# space = " "
# hidden_text=""

# for letter in some_text:
#     if letter == space: # alternative if letter.isspace(): # it would work with tabs and newlines as well
#         hidden_text += space # same as hidden_text = hidden_text + space
#     else: # letter != space:
#         hidden_text += star # same as hidden_text = hidden_text + star
 
 
# print(hidden_text)
 
# hidden_text2 = ""
 
# print("Enter a letter")
 
# input_letter = input()
# for letter in some_text:
#     if letter == input_letter:
#         hidden_text2 += letter # same as hidden_text2 = hidden_text2 + letter
#     elif letter == " ":
#         hidden_text2 += space # same as hidden_text2 = hidden_text2 + space
#     else:
#         hidden_text2 += star # same as hidden_text2 = hidden_text2 + star
 
# print(hidden_text2)

#############################################################
#############################################################
# 2. Uzrakstīt programmu teksta simbola atpazīšanai ??? STUB
from getpass import getpass # from stdlib import getpass

# getpass hides the input
# useful if we have to input a password
txt = getpass("Please input a string to guess: ")
 
print("Please take a guess: "+"*"*len(txt))
 
guesses = ' ' # we need whitespace for cases when user inputs space
 
turns = 20
 
while turns > 0:
    failed = 0
    for char in txt:
        if char in guesses:
            print(char, end = "")
        else: 
            print("*", end="")
            failed += 1
    if failed == 0:
        print("You Win")
 
        print("The word is: ", txt)
        break
    print()
    guess = input("Guess a Char: ")
    
    if guess not in txt and guess not in guesses:
        turns -= 1
        print("Wrong")
        print(f"You have {turns} left!")
        # here we could add drawing of hangman, activating leds, playing sounds etc
        if turns == 0:
            print("You Lost")
    if guess not in guesses: # code would work without this if but guesses would grow with each turn
        guesses += guess
    else:
        print(f"You have already guessed {guess}")