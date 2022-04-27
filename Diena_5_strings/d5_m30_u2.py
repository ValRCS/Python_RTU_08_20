# Task No.2
###
 
# text_entry = input("Enter some sentence: ")
# new_text_entry = ""
# for char in text_entry:
#     if char == " ":
#         new_text_entry += " "
#     else:
#         new_text_entry += "*"
 
# print(new_text_entry)
 
# # we could write a loop around this code  
# letter_input = input("Enter a letter: ")
# letter_in_entry = ""
# for char in text_entry:
#     if char == letter_input:
#         letter_in_entry += letter_input
#     elif char == " ":
#         letter_in_entry += " "
#     else:
#         letter_in_entry += "*"
# print(letter_in_entry)

# Task 2, text recognition, a bit differently and with some additions
from os import system, name  # cls the terminal for task 2
print("\nTask 2 - Teksta simbolu atpazīšana, MK II")

input_text = input("Ievadiet tekstu: ").lower()
# we check for operating system and clear the terminal
if name == "nt" or name == "dos":
    system("cls")
else:
    system("clear")
guesses = ""
errors = 0
alphabet = "aābcčdeēfgģhiījkķlļmnņopqrsštuūvwxyzž"
stars = str().join("*" for c in alphabet) # "*" * len(alphabet)	
translator_table = str().maketrans(alphabet, stars)
result_text = input_text.translate(translator_table)
while True:
    input_char = input(f" [{result_text}] :? ")[:1]
    # 1 - exit chance, surrender
    if input_char == "1":
        print(f"Padodos!\n\n [{input_text}]")
        break
 
    # 2 - input unknown char, not from valid alphabet
    elif input_char not in alphabet and input_char not in guesses:
        print("Un no kādas valodas ir tas?\n")
 
    # 3 - input existing guess, let's not count this as a try
    elif input_char in guesses:
        print("Šo jau jūs minējāt ...\n")
 
    # 4 - input new guess, bad one
    elif input_char not in input_text:
        errors += 1
        guesses += input_char
        alphabet = alphabet.replace(input_char, "")
        stars = str().join("*" for c in alphabet)
        print(f"Kļūdas: {errors}! Tāds burts te nav!\n")
 
    # 5 - input new guess, a good one
    elif input_char in input_text:
        guesses += input_char
        alphabet = alphabet.replace(input_char, "") # in effect we remove the char from alphabet
        stars = str().join("*" for c in alphabet)
        translator_table = str().maketrans(alphabet, stars)
        result_text = input_text.translate(translator_table)
        print("Lieliski, pareizi atminēts burts!\n")
        if "*" not in result_text:
            print(f" [{result_text}]\nApsveicu! Jūs atminējāt tekstu ar {len(guesses)} mēģinājumiem un {errors} kļūdām!")
            break
 
    # 6 - shouldn't ever occur, buuuuuuuut ....
    else:
        print("Apsveicu, Jūs atradāt kļūdu programmā! :)")
        break