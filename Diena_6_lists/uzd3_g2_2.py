my_sentence = input("Enter yout sentence ")
# my_sentence_split = my_sentence.split()
# my_rev_list = []
# for item in my_sentence_split:
#     rev = (item[::-1])
#     my_rev_list.append(rev)
my_rev_list = [word[::-1] for word in my_sentence.split()]
rev_my_sentence = " ".join(my_rev_list)
# rev_my_sentence = " ".join([word[::-1] for word in my_sentence.split()])
print(f"{my_sentence.capitalize()} --> {rev_my_sentence.capitalize()}")