import string
# from this import d # has some useful constants
# # # https://docs.python.org/3/library/string.html
# print("Having fun with string")
food = "Pizza"
drink = "Coffee"
# print(food) 

# strings are delimited by " or ' or """ or ''' - triple quotes are multiline strings
# string_example = "I'm a string" # notice the ' inside the string	
# string_example_2 = 'I\'m a string' # notice the \' inside the string - escape character
# print(string_example)
# print(string_example_2)

# # we could use single quotes to delimit string with double quotes inside
# string_example_3 = 'I\'m a string "said Alice to Tortoise" "Run!" ' # notice the \' inside the string - escape character
# print(string_example_3)

# # we can use triple quotes to delimit strings with single and double quotes inside
# string_example_4 = """I'm a string "said Alice to Tortoise" "Run!" """
# print(string_example_4)
# # i can also use newlines and tabs and other special characters
# string_example_5 = """I'm a string "said Alice to Tortoise" "Run!"
# \t\tAha \" \' \n\t\\ \\ \t \n and so on
#   dadfkjalkdfjal Varu rakstīt ko vēlos vairākās rindās
#     un varu izmantot \n jaunu rindu
# """
# print(string_example_5)

# full list of escape characters
# https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals


# print(food[0])  # string indexes start at 0 - so careful with off by one errors
# print(food[1])  # un/commenting in VS Code is with ctrl+/ (cmd+/ on Mac)
# first_letter = food[0]  # save first letter to a variable
# print(first_letter)

# food = "kartupelis" # string is immutable but we can overwrite it
# print(food)

# food_len = len(food)
# print(food_len) # string length
# print(food[9]) # string indexes start at 0 so 10th character has index 9

# # # # # How to get last character in general?
# print(food[len(food)-1]) # no need for this in Python - anti-pattern avoid!
# print(food[-1]) # last character Python has secondary indexing from the end
# print(food[-2]) # second last character
# print(food[-10]) # 10th from the end

# # # print(food[2])  # so we can print the 3rd character

# # # # # out of bounds indeces will raise IndexError
# try:
#     print(food[10])  # IndexError: string index out of range we do not have 11th character
# except IndexError:
#     print("Oopps! IndexError: string index out of range")
# print(food[-10]) # not an error, prints first character
# try:
#     print(food[-11]) # IndexError: string index out of range
# except IndexError:
#     print("Oopps! IndexError: string index out of range")
# # # print(food[-11]) # IndexError: string index out of range

# food = "kartupelis"

# # # # # string slicing - next best thing after sliced bread
# print(food[0])
# print(food[3]) # 4th character
# print(food[0:3]) # prints first 3 characters, 4th character is not included
# print(food[:3]) # 0th character is default start index
# print(food[3:]) # print starting from 4th character until the end
# prefix = food[:3] # save the slice to a variable
# postfix = food[3:] # save the slice to a variable
# print(prefix + postfix) # concatenation
# print(food[:3] + food[3:]) # concatenation -> kartupelis
# print(food[3:10]) # print starting from 4th character until the end
# print(food[3:9]) # last character is not included with index 9
# print(food[3:-1]) #print starting from 4th character until the end but not including last character

# print(food[:-3]) # prints everything except last 3 characters
# print(food[-3:]) # prints last 3 characters

# # # # # i can use out of bounds indexes with slicing no errors
# print(food[3:50000])
# print(food[-5555:5])
# print(food[-333:9000]) # prints everything no problems


# print(food[5:10], food[5:], food[-5:], sep="\n")  # sep is a separator, single space is default

food = "Auzu putra ar krējumu"
# print(food)
# print(food[5:10], food[5:], food[-5:], sep="\n") 

alphabet = string.ascii_lowercase
print(alphabet)
print(len(alphabet))

## Let's slice the alphabet	
start = 3
end = 15
step = 2
print(alphabet[start:end])  # default step is 1
print(alphabet[start:end:step])  # full slicing syntax
print(alphabet[::2]) # every other character from start until the end
print(alphabet[::3]) # every third character from start until the end
print(alphabet[1::2]) # every other character starting from 2nd until the end

reverse_alphabet = alphabet[::-1] # reverse alphabet Pythonic way
print(reverse_alphabet)
print(alphabet[::-2]) # every other character starting from last


# # # # when to use " and when to use '
# my_string = "I'm a string" # so we can use " when we want ' inside our string
# print(my_string)
# my_other_string = 'I\'m a string said Alice to Tortoise "Run!" ' # so we can use ' when we want " inside our string
# print(my_other_string) 
# string_with_escaped_chars = "\t\tAha \" \' \n\t\\ \\ \t \n and so on"
# print(string_with_escaped_chars)
# multi_line_string = """I can write anything
# over multiple lines 
# and I can use \n new line
# I can use " and '
# well if I need triple quotes then I can write ""\"
# { just regular brackets no special meaning }
# and I can use \t tab and son
# """ # ends the multiline string with triple quotes
# print(multi_line_string)
multi_line_with_template = f"""
I like {food}
    I like to drink {drink}
I can write anything"""
print(multi_line_with_template)

print(min(alphabet), max(alphabet), len(alphabet)) # min and max and length
print(min(food), max(food), len(food)) # min and max and length
# ascii table https://en.wikipedia.org/wiki/ASCII
print(ord(" "), ord("e"), ord("ē"), ord("😁")) # ordinal number of a character - Unicode

print("Valdis" < "Voldemārs") # why? lexicographical order

print("Valdis" < "Voldis") # lexicographical order
print("Valdis" < "Vol") # lexicographical order
# # # # by length
print(len("Valdis") < len("Voldemars"))	# by length

# # # # membership operator
# returns True or False - useful in if statements
print("a" in "Valdis")
print("al" in "Valdis")
print("putra" in food)
print("alus" in food)

print(food)
print(food.index("putra")) # index of first occurence of a substring
# # # # throws error if substring is not found
try:
    print(food.index("Neputra")) # ValueError: substring not found
except ValueError:
    print("Oopps! ValueError: substring not found")
print(food.find("putra")) # returns -1 if substring is not found
print(food.find("Alus")) # returns -1 if substring is not found


print(food.count("a")) # counts occurences of a substring
# # # # count is picky it only counts non-overlapping occurences
print("AAAA".count("AA")) # counts 2 occurences - not three
# # TODO find in stack overflow how to do overlapping counts


print(food.replace("putra", "alus")) # replaces all occurences of a substring
new_food = food.replace("putra", "alus") # to save the results of my replace

beer = "Alus " * 10
print(beer)
beer_replaced = beer.replace("Alus", "Vīns")
print(beer_replaced)
beer_partially_replaced = beer.replace("Alus", "Vīns", 3) # so first three occurences
print(beer_partially_replaced)

print(new_food)
print(type(new_food)) # should be string

print(new_food.capitalize()) # capitalizes first letter
# if i want to save the result of capitalize
# overwriting the old variable
print(new_food)
new_food = new_food.capitalize()
print(new_food)
print(alphabet.capitalize()) # capitalizes first letter
print(new_food.upper()) # capitalizes all letters YELLING
print(new_food.lower()) # lowercases all letters whispering
print(new_food.title()) # capitalizes first letter of every word

print(new_food.swapcase()) # swaps case of all letters
print(new_food.swapcase) # this is a function not a string

try:
    food[5] = "U" # string is immutable, so we can't change individual characters
except TypeError:
    print("Oopps! TypeError: 'str' object does not support item assignment")
# so I need to change or replace the whole string
# # # # string concatenation
print(food[:5]) # first 5 characters
print(food[5]) # 6th character
print(food[6:]) # 7th character and onwards
print(food[:5] + food[5] + food[6:])
print(food[:5] + "ZZzzz..." + food[6:])
new_food_mod = food[:5] + "ZZzzz..." + food[6:]
print(new_food_mod)
# print(food[:10] + "oXo" + food[2:])  # i can slice and dice
# # # # f-strings are a new way to concatenate strings in Python 3.6
print(f"{food[:5]}mynewcharacters{food[6:]}")
# my slices can be overlapping
print(f"{food[:5]}mynewcharacters____{food[2:]}")

franken_putra = food.replace("u", "y")
print(franken_putra)

# # looping through strings
for char in food: # char is a name of a variable I came up with
    print(char)
    # so i can do something with this character

# # finding needle in string and making new string
needle = "u"
replacement_char = "_"
new_string = ""  # typical to start with empty string
for char in food: # instead of char i could call it c, n, etc.
    if char == needle:
        new_string += replacement_char  # this is a bit slow on large strings\
        # new_string = new_string + replacement_char # same as above line
    else:
        new_string += char # keep original character 

print(new_string)

# i can also use enumerate to get index and character
# enumerate starts with 0 by default
for index, char in enumerate(alphabet): 
    print(index, char)
    # so i can do something with this character

c = "z"
print(c, "is alpha?", c.isalpha()) # is it a letter?

c = "ķ"
print(c.isalpha() or c.isspace()) # is it a letter or space?
c = " "
print(c.isspace()) # is it a space?

print("Valdis".isalpha()) # is it a letter?
print("3423424".isdigit()) # is it a digit? # could be useful when checking input from user

city = "    Rīga Rīga Rīga  "	
print(city)
clean_city = city.strip() # removes whitespace from beginning and end
print(clean_city)
# there is also lstrip and rstrip for left and right
print(clean_city.lstrip("R")) # removes R from beginning
print(clean_city.rstrip("a")) # removes a from end

# we can use replace to remove all spaces
print(city.replace(" ", "")) # removes all spaces