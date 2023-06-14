# 2.uzdevums
# text = input("Ievadi tekstu: ")
# symbol = "*"
# output = ""

# for char in text:
#     if char.isalnum(): # works with Latvian letters as well
#         output = output + symbol
#     else:
#         output = output + char

# print(output) # at this point we will have output with * instead of letters or digits

# new_output = ""
# guess = input("Ievadi simbolu:")
# # TODO add check for length of guess - only 1 character allowed
# for char in text:
#     if char == guess:
#         new_output = new_output + guess
#     elif char == " ":
#         new_output = new_output + " "
#     else:
#         new_output = new_output + symbol

# print(new_output)

############
# Task - 2 #
############
 
enter_phrase = input("Enter a word or phrase: ")
# instead of input above we could have used a list of phrases and random.choice
hidden_text = ""
for c in enter_phrase:
    if c == " ":
        hidden_text += " "
    else:
        hidden_text += "*"
print("Hidden text: ", hidden_text)
 
revealed_text = hidden_text # this is not copy this is alias, shortcut
while "*" in revealed_text: # so while there are still hidden letters
    enter_letter = input("Enter a letter: ")
    temp_text = ""
    # for i in range(len(enter_phrase)):
    #     if enter_phrase[i] in [" ", enter_letter.lower(), enter_letter.upper()]:
    #         temp_text += enter_phrase[i]
    #     else:
    #         temp_text += revealed_text[i]
    # alternative solution by using zip
    # zip stops when the shortest iterable is exhausted
    for phrase_char, revealed_char in zip(enter_phrase, revealed_text):
        # if phrase_char in [" ", enter_letter.lower(), enter_letter.upper()]:
        if phrase_char.lower() == enter_letter.lower():
            temp_text += phrase_char
        else:
            temp_text += revealed_char
    revealed_text = temp_text
    print("Revealed text: ", revealed_text)

############
print("Congratulations! You guessed the entire phrase:", revealed_text)