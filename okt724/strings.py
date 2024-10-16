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

# if we access single characters by index
# we can get IndexError if we go out of bounds
try:
    print("Out of bounds", food[10]) # index 10 is 11th character!!
except IndexError as e:
    print(f"Error: {e}")
    
# however slicing does not throw errors, we can use any index we want
print("crazy indexes but sane rezults", food[-151352:3522512])
# above would start mattering if my string was at least 151352 characters
# of course those numbers are arbitrary chosen at random by my fingers
# what is the worst that could happen
# i could get nothing
print("if both indexes are out of range:", food[5000:5200])
chiks = food[5000:5200]
print("nekas",chiks)

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(f"alphabet is {len(alphabet)} characters long")
# i could get every second letter of alphabet
# slice has 3rd option, step, which has default 1
print("every second letter", alphabet[0:26:2]) # 2 is step
print("every second letter", alphabet[::2]) # 2 is step start 0 and 26 are default
# i could start with letter b
print("every second letter starting with second", alphabet[1::2])
print("every third letter", alphabet[::3])
# this leads to last slicing approach, we can reverse strings with slices
reverse_alphabet = alphabet[::-1] # so this gives us reversed string
print(reverse_alphabet)

# python strings are immutable, if I need some string changed, I make a new one

# let's change p in kartupelis to m
# let's find index of p in kartupelis
# it should be 5 (6th letter)
p_index = food.index("p")
print("We can find p at index", p_index, food[p_index])
# we could also use find method
p_index_also = food.find("p")
print("We can find p at index", p_index, food[p_index_also])
# what is the difference?
# difference is how not finding substring is handled
tupe_index = food.index("tupe")
tupe_len = len("tupe")
print(food[tupe_index:tupe_index+tupe_len]) #guarantee if found we print this string
# thus I can print everything before
print("BEFORE tupe", food[:tupe_index])
# also after when combined with substring length
print("AFTER tupe", food[tupe_index+tupe_len:])
# however we do not have a guaranteed that we will find anything
# index will throw an error on bad substring or as we can call it needle
try:
    no_such_index = food.index("Trumps")
except ValueError as e:
    print(f"error {e}")
# find will give you -1 if you do not find the substring
neg_index = food.find("Kamila")
print(neg_index)
# so use either find or index just be ready to handle not finding
# for index you would use try except
# for find you would save the resulting index and check for -1
# find and index will give you same results if they find the substring

# back to our kartupelis
# we want to change p to m
# if we know the index we would like to do this
try:
    food[p_index] = "m" # strings are immutable not allowed
except TypeError as e:
    print("Error ", e)
  
# since we know index we can rebuild the string in various ways
# following will INSERT the letter between keeping everything from original
new_food = food[:p_index] + "m" + food[p_index:]
print(new_food)
new_food_2 = food[:p_index] + "m" + food[p_index+1:] # one is length of "m"
print(new_food_2)
# i could use f-strings for this as well
new_food_3 = f"{food[:p_index]}m{food[p_index+1:]}____and so on {food[p_index:]}_"
print(new_food_3)

# sometimes we just want to replace some characters without caring about indexes
# we can do that as well
# we use replace method
new_food_4 = food.replace("p","m") # food is not changed! we get new strings
print(new_food_4)
breakfast = "Auzu Putra ar Mellenēm"
print(breakfast)
# let's change all u with y
breakfast_y = breakfast.replace("u","y") # change ALL occurences
print(breakfast_y)
# i could only say copy and replace first two
breakfast_y2 = breakfast.replace("u","y", 2) # so 2 or less changes
print(breakfast_y2)
# we could use replace to get rid of all spaces
no_spaces = breakfast.replace(" ", "")
print(no_spaces)
# if i use same variable I will overwrite the original
# let's see this with lower method which lowercases
breakfast = breakfast.lower() # original gets overwritten
print(breakfast)
breakfast = breakfast.capitalize() # First letter only!
print(breakfast)
breakfast = breakfast.title() # first letter of Every word is uppercase
print(breakfast)
crazy_case = breakfast.swapcase() # switches cases around
print(crazy_case)
all_upper = crazy_case.upper()
print(all_upper)

dirty_city = "     Rīga   \t \t \n\n   "
print(dirty_city)
# i can strip left AND right side of all whitespace characters including newlines
clean_city = dirty_city.strip()
print(clean_city)
right_side_clean = dirty_city.rstrip()
left_side_clean = dirty_city.lstrip()
print(right_side_clean)
print(left_side_clean)






