# # Uzrakstīt programmu teksta simbola atpazīšanai
# # Lietotājs (pirmais spēlētājs) ievada tekstu.
# # Tiek izvadītas tikai zvaigznītes burtu vietā (atstarpe nav ar zvaigznīti un ciparu nav)
# # Lietotājs (otrs spēlētājs) ievada simbolu. 
# # Ja burts ir tad tas burts attiecīgajās vietās tiek parādīts, visi pārējie burti paliek par zvaigznītēm.
# # Piemērs: Kartupeļu lauks -> ********* *****. Pēc ievades: a -> *a****** *a***
import string

text_input = input('Enter word combination for guessing game: ') 
word = text_input.lower()
# for i in range(len(hidden_word)):
#     print(hidden_word)
#     hidden_word = hidden_word[0:i] + "*"
#     if ' ' in word:
#         hidden_word = hidden_word[:word.index(' ')] + ' ' + hidden_word[word.index(' ')+1:]
# print(hidden_word) 
hidden_word = ""
for c in word:
    if c == " ":
        hidden_word += c # could also use " "
    else:
        hidden_word += "*"
print(hidden_word) 
print(string.ascii_letters)

tries = 0
MAX_TRIES = 7
while hidden_word != word: # we will play forever
    guess = input("Enter a single letter: ")
    guess = guess[0].lower()
    temp_word = ""
    for c, guess_char in zip(word, hidden_word):# we go over two strings at once
        if c == guess_char or c == guess: # we check for old guess or new guess both are good 
            temp_word += c
        else:
            temp_word += "*"
    hidden_word = temp_word
    tries += 1
    print(f"your Guess so far: {hidden_word} in {tries} tries")
    if tries >= MAX_TRIES:
        print("SOrry you lost!")
        break
# while hidden_word != word:
#     guess = input("Enter a single letter: ")
#     guess = guess.lower()
#     for i in range(len(word)):
#         if word[i] == guess:
#             hidden_word = hidden_word[0:i] + guess + hidden_word[i + 1:]
#     print(hidden_word) 
# print(f"You have guessed '{word}' correclty.")