# 1. uzd Saskaita gan simbolus virknē, gan ciparus skaitlī.
 
def get_char_count(txt_int):
    string_text = str(txt_int)
    dictionary = {}
 
    for char in string_text:
        # char_count = dictionary.get(char, 0) # ja vārdnīcā nebūs char tad tiks atgriezta 0
        # dictionary[char] = char_count+1 # ja nebūs char, tad tiks pievienots 1
        # same in one line
        # dictionary[char] = dictionary.get(char, 0) + 1
        # we could also use in operator
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
        # all of three above are correct approaches
        # mistake would be to use count() method
        # why?
        # because count() method would count all occurences of char in string_text
        # over and over again - so not efficient
        # for each char in string_text we would iterate over string_text
        # we would get O(n^2) time complexity - quadratic time
 
    return dictionary

print(get_char_count(1234567890))
print(get_char_count("abracadabra maģija mana")) 

# counting things is so common that there is a special class for it
# collections.Counter
from collections import Counter # standard library
# Counter is a dictionary subclass for counting hashable objects
# i call it dictionary with benefits

# so let's use it
my_counter = Counter("abracadabra maģija mana")
print(my_counter)
# we also can get top n most common elements
# lets save top 5
top_5 = my_counter.most_common(5)
print(top_5) # notice it is a list of tuples
# if need be we can convert it to dictionary
top_5_dict = dict(top_5)
print(top_5_dict)

# i can count items in any iterable
my_shopping_list = ['apple',
                    'apple',
                    'apple',
                    'banana',
                    'citrus',
                    'chorizo',
                    'potato',
                    'potato',
                    'sausage',
                    'chocolate',
]
my_shopping_counter = Counter(my_shopping_list)
print(my_shopping_counter)
# i can get top 3 most common items
print(my_shopping_counter.most_common(3))
