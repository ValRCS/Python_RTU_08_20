# let's see about string methods

# first how to check for existance of substring in string

haystack = "kartupelis"
needle = "tup"
print(needle in haystack) # True
print("tup" in "kartupelis") # True

# let's change our needle
needle = "tupi"
if needle in haystack:
    print(f"Found {needle} in {haystack}")
    # then we could proceed with further processing
else:
    print(f"Did not find {needle} in {haystack}")
    # then we could do something else

# since single character is also string we can check for it
print("t" in "kartupelis") # True

# string comparison
# we can compare strings
# lexigraphical comparison
# we compare strings character by character
# first we compare first characters
# if they are equal we compare second characters
# if they are equal we compare third characters
# and so on
print("a" < "b") # True
print("a" < "A") # False
# why false?
# because "a" is not less than "A" in ASCII table
print(ord("a")) # 97
print(ord("A")) # 65
# thus "a" is less than "o" because 97 < 111
print("Valdis" < "Voldemars") # True

# if we want by length we can use len()
print(len("Valdis") < len("Voldemars")) # True

# how about finding exactly where substring is in string?
# we have two methods
# find() and index()

# find() returns index of first occurance of substring
# or -1 if substring is not found
print("kartupelis".find("tup")) # 3 because 4th character is the start
print(haystack.find(needle)) # -1 because "tupi" is not in "kartupelis"
needle = "tup"
print(haystack.find(needle)) # 3 because "tup" is in "kartupelis"
# how about ka
print(haystack.find("ka")) # 0 # because ka is at the start
# how about elis
print(haystack.find("elis")) # 6 # because elis starts at 7th character

if haystack.find(needle) != -1:
    print(f"Found {needle} in {haystack}")
    # then we could proceed with further processing
else:
    print(f"Did not find {needle} in {haystack}")
    # then we could do something else

# alternatively we can use index()
# index() will raise ValueError if substring is not found
# otherwise it will return index of first occurance of substring
try:
    print(haystack.index("tupi"))
except ValueError as e:
    print("Oooops!", e)

# then we have count() method
# count() will return how many times substring is found in string
print(haystack.count("tup")) # 1
# how about a in abracadabra
print("abracadabra".count("a")) # 5
# count is case sensitive
# count skips overlapping substrings!!
print("aaaaa".count("aa")) # 2 why 2 ? because aa overlaps
# personally i would expect 4 but that's not how it works

# next we have replace() method
# much more useful than count()

# again strings themselves are immutable
# i can't change string in place
name = "Valdis"
# name[0] = "K" # this will not work
food = "auzu putra ar sviestu"
# let's change all u to y
new_food = food.replace("u", "y")
print(new_food) # ayzy pytra ar sviesty
# i can replace multiple characters with multiple characters
new_food = food.replace("au", "AU")
print(new_food) # AUzu putra ar sviestu

# i can also specify how many times to replace
new_food = food.replace("u", "y", 2) # so only first two u's will be replaced
print(new_food) # ayzy putra ar sviestu

# so what do we do when we want to replace first character of string but keep the rest?
# we can use slicing
print(name[1:]) # aldis
prefix = "Visv"
print(prefix + name[1:]) # Visvaldis

# how about if we want to replace 3rd letter with something else?
# we can use slicing again
# so we slice first 2 letters and then add our replacement and then add the rest of the string
print(name[:2] + "Z" + name[3:]) # VaZdis
# i could also keep everything and insert a new character
# here i have slice of first 3 letters and then i add my new character and then i add the rest of the string
print(name[:3] + "Z" + name[3:]) # ValZdis
# i could save this to a new variable
new_name = name[:2] + "ZZZ" + name[2:]
print(new_name) # VaZZZldis

# let's get a cat string
cats = "Raibi runči Rīgā rūc" # note that we have both upper and lower case letters
print(cats)

# we can lowercase everything
print(cats.lower()) # raibi runči rīgā rūc
# note lower does not change original string
# if you need to change original string you need to reassign it
# cats = cats.lower() # we would overwrite original string
new_cats = cats.lower()
print(new_cats) # raibi runči rīgā rūc

# if we have lower case string we can uppercase it
print(new_cats.upper()) # RAIBI RUNČI RĪGĀ RŪC - we are yelling now

# also have capitalize() method
# capitalize() will capitalize first letter of string only rest will be lowercased
print(new_cats.capitalize()) # Raibi runči rīgā rūc

# we also have title() method for capitalizing first letter of EACH word
print(new_cats.title()) # Raibi Runči Rīgā Rūc

# we can also swap case for ALL letters - less common
print(cats.swapcase()) # rAIBI RUNČI rĪGĀ RŪC

# we can also strip whitespace from start and end of string
dirty_city = "   \tRīga   \t\t\n"
print(dirty_city)

# we can use strip() method to remove whitespace from start and end
print(dirty_city.strip()) # Rīga
clean_city = dirty_city.strip()
print(clean_city) # Rīga no newlines or tabs or whitespace
# we can also clean just one side
print(dirty_city.lstrip()) # Rīga   \t\t\n
print(dirty_city.rstrip()) #    \tRīga

# we can also remove specific characters from start and end
# we can specify which characters to remove
# we can also specify how many characters to remove
# we can also specify which side to clean

# let's say we want to remove all "a" and "i" from start and end of string
print("aaaaiiiiiValdisiiiiiaaaaa".strip("ai")) # Valdis
# we can also specify which side to clean with rstrip() and lstrip()

print(cats.strip()) # will not remove whitespace in the middle!!
# instead replace() is better for that
print(cats.replace(" ", "")) # RaibirunčiRīgārūc # we replace all spaces with nothing!

# how about if we wanted to clean some bad characters from string?
# we could use a loop
bad_chars = ".,;:!?-" # could use string.punctuation
dirty_text = "This is a dirty text, with --- some punctuation; and other stuff!"
print(dirty_text)
# we iterate over bad_chars and replace them with nothing
for bad_char in bad_chars:
    dirty_text = dirty_text.replace(bad_char, "")
    # so i keep replacing bad characters with nothing
print(dirty_text) # This is a dirty text with some punctuation and other stuff
# alternative would be to use translate() method

print(name)

# i can check start and end of string for specific substring
print(name.startswith("Val")) # True
# compare with in operator which would look for substring anywhere in string
print("Val" in name) # True

# we can also check end of string
print(name.endswith("dis")) # True


# with this new knowledge we can have a nicer user experience for input
# we can let users enter any word in any case as long as it starts with Y or N
# we can then lowercase the input and check if it starts with y or n

# user_input = input("Do you want to continue? (Y/N) ")
# print(user_input)
# if user_input.lower().startswith("y"):
#     print("You said some text that starts with y or Y")
# else:
#     print("You said something else", user_input)
# # note user_input is not changed!
# print(user_input)

# we can also check if string is alphanumeric and is digit or is alpha or space
my_string = "Valdis 123 🍺"
for c in my_string:
    print(c, c.isalnum(), c.isdigit(), c.isalpha(), c.isspace())

# we also have center() method
# we can specify how long we want our string to be
# we can also specify what to fill the rest of the string with
print(name.center(20)) #     Valdis # 7 spaces + 6 letters + 7 spaces = 20
print(name.center(20, "*")) # ******Valdis****** 7 + 6 + 7 = 20