# Let's talk a little about strings in Python.
# Strings are a sequence of characters.
# Python does not have character data type - just strings of length 1 for characters
# Strings are immutable - we cannot change them in place
# if need to change we need to create a new string

# let's create some strings
food = "potatoes"
drink = 'kvass' # note that single and double quotes are the same
print(food, drink)
# string concatenation
print(food + " goes well with " +  drink) # note spaces in strings

# we can multiply strings
print(food * 3)
# if i wanted space between potatoes I could do this
print((food + " ") * 3)
print(f"{food} " * 3)
# also we have f-strings
print(f"{food} goes well with {drink}")

# when to use double quotes and when single quotes?
# if we need to use single quote in string we can use double quotes
print("I don't like it") # so we can use single quote in double quotes
# when to use single quotes?
# if we need to use double quotes in string we can use single quotes
print('I said "I don\'t like it" inded') # so we can use double quote in single quotes

# notice I used \ to escape the single quote
# full list of escape strings in Python in docs: https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals

# full example of all escape sequences
print("This is a string with \n new line") # common escape sequences
print("This is a string with \t tab")
# \\
print("This is a string with \\ backslash")
# \'	
print("This is a string with \' single quote")
# \"
print("This is a string with \" double quote")

# uncommon escape sequences
print("This is a string with \v vertical tab")
print("This is a string with \b backspace")
print("This is a string with \r carriage return")
print("This is a string with \f form feed")
print("This is a string with \a alert")

# raw strings
# if we do not want to escape anything we can use raw strings
print(r"This is a string with \n new line ' \t \f ") # common escape sequences
# raw strings are useful for regular expressions - which have their own escape sequences

# we also have multiline strings
# we can use triple quotes
print("""This is a multiline string
with multiple lines
and new lines
    and tabs\t and quote " and even double quote "" 
      and backslash and so on
""")

# i could use triple single quotes if for some reason
# i need to use triple double quotes inside

# also we can use f-strings with triple quotes
print(f"""This is my favorite food {food}
      and this is my favorite drink {drink}
""")
