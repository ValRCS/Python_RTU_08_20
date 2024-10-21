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
for ch in player1_str: # for each character in player1_str
    if ch != ' ':
        a = '*'
    else:
        a = ch
    star_str += a
print("Slēptais teksts: " + star_str)
 
guessed_str = ''
player2_guess = input("Ievadiet lūdzu simbolu ->")
# here we could check the length of player2_guess
print(f"Pārbaudam simbolu {player2_guess}")
# for i in range(len(player1_str)):
#     if player2_guess == player1_str[i]:
#         guessed_str += player1_str[i]
#     elif player1_str[i] == ' ':
#             guessed_str += ' '
#     else:
#          guessed_str += '*'
# we do not have to use range to iterate through the string
for ch in player1_str: # so we go through the original string one by one
    # we have three possible cases
    # one is when the character is the same as the one guessed
    if ch == player2_guess: 
        guessed_str += ch # then we add the character to the guessed string
    elif ch == ' ': # we have space
        guessed_str += ' ' # then we add space to the guessed string
    else:# otherwise we add a star
        guessed_str += '*' 
print(f"Ievadītais simbols {player2_guess} tekstā "+ guessed_str)