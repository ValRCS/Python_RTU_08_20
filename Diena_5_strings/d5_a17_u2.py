## Uzdevums-2
"""
Lietotājs(pirmais spēlētājs) ievada tekstu.
Tiek izvadītas tikai zvaigznītes burtu vietā. Pieņemsim, ka cipari nebūs, bet atstarpes gan var būt
Lietotājs(tātad otrs spēlētājs) ievada simbolu.
Ja burts ir tad tas burts attiecīgajās vietās tiek parādīts, visi pārējie burti paliek par zvaigznītēm.
Kartupeļu lauks -> ********* *****
ievada a -> *a****** *a***
Principā tas ir labs iesākums karātavu spēlei.
"""
 
user_text = input("Player 1, please enter your text: ")
user_text_solved = '*' * len(user_text)
 
print(f"Text to find out: {user_text_solved}")
 
tries = 0
MAX_TRIES = 7
while True:
    guess = input("Player 2, enter your guess: ")[:1] # a bit safer than [0]
    for idx, c in enumerate(user_text): # if we need index in for loop we use enumerate it starts with 0
        if guess == c:
            user_text_solved = user_text_solved[:idx] + guess + user_text_solved[idx + 1:]
    print(f"Result : {user_text_solved}")
    if not '*' in user_text_solved:
        print(f"Congratulations! Final text: '{user_text_solved}'")
        break
    tries += 1
    print(f"Tries so far {tries}")
    if tries >= MAX_TRIES:
        print(f"Sorry you lost too many tries -> {tries}")
        break



# Uzrakstīt programmu teksta simbola atpazīšanai
# text = input("Ievadiet tekstu: ")
# print(text)
# for c in text:
#     if c == " ":
#         print(" ", end="")
#     else:
#         print("*", end="")

# print()
# guess = input("Uzminiet simbolu ")
# print(guess)
# for c in text:
#     if c == " ":
#         print(" ", end="")
#     elif c == guess:
#         print(c, end="")
#     else:
#         print("*", end="")