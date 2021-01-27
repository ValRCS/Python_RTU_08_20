from collections import Counter

def get_char_count(text):
    my_dict = {}
    for i in text:
        if i in my_dict: # so i is key
            my_dict[i] += 1 # my_dict[i] = my_dict[i] + 1
        else:
            my_dict[i] = 1
    return my_dict
 
print(get_char_count("hubba bubba"))

my_nums = [5, 9, 9, 6, 3, 7, 0, 0, 3]
print(Counter(my_nums))

my_char_cnt = Counter("hubba bubba")
print(my_char_cnt)
print(my_char_cnt.most_common())