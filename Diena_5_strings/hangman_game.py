# write a hangman game that picks a random word from a list of words and then lets the user guess one letter at a time.

# The user gets 6 guesses and loses a guess every time they guess incorrectly.

# If the user guesses the same letter twice, they don’t lose a guess.

# If the user guesses all the letters correctly before they run out of guesses, they win.

# If the user runs out of guesses before they guess the word, they lose.

# At the end of the game, the program should reveal the word to the user.

# The program should let the user play again if they want to.

# The program should let the user choose a difficulty level at the beginning of the game.

# The program should let the user choose a category at the beginning of the game.

# The program should let the user choose a word length at the beginning of the game.

# let's start with a list of words

words = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "lemon", "pear", "peach", "grape", "strawberry", "blueberry", "raspberry", "blackberry", "watermelon", "apricot", "avocado", "coconut", "cantaloupe", "fig", "guava", "honeydew", "jackfruit", "lychee", "papaya", "pineapple", "pomegranate", "tomato", "tangerine", "grapefruit", "plum", "nectarine", "persimmon", "quince", "raisin", "currant", "cranberry", "date", "durian", "elderberry", "gooseberry", "grape", "huckleberry", "jambul", "kumquat", "litchi", "mulberry", "olive", "pomelo", "rambutan", "starfruit", "tamarind", "yuzu", "zucchini", "artichoke", "asparagus", "aubergine", "broccoli", "brussels sprouts", "cabbage", "carrot", "cauliflower", "celery", "chili pepper", "corn", "cucumber", "eggplant", "garlic", "ginger", "green bean", "kale", "lettuce", "mushroom", "onion", "pea", "potato", "pumpkin", "radish", "spinach", "sweet potato", "tomato", "turnip", "yam", "zucchini", "acorn squash", "butternut squash", "cucumber", "eggplant", "zucchini", "pumpkin", "summer squash", "tomato", "potato", "sweet potato", "yam", "beet", "carrot", "celery", "corn", "cucumber", "eggplant", "garlic", "ginger", "green bean", "kale", "lettuce", "mushroom", "onion", "pea", "potato", "pumpkin", "radish", "spinach", "sweet potato", "tomato", "turnip", "yam"]

# let's choose a random word from the list

import random

word = random.choice(words)

# let's create a list of underscores that is the same length as the word

cover = ["_"] * len(word)

# let's create a list of letters that the user has guessed

guessed = []

# let's create a variable to keep track of the number of guesses

guesses = 6

# let's create a variable to keep track of whether the user has won or lost

won = False

# let's create a variable to keep track of whether the user wants to play again

again = True

# let's start the game

while again:
    
        # let's reset the variables
    
        word = random.choice(words)
    
        cover = ["_"] * len(word)
    
        guessed = []
    
        guesses = 6
    
        won = False
    
        # let's start the game
    
        while guesses > 0 and not won:
    
            # let's print the word with the guessed letters revealed
    
            print(" ".join(cover))
    
            # let's ask the user to guess a letter
    
            guess = input("Guess a letter: ")
    
            # let's check if the user has already guessed the letter
    
            if guess in guessed:
    
                print("You already guessed that letter.")
    
            # let's check if the letter is in the word
    
            elif guess in word:
    
                print("That letter is in the word.")
    
                # let's reveal the letter in the cover
    
                for i in range(len(word)):
    
                    if word[i] == guess:
    
                        cover[i] = guess
    
            # let's check if the letter is not in the word
    
            else:
    
                print("That letter is not in the word.")
    
                # let's subtract a guess
    
                guesses -= 1
    
            # let's add the letter to the list of guessed letters
    
            guessed.append(guess)
    
            # let's check if the user has won
    
            if "_" not in cover:
    
                won = True
    
        # let's print the word with the guessed letters revealed
    
        print(" ".join(cover))
    
        # let's check if the user has won
    
        if won:
    
            print("You won!")
    
        # let's check if the user has lost
    
        else:
    
            print("You lost!")
    
        # let's ask the user if they want to play again
    
        again = input("Do you want to play again? (y/n) ") == "y"   


