# Uzrakstīt programmu teksta simbola atpazīšanai
# Lietotājs(pirmais spēlētājs) ievada tekstu.
# Tiek izvadītas tikai zvaigznītes burtu vietā. Pieņemsim, ka cipari nebūs, bet atstarpes gan var būt
# Lietotājs(tātad otrs spēlētājs) ievada simbolu. 
# Ja burts ir tad tas burts attiecīgajās vietās tiek parādīts, visi pārējie burti paliek par zvaigznītēm.
# Kartupeļu lauks -> ********* *****
# ievada a -> *a****** *a***
# Principā tas ir labs iesākums karātavu spēlei.
player1_str = input("Ievadiet tekstu ->")
star_str = '' # in beginning new_str is empty
for original_ch in player1_str: # for each character in player1_str
    if original_ch != ' ':
        a = '*'
    else:
        a = original_ch # original character is space
    star_str += a
print("Slēptais teksts: " + star_str)
 
# buffer = ''
# player2_guess = input("Ievadiet lūdzu simbolu ->")
# # here we could check the length of player2_guess
# print(f"Pārbaudam simbolu {player2_guess}")
# for i in range(len(player1_str)):
#     if player2_guess == player1_str[i]:
#         guessed_str += player1_str[i]
#     elif player1_str[i] == ' ':
#             guessed_str += ' '
#     else:
#          guessed_str += '*'

while player1_str != star_str: # we continue until the guessed string is the same as the original string
    player2_guess = input("Ievadiet lūdzu simbolu ->") # we ask for a character
    buffer = '' # we reset the guessed string
    for original_ch, hidden_ch in zip(player1_str, star_str): # we go through the original string
        if original_ch == player2_guess: # if the character is the same as the one guessed
            buffer += original_ch # then we add the character to the guessed string
        # elif original_ch == ' ': # if we have space
        #     buffer += ' ' # then we add space to the guessed string
        # we do not need to check for space, because we have already added it to the guessed string
        else: # otherwise we add a star
            buffer += hidden_ch # we add the hidden character
    # finally we need to assign the buffer to the guessed string
    star_str = buffer # critical otherwise we lose all the previous guesses
    print(f"Ievadītais simbols {player2_guess} tekstā "+ star_str)
# we do not have to use range to iterate through the string
# for ch in player1_str: # so we go through the original string one by one
#     # we have three possible cases
#     # one is when the character is the same as the one guessed
#     if ch == player2_guess: 
#         guessed_str += ch # then we add the character to the guessed string
#     elif ch == ' ': # we have space
#         guessed_str += ' ' # then we add space to the guessed string
#     else:# otherwise we add a star
#         guessed_str += '*' 
print(f"Ievadītais simbols {player2_guess} tekstā "+ buffer)