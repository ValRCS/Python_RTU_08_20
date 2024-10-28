# 1. Simbolu biežums
# 1 a
def get_char_count(text):
    burti_dict = {} 
    # so in the end to count we only have to go through the text(sequence) once
    for ch in text:
        # if burti_dict.get(ch) is None:
        if ch not in burti_dict: # a bit faster
            burti_dict[ch] = 1 # so we set the value to 1 initially
        else:
            burti_dict[ch] += 1 # same as burti_dict[ch] = burti_dict[ch] + 1
        # we could have used setdefault method
        # setdefault has built in check if key is in dictionary
        # burti_dict.setdefault(ch, 0)
        # burti_dict[ch] += 1
    # print(burti_dict)
    return burti_dict
 
print(get_char_count("vienkārši ievadiju random tekstu"))
abra_dict = get_char_count("Abrakadabra")
print(abra_dict)

# will work on lists, tuples as well
food_list = ["apple","banana", "apple", "banana", "grapes", "apple", "grapes", "banana", "apple", "grapes"]
print(get_char_count(food_list))

# Python has built in Counter class in collections module
from collections import Counter # this is a standard library module
abra_counter = Counter("Abrakadabra")
print(abra_counter)
# it is a Counter object, which is dictionary subclass
# so dictionary with some extra functionality
# so we can use it as dictionary
print(abra_counter['a']) # 4
# also we have most_common method
print(abra_counter.most_common(3)) # [('a', 4)]

# we can convert most_common into dictionary
abra_dict = dict(abra_counter.most_common(4))
print(abra_dict) # {'a': 4, 'b': 2, 'r': 2, 'k': 1}

# we can also use Counter on lists
sentence = "I have a cat and a dog and a chicken and something else"
words = sentence.split() # this will get list of words
print(words)
word_counter = Counter(words)
print(word_counter)