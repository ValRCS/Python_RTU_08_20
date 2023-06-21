##############
# 1st Task
##############

def get_char_count(text):
    chars = {}
    # text = text.replace(" ", "") # optional
    for char in text: # so linear time O(n) where n is number of characters
        # count is slow O(n) linear time! we would get O(n^2) quadratic time
        # if char in chars: # also O(1) constant time - similar to set
        #     chars[char] += 1 # these instant
        # else:
        #     chars[char] = 1 # initialising new key
        # alternative using get - same principle as above
        chars[char] = chars.get(char, 0) + 1
        # so if no key char is found then we get 0
    return chars



input = input("Enter word or multyple words: ")
print(get_char_count(input))

# turns out this is so common that there is a built in Counter class
# https://docs.python.org/3/library/collections.html#collections.Counter
from collections import Counter
counter_result = Counter(input)
print(counter_result)
# i call it dictionary with benefits - extra methods
print(counter_result.most_common(5))  # TOP 5 most common elements
most_common_5 = counter_result.most_common(5)
print(most_common_5[0][0]) # first element of first tuple
# if i want dictionary with top 10 most common elements
new_dict = dict(counter_result.most_common(10)) # i can convert to dict
print(new_dict)


# i can transform into count any list items
my_shopping_list = ["beer", 
                    "beer",
                    "banana",
                    "apple",
                    "apple",
                    "apple",
                    "strawberry"
                    ]
print(Counter(my_shopping_list))

# again Counter is a dictionary with extra methods
# you can always convert to regular dictionary with dict(my_counter)