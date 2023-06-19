########## 3. uzdevums ##########
 
# sentence = input("Ievadiet vienu vai vairākus vārdus: ")
# words = sentence.split()
# reversed_words = [word[::-1].capitalize() if word[0].isupper() else word[::-1] for word in words]
# reversed_sentence = ' '.join(reversed_words)
# print(reversed_sentence)

sentence = input("Ievadiet vienu vai vairākus vārdus: ")
# deconstruction of the above line
word_list = sentence.split() # by default uses any whitespace to split - returns a list

# create a new list with reversed words
reversed_word_list = []
for word in word_list:
    reversed_word_list.append(word[::-1]) # minimalistic solution
    # if word[0].isupper():
    #     reversed_word_list.append(word[::-1].capitalize())
    # else:
    #     reversed_word_list.append(word[::-1])

# construct a new sentence from the reversed word list
reversed_sentence = ' '.join(reversed_word_list) # we do lose all the extra whitespace -
# only single space between words remains
print(reversed_sentence)