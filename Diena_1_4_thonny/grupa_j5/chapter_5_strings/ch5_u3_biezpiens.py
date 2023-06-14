############
# Task - 3 #
############
 
phrase = input("Ievadiet savu tekstu: ")
nav_phrase = "nav"
slikt_phrase = "slikt"
replacement_text = "ir lab"
slikt_len = len(slikt_phrase)
nav_index = phrase.find(nav_phrase)
slikt_index = phrase.rfind(slikt_phrase)

 
if nav_index == -1 or slikt_index == -1 or nav_index > slikt_index:
    # crucially nav_index > slikt_index is needed to check if nav is before slikts
    print(phrase)
else: 
    new_phrase = phrase[:nav_index] + replacement_text + phrase[slikt_index+slikt_len:]
    # alternative with f-strings
    also_new_phrase = f"{phrase[:nav_index]}{replacement_text}{phrase[slikt_index+slikt_len:]}"
    print(new_phrase)
    print(also_new_phrase)