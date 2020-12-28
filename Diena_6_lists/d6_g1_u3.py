sentence = input("Ievadiet teikumu: ")
rev_list = [word[::-1] for word in sentence.split()]
print(sentence, "->", " ".join(rev_list).capitalize())

# sentence = input("Please type sentence: ")
# words = sentence.split()
# new_words = []
# for word in words:
#     # rwords=''.join(reversed(word))
#     rword=word[::-1]
#     new_words.append(rword)
# new_sentence = ' '.join(new_words)
# print(f"{sentence} -> {new_sentence.capitalize()}")
