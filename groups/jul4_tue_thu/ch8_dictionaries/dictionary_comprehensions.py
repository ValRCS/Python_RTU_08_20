# Python provides a shorter more concise way to create dictionaries

# let's say we want to create a dictionary of letters as keys
# and their Unicode numbers as values

# normal way
letter_dict = {}
text = "Valdis"
for letter in text:
    letter_dict[letter] = ord(letter)
print(letter_dict)

# dictionary comprehension way
letter_dict = {letter: ord(letter) for letter in text}
print(letter_dict)

# i could add optional filtering
# here I check if the Unicode number is greater than 100
letter_dict_filtered = {letter: ord(letter) for letter in text if ord(letter) > 100}
print(letter_dict_filtered)

# again when to use dictionary comprehension?
# when the logic is simple and fits on one line

# we could also use dictionary comprehension to filter an existing dictionary
# let's say we want to keep only keys with values greater than 100
# we could do it like this by looping through existing dictionary
letter_dict_also_filtered = {key: value for key, value in letter_dict.items() if value > 100}
print(letter_dict_also_filtered)

# also we have easy way to reverse keys and values 
# let's say we want to create a new dictionary where keys are Unicode numbers
# and values are letters
unicode_dict = {value: key for key, value in letter_dict.items()}
print(unicode_dict)

print(unicode_dict[86]) # so we can use Unicode numbers as keys
# notice one bad thing about numeric keys - they are look like list indexes
# we could have used list instead of dictionary

# numeric keys make sense for dictionaries where there are large gaps between keys
# for example 3, 234, 325252, 135156 would be good candidates for dictionary keys
# but 1,2,3,4,5,6,7,8,9,10 would be better as list indexes
