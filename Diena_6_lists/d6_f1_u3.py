sentence = input("Ievadiet teikumu")
# code golf , i'd say two lines would be better
print(" ".join([word[::-1] for word in sentence.split()]).capitalize())
words = sentence.split()
reverse_words = [word[::-1] for word in words]
new_sentence = " ".join(reverse_words).capitalize()
print(new_sentence)
# sentence_list = sentence_input.split()
 
# rev_lst = []
# for item in sentence_list:
#     rev_lst.append(item[::-1])
 
# print(" ".join(rev_lst).capitalize())
 