# 3.uzd
 

first_needle = "nav"
second_needle = "slikt"
replacement = "ir lab"

text = input('Ievadiet tekstu ')
nav_index = text.find(first_needle)
slikt_index = text.find(second_needle)
# we check that indexes are not -1 (not found)
# also we check that first needle is found before second needle
if nav_index > -1 and slikt_index > -1 and nav_index < slikt_index:
    print (text[:nav_index] + replacement + text[slikt_index+len(second_needle):])
else:
    print(text)