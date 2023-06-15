# so let's talk about string indexing and slicing in Python

food = "kartupelis"

# indexing starts at 0
# so the first character is at index 0
print(food[0])

# there are historical reasons for this
# from C programming language and actually before that

# second character is at index 1
print(food[1])

# how about length of a string?
print(len(food))

# so last character is at index len(food) - 1
print(food[len(food) - 1])

# however above is not Pythonic - anti-pattern - not recommended

# Python has a better way to access last character
# we can use negative indexing

# last character is at index -1
print(food[-1])

# more on strings here https://developers.google.com/edu/python/strings

# so index 5 from the start and index -5 from the end are the same
print(food[5], food[-5]) # so 5 means 6th character

# lets make a short loop to print all charactes using range
# for i in range(len(food)):
#     print(f"i start -> food[i] {i} -> {food[i]}")
# # from the end
# for i in range(-1, -len(food) - 1, -1):
#     print(f"i start -> food[i] {i} -> {food[i]}")
# # again usually we do not do this in Python
# # we can use enumerate to get both index and value
# for i, letter in enumerate(food):
#     print(f"i start -> food[i] {i} -> {letter}")

# how about out of bounds?
# print(food[100]) # this will give an error
try:
    print(food[100])
except IndexError as err:
    print(f"Error {err} happened")

# similarly negative index out of bounds will give an error
try:
    print(food[-11])
except IndexError as err:
    print("Negative index out of bounds", err)
    print(f"Error {err} happened")

# now string slicing
print("Slicing and diceing")
# the best thing since sliced bread

# we can get a substring from a string
# we can use slicing to get a substring
print(food)
# we use the colon : to slice a string

print(food[0:3]) # so we start at index 0 and end at index 3 (not included)

# in fact there is a shortcut for this
print(food[:3]) # so if we omit the start index it defaults to 0

# we can also omit the end index
print(food[3:]) # so if we omit the end index it defaults to len(food)

my_alphabet = "abcdefghijklmnopqrstuvwxyz"
# could have imported string.ascii_lowercase instead

# we can also use negative indexes

print(my_alphabet[-3:]) # last 3 characters
print(my_alphabet[-3:-1]) # 3rd and 2nd from the end
print(my_alphabet[-3:26]) # 3rd and 2nd from the end

# we can overstep bounds with no error
print(my_alphabet[-3:100]) # 3rd to the end
# we can overstep both bounds
print(my_alphabet[-100_000:9_000]) # whole string

# we also have step (similar to range)
print(my_alphabet[0:10:2]) # every second character
# how about every 2nd character 
print(my_alphabet[::2]) # every second character
# every 3rd character
print(my_alphabet[::3]) # every third character
# lets start with 2nd character
print(my_alphabet[1::3]) # every third character

# we can also use negative step
print(my_alphabet[::-1]) # reverse string
# reversing a string used to be a common interview question
# in Python it is trivial

# if we did not know of this -1 feature we would have to do a loop
# to reverse a string
reversed_string = ""
for i in range(len(my_alphabet) - 1, -1, -1):
    reversed_string += my_alphabet[i]
print("Reversed", reversed_string)
# again no need for above in Python

# remember strings are immutable
# so to save a substring we need to assign it to a variable
my_substring = my_alphabet[0:10:2]
my_tupelis = food[3:]
