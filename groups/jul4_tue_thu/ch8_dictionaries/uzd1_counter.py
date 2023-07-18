# 1. Simbolu biežums
 
def get_char_count(text):
    counter_dict = {}
    # we could convert any input to string
    text = str(text) # we can count digits in numbers
    # so crucially we only loop through the text once
    for c in text:
        if c in counter_dict:
            counter_dict[c] += 1 # constant time operation
        else:
            counter_dict[c] = 1
 
    return counter_dict

# test it
print(get_char_count("hello")) # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# count digits
print(get_char_count(1234562523527890)) 


# counting things is so common that there is a special class for it
from collections import Counter
# Counter is a dictionary with "benefits" - extra methods

text = "abrakadabra maģija mana"
counter = Counter(text)
print(counter) # Counter({'a': 7, 'r': 2, 'b': 2, ' ': 2, 'k': 1, 'd': 1, 'm': 1, 'ģ': 1, 'i': 1, 'j': 1, 'n': 1})
top_5 = counter.most_common(5) # returns a list of tuples
print(top_5) # [('a', 7), ('r', 2), ('b', 2), (' ', 2), ('k', 1)]
# if we want we can convert it to a dictionary - plain one
top_5_dict = dict(top_5)
print(top_5_dict) # {'a': 7, 'r': 2, 'b': 2, ' ': 2, 'k': 1}

# we can also use Counter to count digits in a number
digit_counter = Counter(str(1234562523527890)) # needs to be iterable
print(digit_counter) # Counter({2: 4, 5: 3, 3: 2, 1: 1, 4: 1, 6: 1, 7: 1, 8: 1, 9: 1, 0: 1})

long_latvian_text = """Kāds ir tavs vārds?
Kāds ir tavs uzvārds?
Kāds ir tavs vecums?
Kāds ir tavs e-pasts?
Kāds ir tavs telefona numurs?
Kāds ir tavs dzimums?
Kāds ir tavs dzimšanas datums?
"""
# we can count words
words = long_latvian_text.split() # split by whitespace
word_counter = Counter(words)
print(word_counter)
# we could have cleaned up and normalized the text before counting
