from collections import Counter 
import string

def get_char_count(text):
    text = str(text) # does nothing if string
    char_dict = {}
    for a in text:
        if a in char_dict: # keys() nav obligāti
            char_dict[a] += 1
        else:
            char_dict[a] = 1
    return char_dict

print(get_char_count("hubba bubba"))
print(get_char_count(12341874908505))

def get_char_counter(text):
    return Counter(text) # dictionary with some extras if we did not want extras then simpo
    # return dict(Counter(text)) # no extras

my_counter = get_char_counter("hubba bubba")
print(my_counter)
print(my_counter.most_common(3)) # top 3 lists ar tuples
print(dict(my_counter)) # no bonuses

item_counter = Counter(['alus', 'maize', 'ūdens', 'alus', 'kafija'])
print(item_counter)


num_dict = {k:0 for k in string.digits}
print(num_dict)