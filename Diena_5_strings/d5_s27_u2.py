# 2.uzdevums
# string_to_guess = input("Please enter string to guess:")
# for c in string_to_guess:
#     if c != " ":
#         print("*", end="")
#     else:
#         print(c, end="") # here c would be whitespace
# print("\n")

# player_guess = input("Input symbol to open:")

# for c in string_to_guess:
#     if player_guess == c:
#         print(player_guess, end="")  # c would work as well
#     elif c == " ":
#         print(c, end="")
#     else:
#         print("*", end="")
# print("\n")

text = input("Ievadiet kādu tekstu:\n")
allways_show_symbols = ' 123456890'
symbol = 'start'
while symbol != 'exit': # TODO check whether text != new_text
    new_text = ''
    # so we need to comprare the old guess here
    for i in range(len(text)): # šajā ciklā izveido new_text, kas saturēs doto simbolu un zvaigznītes
        if text[i] == symbol or text[i] in allways_show_symbols:
            new_text += text[i]
        elif text[i] == symbol.upper(): # pārbauda arī lielo burtu, ja ievadīts mazais...
            new_text += symbol.upper()
        elif text[i] == symbol.lower(): # ...un mazo, ja ievadīts lielais
            new_text += symbol.lower()
        else:
            new_text += '*'
    print(new_text)
    symbol = input('Ievadiet burtu, ko vajag parādīt; vai ievadiet "exit", lai beigtu spēli: ')