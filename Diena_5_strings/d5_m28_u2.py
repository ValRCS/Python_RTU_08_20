# Otrais uzdevums
# import string
# alphabet = string.ascii_lowercase
text = input("Lūdzu ievadiet tekstu: ")
# text=text.replace(" ","")
# print(text.replace(text, len(text)*"*"))

guess = len(text) * "*"
print(guess)

# TODO add counter for guess
# TODO add nice ASCII art for hangman

while text != guess:
    new_string =  ""
    letter=input("Lūdzu ievadiet burtu: ")
    for c, g in zip(text, guess):  # we loop through two strings at the same time
        if c == letter:
            new_string += c # not efficient for huge strings but good for smaller ones
            # above is same as new_string = new_string + c
        else:
            new_string += g
    guess = new_string # we need to update the guess so loop terminates
    print(f"Guess so far is: {guess}")

print(f"Cool word is {text}")  # or guess




# teksts = input("Ievadiet, lūdzu, tekstu: ")
# slepts_teksts = [letter if letter == " " else "*" for letter in teksts]
# print("".join(slepts_teksts))
# burts = input("Lūdzu mēģiniet uzminēt kādu burtu: ")
# minejuma_teksts = [letter if letter == " " or letter == burts else "*" for letter in teksts]
# print("".join(minejuma_teksts))