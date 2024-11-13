import random
 
# let's make a function that returns a list of names from a file
def get_names_from_file(file_path, encoding="utf-8"):
    with open(file_path, "r", encoding=encoding) as file:
        content = file.read()
    names = content.splitlines()
    return names

# # Latvian names from txt file:
# with open("data/latvian_names.txt", "r", encoding="utf-8") as file:
#     # Your code to read from the file
#     content = file.read()
#     latvian_names = content.splitlines()


# Latvian alphabet
latvian_alphabet = "AĀBCČDEĒFGĢHIĪJKĶLĻMNŅOPRSŠUŪVZŽaābcčdeēfgģhiījkķlļmnņoprsštuūvzž"

# let's make a function that returns a random name from the list
# include optional lower flag to return name in lowercase
def get_random_name(names, lower=True):
    name = random.choice(names)
    if lower:
        name = name.lower()
    return name

# let's make a function that takes in random_name and max_incorrect_guesses
# it returns a boolean whether game is won by guesser in allowed guesses
def guess_the_word(random_name, max_incorrect_guesses=5, latvian_alphabet=latvian_alphabet):
    # Initialize game variables
    incorrect_guesses = 0
    guessed_letters = set()
    # Game loop
    while incorrect_guesses < max_incorrect_guesses:
        # Display the current state of the guessed word
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in random_name])
        print(f"Current word: {display_word}")
     
        # Ask the user for a guess
        guess = input("Guess a letter: ").lower()
     
        # Check if the guess is valid
        if guess not in latvian_alphabet:
            print("Invalid input. Please enter a letter from the Latvian alphabet.")
            continue
     
        # Check if the guess is correct
        if guess in guessed_letters:
            print("You have already guessed this letter. Try another one.")
        elif guess not in random_name:
            print("This letter is not in the word. Try another one.")
            incorrect_guesses += 1
            print(f"Incorrect guess! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")
        else:
            guessed_letters.add(guess)
            print("Correct guess!")
     
            # Check if the user has guessed the entire word
            if all(letter in guessed_letters for letter in random_name):
                print(f"Congratulations! You've guessed the word: {random_name}")
                return True
    else:
        print(f"Game over! The word was: {random_name}")
        return False

# now let's write a main function
# we need to read names
# we need to get random name
# we need to run the game
def main(filename):
    # Read names from file
    latvian_names = get_names_from_file(filename)
    # Get a random name
    random_name = get_random_name(latvian_names)
    # Run the game
    guess_the_word(random_name)

# let's run the main function
if __name__ == "__main__":
    print("Let's play a guessing game!")
    # let's add argument parsing for file name as option -input
    import argparse
    parser = argparse.ArgumentParser()
    # docs on argparse: https://docs.python.org/3/library/argparse.html
    # there are many options on argparse, we will use -input for now
    parser.add_argument("-input", help="Input file path")
    args = parser.parse_args()
    # check that input file is provided
    if args.input:
        filename = args.input
    else:
        filename = "data/latvian_names.txt"
    main(filename)
    print("Thanks for playing!")


