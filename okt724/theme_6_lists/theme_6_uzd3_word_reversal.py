sentence = input("Ievadiet teikumu: ")
# next is a one liner to reverse the words in a sentence
# reversed_sentence = ' '.join(word[::-1] for word in sentence.split())
# let's do this step by step
words = sentence.split() # split the sentence into words
# now I can process the words one by one

# reversed_words = [word[::-1] for word in words] # reverse each word with list comprehension
# let's do the reversed words with a loop
reversed_words = []
for word in words:
    reversed_words.append(word[::-1]) # we add the reversed word to the list
# the above loop is equivalent to the list comprehension above

# we have a list of words reversed
# now we need to join them into a string
reversed_sentence = ' '.join(reversed_words)
capitalized_reversed_sentence = reversed_sentence.capitalize()
print(capitalized_reversed_sentence)