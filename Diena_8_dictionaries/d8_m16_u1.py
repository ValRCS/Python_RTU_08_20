from collections import Counter

## 1.uzdevums
def get_char_count(text):
    char_dict = {}
    for char in str(text):
        if char in char_dict:
            char_dict[char]  += 1
        else:
            char_dict[char]  = 1
    return char_dict 
 
print(get_char_count("hubba bubba"))
digit_dict = get_char_count(599637003)
print(digit_dict)

my_counter = Counter("hubba bubba") # Counter gives us a dictionary with some extra
print(my_counter)
print(my_counter.most_common())
plain_dict = dict(my_counter)
print(plain_dict)
