# for creating dictionary from other iterables we can use dict comprehension

name = "Valdis"
# let's make a dictionary from name and its unicode code points
# we can use dict comprehension
ord_dict = {letter: ord(letter) for letter in name}
print(ord_dict)
# so letter was key and ord(letter) was value
# i could have done it reverse
ord_letter_dict = {ord(letter): letter for letter in name}
print(ord_letter_dict)

# i could use dictionary comprension to filter an existing dictionary

# let's filter out only keys with even unicode code points
ord_even_dict = {key: value for key, value in ord_dict.items() if value % 2 == 0}
print(ord_even_dict)

# if i did not know about dictionary comprehension i could have done it like this
ord_even_dict = {}
for key, value in ord_dict.items():
    if value % 2 == 0: # lets us use more complex conditions
        ord_even_dict[key] = value
print(ord_even_dict) # same result as above with dict comprehension