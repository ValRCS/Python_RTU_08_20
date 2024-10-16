# strings are sequences of single letter strings in Python
# we also could have empty string with nothing
# Python strings are immutable - means we do not change them
# we can just overwrite them

food = "Pizza"
# in Python there is no difference between " and '
drink = 'Coffee'
# it can be convenient to use " when we need ' inside string
# and vice versa
quoted_text = "It's a sunny day!" # then we can use ' inside
# rarer but useful we could use " inside then we use ' outside
another_quote = 'It is a "warm" autumn indeed '
print(quoted_text)
print(another_quote)

# what if we need both " and '
# we have two choices
# we could escape characters with \
escaped_text = "some text with \"quote\" inside and also 'as well' indeed"
print(escaped_text)
# https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences
# we can use escape characters to create multiline text
multi_line_escaped = "line 1\nline 2\nline 3\nline 4\tX\tX\nline 5\n\nfin \\ish"
print(multi_line_escaped)
# using single \ I can enter single line over many rows
single_line_text = "very very long text\
continues this long text\
and more in same line"
print(single_line_text)

# it might be more convenient to just use """ for multi line strings
big_string = """I can write any symbols
Can use many rows
I can use " I can use '
I can use tab with \t if need be
And so on\
Note \ does not work here it is just a backslash
And so on"""
print(big_string)
# even better I can combine f-strings with multiline """ strings
string_template = f"""I love {food} 🍕
but I also love {drink} 🧉.
Also any string supports full unicode in Python.
"""
print(string_template)

# now we want to start working with individual letters in strings
# so in Python we use [index] to get individual letters in strings
# index starts with 0 !
# thus first letter will be
print(food, "starts with", food[0])
print("second", food[1]) # so 2nd character will be with index 1

# let's overwrite pizza with kartupelis
food = "kartupelis"
print("Cool we got", food)
print(food, "starts with", food[0])

# so since kartupelis has 10 letters
# the last letter will have index -
print(food, "last letter", food[9]) # 9 because we start with 0

# now how would we generally get the last letter of some string?
# what if we knew the length?
string_length = len(food)
print(food, "is ", string_length, " characters long")
# then I could do the following to generalize last letters
print(food, "last letter", food[string_length-1])
# above is to be avoided in Python, we have better syntax
print(food, "last letter", food[-1])
# Python offers us TWO indexes for sequences
# left->right starts from 0
# left<-right starts from -1
# then first letter of kartupelis could also be gotten as follows
print(food, "starts with", food[-10])
# which index to use? use one which is more convenient
# I did not have to use variables
# I could do this, thought not very useful
print("pirmais burts kartupelim", "kartupelis"[0])

# what about longer substrings ?
# Python offers a very convenient syntax
# so called slicing
# best thing since sliced bread

# how about first three letters of food?
# we simply use same [] but we use [start_index:stop_index_not_included]
print("Pirmie trīs burti", food[0:3])
# in fact start is 0 by default
print("Pirmie trīs burti", food[:3]) # 0 is default
# how about middle ?
print("vidū", food[3:8]) # we stop at index 7 included, but not 8, so we stop at 8th character
# how about end?
print("end", food[8:10]) # well there is no 10, but that is okay it is not included
# in fact end is not needed to be shown it is the default also
print("end", food[8:]) # means start with 9th character(index 8) and go to end
# if we want last 2 characters it is easier to use negative syntax
print("end", food[-2:]) # we start at second to last character
# we could mix
# start at 4th letter and stop at second to last (but not included)
print("middle", food[3:-2])



