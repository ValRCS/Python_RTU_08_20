# Uzrakstīt programmu teksta simbola atpazīšanai
# Lietotājs(pirmais spēlētājs) ievada tekstu.
# Tiek izvadītas tikai zvaigznītes burtu vietā. Pieņemsim, ka cipari nebūs, bet atstarpes gan var būt
# Lietotājs(tātad otrs spēlētājs) ievada simbolu. 
# Ja burts ir tad tas burts attiecīgajās vietās tiek parādīts, visi pārējie burti paliek par zvaigznītēm.
# Kartupeļu lauks -> ********* *****
# ievada a -> *a****** *a***
# Principā tas ir labs iesākums karātavu spēlei.
MAX_BAD_GUESS = 5

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
bad_guess_count = 0 # initialize the number of guesses

while player1_str != star_str: # we continue until the guessed string is the same as the original string
    if bad_guess_count >= MAX_BAD_GUESS: # if we have reached the maximum number of guesses
        print("Jūs zaudējāt")
        print(f"Jūs minējāt {bad_guess_count} reizes")	
        print("Vārds bija: " + player1_str)	
        break
    player2_guess = input("Ievadiet lūdzu simbolu ->") # we ask for a character
    buffer = '' # we reset the guessed string
    for original_ch, hidden_ch in zip(player1_str, star_str): # we go through the original string
        if original_ch == player2_guess: # if the character is the same as the one guessed
            buffer += original_ch # then we add the character to the guessed string
        else: # otherwise we add a star
            buffer += hidden_ch # we add the hidden character
            
    star_str = buffer # critical otherwise we lose all the previous guesses
    # let's check if we should increment the bad_guess_count
    if player2_guess not in player1_str: #not the most efficient way but okay for short strings
        bad_guess_count += 1
    print(f"Ievadītais simbols {player2_guess} tekstā "+ star_str)

# check winner
if bad_guess_count < MAX_BAD_GUESS:
    print("Jūs uzvarējāt")
    print(f"Jūs minējāt {bad_guess_count} reizes")	
    print("Vārds bija: " + player1_str)

# TODO 
# idejas uzlabojumiem
# pielikt kopējo skaitītāju, cik reizes minēts
# rādīt, cik reizes vēl var minēt
# radīt vizuāli cilvēciņu, vai kā savādāk
# vēlāk varētu veidot spēli cilvēks pret datoru
# dators piedāvātu vārdu no saraksta, vai no kāda ārēja resursa (tīmekļa)
# iespējams arī var paņemt vārdus no kāda teksta faila (to arī skatīsimies citā nodarbībā)


