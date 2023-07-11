# let's talk about string methods

# first let's check for existence of a substring in a string

# we can use in operator
haystack = "kartupelis" # string in which we are looking for a substring
needle = "tup" # substring we are looking for
print(needle in haystack) # True
print("tup" in "kartupelis") # True

# let's change our needle
needle = "tupi"
needle = "peli"
if needle in haystack:
    print(f"Found {needle} in {haystack}")
else:
    print(f"Did not find {needle} in {haystack}")

# since single character is a string of length 1
# we can check for existence of a character in a string
print("a" in "kartupelis") # True
print("art" in "kartupelis") # True

# we can compare strings - using lexicographical order
# https://en.wikipedia.org/wiki/Lexicographical_order
# basically it means that strings are compared character by character
# first character that is different determines the result

# let's compare two strings
name = "Valdis"
other_name = "Voldemorts"
print(name < other_name) # True because 'a' < 'o' in lexicographical order
print(ord('a')) # 97
print(ord('o')) # 111

# by length
print(len(name) < len(other_name)) 
print(len(name))
print(len(other_name)) 

# for finding exact location of a substring in a string we can use find method
# or index method

# find method returns the index of the first occurrence of a substring
# or -1 if substring is not found

# let's find the index of a substring
print(haystack.find("pel")) # 5 because 'pel' starts at index 5 - 6th character
print(haystack.find(needle)) 
starting_index = haystack.find(needle)
end_index = starting_index + len(needle)
print(starting_index, end_index)
print(haystack[starting_index:end_index])
# here we could have just printed peli - but above is more general will work on any string

# let's try with non existant needle
needle = "baddie"
print(haystack.find(needle)) 
starting_index = haystack.find(needle)
end_index = starting_index + len(needle)
print(starting_index, end_index)
print(haystack[starting_index:end_index]) # so no problems but nothing is printed
# so if there is chance of not finding anything we need to check for -1
if starting_index != -1:
    print(haystack[starting_index:end_index])

# we have an alternative to find method - index method
# main difference is that index method will raise an exception if substring is not found
# we would use it with try except block
try:
    print(haystack.index(needle))
except ValueError:
    print(f"Did not find {needle} in {haystack}")

needle = "pel"
try:
    print(f"Found {needle} at index {haystack.index(needle)}")
except ValueError:
    print(f"Did not find {needle} in {haystack}")

# how about counting substrings in a string?
# i do not like it because it skips overlapping substrings
a_string = "aaaaabdfa"
print(a_string.count("aa")) # 2 ! not 4
print(a_string.count("a")) # 6 which is correct 

# much more useful is replace method
# since strings are immutable we cannot change them but we can return a new string
# with replaced characters

food = "auzu putra ar kartupeli"
# changing single letter will not work because strings are immutable
# food[0] = "b" # TypeError: 'str' object does not support item assignment
try:
    food[0] = "b"
except TypeError as err:
    print("Strings are immutable cannot change them", err)

# we can replace a substring with another substring
new_food = food.replace("auzu", "baltu")
print(food) # unchanged
print(new_food) # changed
# i can change all occurrences of a substring
new_food = food.replace("u", "y")
print(new_food) # changed
# i can change only first two occurrences of a substring
new_food = food.replace("u", "y", 2)
print(new_food) # changed

# how about when we want to change first 4 letters of a string with something else
# we use slicing
new_food = "Baltā" + food[4:] # so we add Baltu and then add the rest of the string starting with 5th character
print(new_food)
# similarly we can change at the end
new_food = food[:-2] + "ļiem" # so we cut off last 2 characters and add new ones
print(new_food)

# if we know how to change first and last characters we can change any substring

# let's change 10th character to say 3 XXX characters
new_food = food[:9] + "XXX" + food[10:]
print(new_food)
# i could have saved any of these changes in original variable then the original would be lost
# food = food[:9] + "XXX" + food[10:] # would destroy original food

# let's work with some case changing methods

cats = "Kakis ir kaķis Rīgas centrā"
# we can yell with upper method
print(cats.upper()) # KAKIS IR KAĶIS RĪGAS CENTRĀ
# capitalize will capitalize first letter only!
print(cats.capitalize()) # Kakis ir kaķis rīgas centrā - note Rīgas is not capitalized
# so we have lower method
print(cats.lower()) # kakis ir kaķis rīgas centrā
# again if we need to save these changes we need to assign them to a variable or overwrite original
# cats = cats.lower() # would destroy original cats
lower_cats = cats.lower()
print(lower_cats)
# we also have title method which will capitalize first letter of each word
print(cats.title()) # Kakis Ir Kaķis Rīgas Centrā - English title case 
# less common we have swapcase method - switches upper to lower and vice versa
print(cats.swapcase()) # kAKIS IR KAĶIS rĪGAS CENTRĀ

# we can also check if a string starts with a substring
print(cats.startswith("Kakis")) # True
# compare with in
print("Kakis" in cats) # True also true but not as specific
# similarly we can check if a string ends with a substring
print(cats.endswith("centrā")) # True
# again compare with in
print("centrā" in cats) # True also true but not as specific

# we can combine let's say we are not sure if words is upper or lower case but we want to check start
word = "kAkis"
print(word in cats) # False
# we can loosen up the check with lower
print(word.lower() in cats.lower()) # True
# we can also check begging
if cats.lower().startswith(word.lower()): # so called normalization
    print(f"Ignoring case... {cats} starts with {word}")

# could be useful for checking input (y/n) or (yes/no) or (true/false)
# we can normalize input and then check
answer = "Yeah I want out"
if answer.lower().startswith("y"):
    print("You said y something")
# original answer is not changed
print(answer)

# let's clean a dirty string
dirty_city = "  \tRīga    \n"
print(dirty_city)

# i can use strip method to remove whitespace from both ends
clean_city = dirty_city.strip()
print(clean_city)
# i can clean left side with lstrip
clean_city = dirty_city.lstrip()
print(clean_city)
# i can clean right side with rstrip
clean_city = dirty_city.rstrip()
print(clean_city)

# strip also takes custom characters to strip
letters = "aaaaaa kākis mans aaaāāā"
print(letters.strip("aā")) # kākis mans
# compare with replace strip stops when it encounters a character not in the list

# more general we can use translate method
# easier is to just use a for loop

bad_chars = "!@#$%^&*()_+" # could use string.punctuation instead
text = "This is a (dirty) string!@#$%^&*()_+ F!!!"
print(text)
for char in bad_chars:
    text = text.replace(char, "") # so I keep overwriting text with new text and replacing bad chars with nothing
print(text) # This is a dirty string cleaned

# we have some isalpha , isdigit, isalnum methods, isspace methods

my_string = "Valdis 123 🍺"
print("char", "isalpha", "isdigit", "isalnum", "isspace", sep="\t")
for c in my_string:
    print(c, c.isalpha(), c.isdigit(), c.isalnum(), c.isspace(), sep="\t")

print("*"*40)	
# then we have center method for padding -tapsēšana
name = "Valdis"
print(name.center(20)) # so we add 20 characters and center name in the middle 7 + 6 + 7
# i can choose custom fill
print(name.center(20, "#")) # so we add 20 characters and center name in the middle 7 stars + 6 + 7 stars

# there is also zfille method for padding with zeros