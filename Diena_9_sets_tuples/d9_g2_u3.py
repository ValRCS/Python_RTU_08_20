import string

def is_pangram(my_text, a='abcdefghijklmnopqrstuvwxyz'): 
    # return not set(a) - set(mytext.lower())
    return set(a) <= set(my_text.lower())
 
# my_pangram = is_pangram("Sodien ir otrdiena divpadsmitais janvaris")
# print(my_pangram)
 
# my_pangram = is_pangram("Šodien ir otrdiena divpadsmitais janvāris")
# print(my_pangram)

# print(string.ascii_lowercase)

print(is_pangram("The five boxing wizards jump quickly", a=string.ascii_lowercase))
# print(is_pangram("The not boxing wizards jump quickly", a=string.ascii_lowercase))


# def is_pangram(my_text: str, eng="abcdefghijklmnopqrstuvwxyz",
#                lv="aābcčdeēfgģhiījkķlļmnņoprsštuūvzž0123456789") -> bool:
#     """ Returns True or False: is given text a pangram.
#     You can choose pangram language (ENG or LV)"""
 
#     # my_text_list = my_text.split()
#     # my_text = "".join(my_text_list).lower()
#     choose = input("In which language would you like to chek pangram? "
#                      "Write ENG or LV: ")
#     language = []
#     if choose.lower() == "eng":
#         language = eng
#     elif choose.lower() == "lv":
#         language = lv
#     else:
#         print("Incorrect answer")
 
#     return set(language) <= set(my_text.lower())

print(is_pangram('Tfū, čeh, džungļos 123456789 0 blīkšķ, zvaņģim jācērp!'))