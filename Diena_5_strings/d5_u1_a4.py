word_original = input("Ievadiet savu vārdu: ")
word_reverse = word_original[::-1] # reverse word
word_reverse_cap = word_reverse.capitalize() # capitalize first letter
print(f"{word_original} —> {word_reverse_cap}, pamatīgs juceklis, vai ne {word_original[0]}?")