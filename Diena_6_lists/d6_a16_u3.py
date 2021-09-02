# Uzdevums Nr. 3
 
sentence = input("Enter any sentence: ")
sentence_list = sentence.split(" ")
# rev_sentence_list = [x[::-1] for x in sentence_list][::-1]
rev_sentence_list = [x[::-1] for x in sentence_list]
print(rev_sentence_list)
result = " ".join(rev_sentence_list)
print(result.capitalize())