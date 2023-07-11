# Let's talk about strings in Python
print("Let's have some fun with strings!")
# what are strings after all?
# strings are a sequence of characters
# Python does not have character data type
# single character is a string of length 1

# strings in Python are immutable
# this means that once a string is created, it cannot be changed
# if we need to change a string, we need to create a new string
# we could do it by adding two strings together or by using string methods

# let's make some strings
food = "kartupelis"
# drink = "alus"
drink = "kefīrs"

# let's print them
print(food)
print(drink)

# string concatenation
# we can add two strings together
print(food + " goes well with " + drink)

# we can also multiply a string by a number
print(food * 3)
# there is no - or / for strings

# we have f-strings
# f-strings are a way to format strings
print(f"{food} goes well with {drink}")

# single quotes vs double quotes
# in Python we can use both single and double quotes to create strings
# there is no difference between them

# when to use one or the other?
# try to be consistent

# for convenience, we can use single quotes when we have double quotes inside
# and vice versa
# for example
print("I'm a string") # single quote did not need to be escaped
# vice versa
print('He/She said: "I\'m a string"') # double quote did not need to be escaped

# what characters can be escaped?
# full list can be found here: https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals

# common escape characters
# \n - new line
# \t - tab
# \\ - backslash - important for file paths
# \' - single quote
# \" - double quote
# example with all of the above
print("This is a string\nwith a new line\tand a tab \t and a backslash\\and a single quote\'and a double quote\"")

# uncommon escape characters
# \a - bell
# \b - backspace
# \f - form feed
# \r - carriage return

# we have raw strings - for times when we don't want to escape anything
# raw strings are created by prefixing the string with r
# example
print(r"This is a string\nwith a new line\tand a tab \t and a backslash\\and a single quote\'and a double quote\"")

# where could we use raw strings?
# file paths
# regular expressions - saves space because regular expressions use a lot of backslashes already

# we have multiline strings - for times when we want to write a string on multiple lines without using \n
# multiline strings are created by using triple quotes - """ or ''' - no difference between them
# example
print("""This is a string
with a new line
      some tab \t some text 
and a backslash\\and a single quote\'and a double quote\"
      and so on""")

# i can use f-strings with multiline strings to insert variables and expressions
# example
name = "Valdis"
age = 49
print(f"""Hello, my name is {name}
I am {age} years old
and I like to eat {food}
and drink {drink}""")

# during all of this I could have saved any of the strings to a variable
# example
my_greeting = f"""Hello, my name is {name}
I am {age} years old
and I like to eat {food}
and drink {drink}"""
# then i could do something else
# and print it at some point or do something else with it
print(my_greeting)

# again strings in Python have full Unicode support
# this means that we can use any characters from any language
