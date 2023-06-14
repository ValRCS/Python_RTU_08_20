# let's talk about string slicing in Python

food = "potatoes"

# we can use square brackets to access individual characters in a string
print(food[0]) # first character
# indexing starts at 0 !
print(food[1]) # second character NOT first

# how many letters are there in the word potatoes?
# how many characters are there in the string potatoes?

# we can use len() function to get the length of a string

print(len(food))

# so to get last letter we could use len() - 1
# warning this is anti-pattern in Python!
print(food[len(food) - 1]) # so 8 - 1 = 7
print(food[7]) # so 8 - 1 = 7

# instead we can use negative indexing
# Python offers negative indexing for strings as well
# so -1 is the last character
print(food[-1])

# picture at https://developers.google.com/edu/python/strings
# address: https://developers.google.com/static/edu/python/images/hello.png

# so let's get first letter using negative indexing
print(food[-8]) # so -8 + 8 = 0
print(food[0])

# how about out of bounds?
try:
    print(food[8]) # so 8 is out of bounds
    # without try the program would crash
except IndexError:
    print("Index 8 is out of bounds for string potatoes")

# similarly negative indexing can go out of bounds as well
try:
    print(food[-9]) # so -9 is out of bounds
    # without try the program would crash
except IndexError:
    print("Index -9 is out of bounds for string potatoes")

# so if you are not sure about the index you could use len(my_string) to check
# or you could use try except

# no need to put everything in try except - just some parts that might fail

# we can use slicing to get a substring from a string
# Python offers slicing for strings a compact way to get substrings

# we use square brackets to slice strings
# we use colon to indicate slicing

my_alphabet = "abcdefghijklmnopqrstuvwxyz"
# we could have imported string module and used string.ascii_lowercase
# import string # offers various prebuilt strings
# # docs at https://docs.python.org/3/library/string.html
# print(string.ascii_lowercase)

# so let's get first 3 letters
print(my_alphabet[0:3]) # so we start at 0 and end at 3 (not including 3)
# so 3 is 4th letter it is not included in the slice
# so we get 0, 1, 2 letters by indexing 0:3
# this is so common that Python offers a shortcut
print(my_alphabet[:7]) # so we start at 0 and end at 3 (not including 3)

# slicing works with negative indexes as well
# let's get last 3 letters
print(my_alphabet[-3:]) # so we start at -3 and end at the end of the string

# what is intersting we can go over the end of the string with no error
# so if we want to get last 10 letters we can do that
print(my_alphabet[-10:]) # so we start at -10 and end at the end of the string
print(my_alphabet[-10:9_000]) # so we start at -10 and end at the end of the string

# i can overshoot both ends
print(my_alphabet[-1000:9_000]) # so we start at -1000 
# and end at the end of the string
# so we get the whole string in this case

# let's remember range function which had start, stop and step
# similarly slicing can have start, stop and step
# so let's get every second letter

print(my_alphabet[::2]) # so we start at 0 and end
# at the end of the string
# so between first two colons we have start and stop defaulting to 0 and len(my_alphabet)
# and after second colon we have step defaulting to 1

# lets get every third letter starting with second letter
print(my_alphabet[1::3]) # so we start at 1 and end

# lets remember that strings are immutable
# so if we want to save the result of slicing we need to assign it to a variable
my_alphabet_slice = my_alphabet[1::3]
print(my_alphabet_slice)

# finally we can use negative step to reverse a string
print(my_alphabet[::-1]) # so we start at 0 and end
reversed_alphabet = my_alphabet[::-1]
print(reversed_alphabet)