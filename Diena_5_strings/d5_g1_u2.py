#Player 1 input:
text_to_guess = input("Player 1, please input the text to guess! ")
guessed_so_far = ""
for i in text_to_guess:
    if i != " ":
        # guessed_so_far = guessed_so_far + "*"
        guessed_so_far += "*"
    else:
        guessed_so_far += " "
print(f"Text to guess: {guessed_so_far}") #
done = False
# while done == False:
while not done:
    if text_to_guess == guessed_so_far:
        done = True
        print("Done!")
    else:
        #get the guess from Player 2
        guess = input("Player 2, make your guess (one letter) ")
        for cut_here, c in enumerate(text_to_guess): # enumerate starts from 0
            if c == guess: 
                new_string = guessed_so_far[:cut_here] + guess + guessed_so_far[cut_here+1:] #neder, string indices must be integers
                guessed_so_far = new_string      
        print(guessed_so_far)



# text = input("Please enter some text: ")
 
# # for c in range(len(text)): no need for range here
# for c in text:
#     if c != " ":
#         print("*", end="")
#     else:
#         print(" ", end="")
 
# print("")


# guess = input("Try to guess a letter: ")
 
# for c in text:
#     if c == guess:
#         print(guess, end="")
#     elif c == " ":
#         print(" ", end="")
#     else:
#         print("*", end="")