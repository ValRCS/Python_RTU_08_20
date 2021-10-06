#1
text = "hubba bubba"
# def get_char_count(text):
#     letters = {}
#     for letter in text:
#         letters[letter] = text.count(letter) # we have a loop hidden in count
#     return letters

# def get_char_count(text):
#     my_dict={}
#     # for i in text.upper(): if i only want upper case keys
#     for i in text:
#         if i in my_dict:
#            my_dict[i] += 1
#         else:
#             my_dict[i] = 1
#     return my_dict

from collections import Counter  # Python standard library Counter - dictionary with benefits/extras
# letters = input("enter words to count letters")
def get_char_count(letters):
    count = Counter(letters)
    print(count.most_common())  # prints in order of most common to least common
    return count
    
# get_char_count(letters)

my_counter = get_char_count("hubba bubba")
print(my_counter)
my_dict = dict(my_counter) # so I take off all the extras from Counter
print(my_dict)
# print(get_char_count)
# print(get_char_count(text))
# print(get_char_count("abracadabra maģija mana"))
item_count = Counter(['maize','piens','siers','piens'])
print(item_count)