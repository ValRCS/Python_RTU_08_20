my_words = ["Hello", "my", "name", "is", "John"]
print(sorted(my_words))
print(sorted(my_words, key=len))

# lambda expression - anonymous function
print(sorted(my_words, key=lambda x: x[-1])) # sort by last letter

def get_last_letter(word):
    return word[-1]

print(sorted(my_words, key=get_last_letter)) # sort by last letter

also_get_letter = lambda word: word[-1] # so we save anonymous function in also_get_letter
print(also_get_letter("Hello"))