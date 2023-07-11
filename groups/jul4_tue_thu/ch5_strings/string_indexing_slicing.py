# Let's discuss indexing and slicing in strings

food = "kartupelis"

# let's say we want to get first letter of the string
# we can do that by using indexing
# indexing is done by using square brackets []
# inside the square brackets we put the index of the character we want to get
# indexing starts at 0

# let's get the first letter

print(food[0]) # k
# how about the second letter?
print(food[1]) # a
# well how about 10th?
# print(food[10]) # IndexError: string index out of range
try:
    print(food[10])
except IndexError as e:
    print("Danger", e)

print(food[9])  # s - so 10th letter is 9th index

# we could get lenght of the string and then subtract 1
print(len(food)) # 10
# so last letter would be 
print(food[len(food) - 1]) # s
# above is not very convenient and considered an anti-pattern

# to solve this Python has negative indexing
# https://developers.google.com/edu/python/strings
# negative indexing starts at -1
# thus last letter would be
print(food[-1]) # s
# second to last would be
print(food[-2]) # i

# again we can go out of bounds with negative indexing
try:
    print(food[-11]) # there is no -11th index
except IndexError as e:
    print("Danger negative index out of bounds", e)

# now how do we loop over a string?
# we can use for loop and iterate over the string no need for indexes
for letter in food:
    print(letter, end="|") # k|a|r|t|u|p|e|l|i|s|

# we could use indexes using range function
for i in range(len(food)):
    print("Letter No.", i, food[i]) 
# again above is not considered a good practice in Python!

# instead we can use enumerate function
for i, letter in enumerate(food):
    print("Letter No.", i, letter)

# what do we do when we need a substring?
# we use something called slicing
# the best thing since sliced bread

# let's say first 3 letters
print(food[0:3]) # kar # 0 is inclusive, 3 is exclusive

# this is so common that Python has a shortcut
print(food[:3]) # kar # so 0 is optional, again 3 is exclusive, 4th is not included
# if we skip colon we get
print(food[3]) # t because that is 4th letter

# let's make an alphabet string
alphabet = "abcdefghijklmnopqrstuvwxyz"
assert len(alphabet) == 26  #throws AssertionError if not true
# if I wanted to be sure i could have used import string and string.ascii_lowercase
import string # various string constants
print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz

# let's get first 10 letters
print(alphabet[:10]) # abcdefghij

# how about last 3 letters?
# with positive indexing it is a bit messy
print(alphabet[23:26]) # xyz
# instead we can use negative indexing
print(alphabet[-3:]) # xyz - so we indicate start from -3 and go to the end of the string

# how about -3 to -1
print(alphabet[-3:-1]) # xy - so we indicate start from -3 and go to -1, -1 is not included

# how about 6th to 10th letter?
print(alphabet[5:10]) # fghij # 5 because that is 6th letter, 10 because that is 11th letter

# i can use variables to save my slices
first_10_letters = alphabet[:10]
last_3_letters = alphabet[-3:]
# combine them
print(first_10_letters + last_3_letters) # abcdefghijxyz

# we can also use step in slicing
# let's say we want every second letter
print(alphabet[::2]) # acegikmoqsuwy
# we can get every 3rd letter
print(alphabet[::3]) # adgjmpsvy
# we can start with 2nd letter and get every 5th letter
print(alphabet[1::5]) # bglqv

# we can also use negative step
# in fact Python has a shortcut for reversing a string

print(alphabet[::-1]) # zyxwvutsrqponmlkjihgfedcba
# we can reverse food
print(food[::-1]) # sileputrak
# how about drink?
drink = "alus"
print(drink[::-1]) # sula

# finally with slicing we do not get IndexError
# we can use any number for start and end even really huge ones
print(alphabet[100:200]) # empty string
print(alphabet[-100_000:200]) # abcdefghijklmnopqrstuvwxyz
print(alphabet[10:200_000]) # klmnopqrstuvwxyz

# again if had a big string then those indexes would produce different results