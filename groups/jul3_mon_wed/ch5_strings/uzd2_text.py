# --- Programma teksta simbola atpazīšanai ----
# player1_text = input("Text:")
# space = " "
# star = "*"
# output_text = ""
# for character in player1_text:
#     if character == space:
#         output_text += space
#     else:
#         output_text += star
# print(output_text)

# output_text = ""
# player2_char = input("Character:")
# for character in player1_text:
#     if character == space:
#         output_text += space
#     if character == player2_char:
#         output_text += player2_char
#     if character!= space and character != player2_char:
#         output_text += star
# print(output_text)


# 2
source = input("Ievadiet vārdu:").lower() # convert to lowercase for simplicity
result = ""
counter = 0
MAX_TRIES = 7
 
# create *** string
for char in source:
    if char == " ":
        result += " "
    else:
        result += "*"
        
# loop until all characters are found
while source != result:
    print(result)
    guess = input("Miniet burtu:")[0].lower() # only use the first character from input and convert to lowercase for simplicity
    counter += 1
    is_found = False
    for i, char in enumerate(source):
        if char == guess:
            result = result[:i] + guess + result[i + 1:] # not optimal for huge strings
            # here we could add a flag if we found a character
            is_found = True # we found a character at least once

    # if we didn't find a character we can print a message
    if not is_found:
        print(f"Burtu {guess} nav vārdā {source}!")
        # we could draw a hangman here...

    # finally we could check counter for max tries
    if counter >= MAX_TRIES:
        print(f"Jūs zaudējāt! Vārds bija {source}")
        break
 
print(f'Vārds {source} atminēts ar {counter} mēģinājumiem!')