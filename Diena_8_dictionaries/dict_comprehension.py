# Dictionary Comprehension
# https://www.python.org/dev/peps/pep-0274/
# plain_squares = {n: n*n for n in range(5)} # dictionary comprehension
# print(plain_squares)
# my_squares = {str(n): n*n for n in range(5)} # dictionary comprehension
# print(my_squares)

# # so same as doing the following
# squares = {}
# for n in range(5):
#     squares[str(n)] = n*n
# print(squares)

# print(squares == my_squares) # so dictionaries have same keys with same values
# print(squares is my_squares) # but they are different objects this should be false

# my_cubes = {f"Cube of {n}": n**3 for n in range(8)}
# print(my_cubes)
food = "kartupelis"
abc = "abcdefghij" # so both strings of same length
cypher = {k: v for k, v in zip(food, abc)}
print(cypher)

def ceasar(plain_text, cypher=cypher):
    secret_list = [cypher.get(c, "X") for c in plain_text] # so replace each letter with letter from dictionary cypher
    return "".join(secret_list)

print(ceasar("art"))
print(ceasar("tupi"))
print(ceasar("valdis"))
# abc_dict = {v: i for i, v in enumerate(abc, start=1)}
# print(abc_dict)
# import string
# all_letter_dictionary = {v: i for i, v in enumerate(string.ascii_uppercase, start=1)}
# print(all_letter_dictionary)
# zero_dict = {c: 0 for c in food}
# print(zero_dict)
tel = {'valdis': 2640, 'līga': 2911, "maija":2911, "ede": 2911, "pēteris":2644}


def filter_dictionary(in_dict, value_to_find=2911):
    out_dict = {key:value for key,value in in_dict.items() if value == value_to_find}
    return out_dict

def filter_dict_without_comprehension(in_dict, value_to_find=2911):
    out_dict = {}
    for key,value in in_dict.items():
        if value == value_to_find:
            out_dict[key] = value # or out_dict.setdefault(key, value)
    return out_dict


my_filtered_dict = filter_dictionary(tel)
print(my_filtered_dict)
my_filtered_dict2 = filter_dict_without_comprehension(tel)
print(my_filtered_dict2)
new_dict = filter_dictionary(tel, 2640)
print(new_dict)


