#3. uzd
 
sentence = input("Lūdzu ievadiet tekstu: ")
words = sentence.split() # by default split uses any whitespace
# so words is a list of words - strings
word_list = []
for word in words:
    reversed_word = word[::-1] # slice with step -1
    word_list.append(reversed_word)
# l = [i[::-1] for i in sentence] # list comprehension
# word_list now has a list of reversed words
# we will join them back into a string using single space
reversed_words_text = ' '.join(word_list)
# finally we capitalize the first letter of the string
reversed_words_text = reversed_words_text.capitalize()
print(reversed_words_text)
 

# one liner of the above
print(' '.join([w[::-1] for w in input("Lūdzu ievadiet tekstu: ").split(' ')]).capitalize()) # tas pats tikai 1 līnijā
# print(' '.join([i[::-1] for i in input("Lūdzu ievadiet tekstu: ").split(' ')])) # tas pats tikai 1 līnijā