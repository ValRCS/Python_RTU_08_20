sentence = input("Ievadiet teikumu: ")
words = sentence.split(" ")
words_reversed = [word[::-1] for word in words]
sentence_reversed = " ".join(words_reversed).capitalize()
print(f"{sentence} --> {sentence_reversed}")