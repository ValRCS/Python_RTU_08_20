##DICTIONARY  1A
# def get_char_count(string):
#     frequency = {'a': 0, 'c': 0, 'b': 0, 'e': 0, 'd': 0, 'g': 0, 'f': 0, 'i': 0, 'h': 0, 'k': 0,
#  'j': 0, 'm': 0, 'l': 0, 'o': 0, 'n': 0, 'q': 0, 'p': 0, 's': 0, 'r': 0, 'u': 0, 
# 't': 0, 'w': 0, 'v': 0, 'y': 0, 'x': 0, 'z': 0}
#     for char in string:
#         if char in frequency:
#             frequency[char] += 1
#     return frequency
 
# res = get_char_count("Kaaarstumvilnis")
# print(res)

# def get_char_count(text):
#     if type(text) is not str:
#         return {} # empty dictionary
#     set_of_symbols = set(text) # so we need to go through our text here
#     accurances_of_symbols = {}
#     for symbol in set_of_symbols :
#         accurances_of_symbols[symbol] = text.count(symbol)  # each symbol will need counting  
#     # not as efficient as going through text once but easier to understand
#     return accurances_of_symbols

text = "hubba bubba kaķis un suns ķēmojās"
def get_char_count(text):
    my_dict = {}
    for symbol in text:
        if symbol in my_dict: # this check is very fast O(1) operation
            my_dict[symbol] += 1
        else:
            my_dict[symbol] = 1
    return my_dict
 
print(get_char_count(text))

# print(get_char_count("Kaaarstumvilnis"))

# this counter is so common that Python offers a built in class for it
from collections import Counter
# Counter is a dictionary with "benefits" - extra methods
my_counter = Counter(text)
print(my_counter)
print(my_counter.most_common(5)) # most common 3 symbols

# so i can createa  dictionary from most_common which is a list of tuples
top_10_dictionary = dict(my_counter.most_common(10))
print(top_10_dictionary)

# i can count item in a list
shopping_list = ["milk", "bread", "eggs", "milk", "milk", "eggs","potatoes","milk"]
print(Counter(shopping_list))