# so let's talk about string indexing and slicing in Python

food = "kartupelis"

# we can access individual characters in string by index
# indexes start at 0
print(food[0], 
      food[1], 
      food[2], 
      food[3], 
      food[4], 
      food[5], 
      food[6], 
      food[7], 
      food[8], 
      food[9])
# so here we access individual characters in string by index 
# note print default separator is space

# we also have negative indexes in Python!
# negative indexes start at -1
print(food[-1],
    food[-2],
    food[-3],
    food[-4],
    food[-5],
    food[-6],
    food[-7],
    food[-8],
    food[-9],
    food[-10])

# see example at Google course
# https://developers.google.com/edu/python/strings

# we could also get length of string
print(len(food))
# antipattern would be to use len() to access last character in string
print(food[len(food) - 1]) # this is antipattern
# instead use negative index
print(food[-1]) # this is better

# for looping over string we can use for loop
for character in food:
    print(character)

# antipattern would be to use range() and len() to loop over string
for i in range(len(food)):
    print(i, food[i]) # this is antipattern - not Pythonic

# if you need index and character you can use enumerate()
for i, character in enumerate(food):
    print(i, character)

# what happens if we go out of bounds?
# we get IndexError
try:
    print(food[10]) # there is no 10th index that would be 11th character
except IndexError as e:
    print("Danger!",e)

# similarly for negative indexes
try:
    print(food[-11]) # there is no -11th index that would be -11th character
except IndexError as e:
    print("Danger!",e)

# we can also slice strings
# the best thing since sliced bread

# how about first 3 characters?
print(food[0:3]) # note that 3 (which would be 4th character) is not included

# we even have shorthand for first 3 characters
print(food[:3]) # so 0 is default start index
# compare with 
print(food[3]) # this would print 4th character

# let's work with alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
# let's check length
print(len(alphabet))
# i could have also imported string module
# then i could have done
# import string
# print(len(string.ascii_lowercase))

# let's get last 3 characters of alphabet
print(alphabet[-3:]) # so we do not specify end index
# compare to
print(alphabet[-3]) # this would print 24th character
# how about -3 to -1
print(alphabet[-3:-1]) # so -1 is not included!! so we get 24th and 25th characters
# we could have done this to get 24 and 25th characters
print(alphabet[23:25]) # so 23 is 24th character and 25 is 26th character

# so let's get 7th to 10th characters inclusive
print(alphabet[6:10]) # so 6 is 7th character and 10 is 11th character
# why because we start counting from 0

# we can save the slice to variable
slice = alphabet[6:10]
print(slice)

# we can also slice with step
# so let's get every 2nd character from alphabet
print(alphabet[::2]) # so we do not specify start and end indexes
# i could skip 3
print(alphabet[::3]) # so we do not specify start and end indexes

# we could start with 2nd letter and get every 2nd letter
print(alphabet[1::2]) # so we do not specify end index

# we could also slice backwards
print(alphabet[::-1]) # so we do not specify start and end indexes
reversed_alphabet = alphabet[::-1]
print(reversed_alphabet)

# with slicing we can go out of range
# we do not get IndexError
print(alphabet[0:100]) # so we do not specify end index gets whole string
# i could even go negative
print(alphabet[-100_000:200_000]) # so we do not specify end index gets whole string
# of course if we had a string with 300_000 characters then it would make some difference
