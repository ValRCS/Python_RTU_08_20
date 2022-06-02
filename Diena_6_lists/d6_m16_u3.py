# 3.uzd
 
text_string1 = input('Ievadiet tekstu')
text_list = text_string1[::-1].split()
# text_list.reverse()  # this reverses the list
text_list = text_list[::-1]  # this reverses the list again
text_string2 = ' '.join(text_list)
print(f'{text_string1} -> {text_string2.capitalize()}')