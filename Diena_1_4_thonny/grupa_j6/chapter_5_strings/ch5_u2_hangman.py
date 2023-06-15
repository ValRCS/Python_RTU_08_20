#2.uzdevums Uzrakstīt programmu teksta simbola atpazīšanai
 
#Lietotājs(pirmais spēlētājs) ievada tekstu.
#Tiek izvadītas tikai zvaigznītes burtu vietā. Pieņemsim, ka cipari nebūs, bet atstarpes gan var būt
 
#Lietotājs(tātad otrs spēlētājs) ievada simbolu. 
 
#Ja burts ir tad tas burts attiecīgajās vietās tiek parādīts, visi pārējie burti paliek par zvaigznītēm.
 
#Kartupeļu lauks -> ********* *****
#ievada a -> *a****** *a***
 
# text = input("Lūdzu ieraksti vienu vai vairākus vārdus ")
# replaced_text = ''
# for char in text:
#     if char.isalpha():
#         replaced_text += '*'
#     else:
#         replaced_text += char
# print(replaced_text)
 
# letter=input("Lūdzu ievadi simbolu ")
 
# replaced_text_1 = ''
# for char in text:
#     if char==letter:
#         replaced_text_1 += char
#     elif char.isalpha(): # so this is a letter we need to hide
#         replaced_text_1 += '*'
#     else: # space or punctuation or number or ...
#         replaced_text_1 += char       
# print(replaced_text_1)

def update_display(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "* "
    return displayed_word.strip()
 
 
def play_game():
    word = input("Player 1, enter a two-word phrase: ").upper().replace(" ", "")
    guessed_letters = set()
    max_guesses = 6
 
    print("\nLet's start the game!\n")
 
    while True:
        # display game status - statusa izvade
        print("Guessed word:", update_display(word, guessed_letters))
        print("Guessed letters:", ", ".join(sorted(guessed_letters)))
 
        guess = input("Player 2, guess a letter: ").upper()
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again!")
            continue
 
        guessed_letters.add(guess)
 
        if guess in word:
            print("Good guess!")
        else:
            max_guesses -= 1
            print("Wrong guess! You have", max_guesses, "guesses left.")
 
        if set(word) <= guessed_letters: # vajag apakškopu
            print("Congratulations! You guessed the word:", word)
            break
 
        if max_guesses == 0:
            print("Game over! The word was:", word)
            break
 
# runs the main game function
play_game()