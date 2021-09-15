# 3. uzdevums
# my_text = input("Ievadiet savu tekstu: ")
 
# text_1 = "nav"
# text_2 = "slikts"
 
# if my_text.find(text_1) != -1 and my_text.find(text_2) != -1:
#     new_text=my_text.replace(text_1, "ir" )
#     new_text=new_text.replace(text_2, "labs" )
#     print(new_text)
# else:
#     print(my_text)

# 3. Uzrakstīt programmu teksta pārveidošanai
# text = input('Please enter your text \n ')
# lower_text = text.lower()
# text_bad = 'slikts'
# text_bad_fem = 'slikta'
# text_no = 'nav'
# text_good = 'ir labs'
# text_good_fem = 'ir laba'
# is_no = text_no in lower_text #convert text to lover case
# is_bad = text_bad in lower_text #check for male version
# is_bad_fem = text_bad_fem in lower_text #check for female version
 
# if (is_no and is_bad) or (is_no and is_bad_fem):
#     if is_bad_fem:
#         text_good = text_good_fem
#         text_bad = text_bad_fem
#     no_index = lower_text.find(text_no)
#     bad_index = lower_text.rfind(text_bad) + len(text_bad)
#     if no_index > bad_index: # nav comes after slikts
#         print(text)
#     else:
#         new_text = text[:no_index] + text_good + text[bad_index:]
#         print(new_text.capitalize())
# else:
#     print(text)

word_string = str(input("Enter text: "))
gender = word_string.find("slikt")
 
nav_index = word_string.find("nav") 
slikt_index = word_string.rfind("slikt")
if nav_index < slikt_index and nav_index > 0 and slikt_index > 0:
    if word_string[gender+5] == "s":
        print(word_string[:nav_index] + "ir labs" + word_string[word_string.rfind("slikts")+6:])
    elif word_string[gender+5] == "a":
        print(word_string[:nav_index] + "ir laba" + word_string[word_string.rfind("slikta")+6:])
else:print(word_string)