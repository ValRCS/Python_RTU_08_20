# Let's talk about strings
# string concatenation
print("Hello String Fun!" + " " + "Hello String Fun!")

food = "pizza"
print(food)
drink = "water"
print(drink)

# strings are immutable - meaning they cannot be changed
# we can reassign a variable to a new string
food = "pasta"
print(food)

# string delimiter
# single quotes
print('Hello World')
# double quotes
print("Hello World")
# in Python there is no difference between single and double quotes
# use those that are more convenient for you
# if you need single quotes inside a string, use double quotes to delimit the string
print("I'm a string with a single quote inside")
# if you need double quotes inside a string, use single quotes to delimit the string
print('I"m a string with a double quote inside')
# how about when we need both single and double quotes inside a string?
# use triple quotes to delimit the string
triple_quote_string = """I'm a string with
 a single quote inside and 
 "I'm a string with a double quote inside" 
 and I can span multiple lines"""
print(triple_quote_string)

# i could also use triple single quotes for the same effect

# then we have f-strings for string interpolation - formatting
# since Python 3.6+

name = "Valdis"
age = 99 # ok I am not that old
print(f"Hello, my name is {name} and I am {age} years old")

# we can use f-strings to do calculations
# any valid Python expression can be used inside the curly braces
print(f"Next year I will be {age + 1} years old")

# we can also format numbers inside f-strings
PI = 3.141592653589793238462643383279502884197169399375105820974944592307816406286
print(f"Pi is {PI:.2f}")
print(f"Pi is {PI:.4f}")

# we can also use f-strings to format dates
from datetime import datetime
today = datetime.now()
print(today) # full date and time
print(f"Today is {today:%Y-%m-%d}")

# also we can use f-strings in triple quotes
# this is useful for longer strings
city = "Rīga"
print(f"""Hello, my name is {name} 
      and I am {age} years old)
        and I live in {city}""")

# now let's talk about escaping characters
# we can use backslash to escape characters
# \n - newline
# \t - tab
# \\ - backslash
# \' - single quote
# \" - double quote
# less common
# \b - backspace
# \r - carriage return
# \f - form feed

# full documentation here: https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
escaped_string = "I am a string newline \n and with tab \t a \"double quote\" inside"
print(escaped_string)

# finally we have raw strings
# raw strings are prefixed with r
# raw strings are useful when we want to ignore escape characters

raw_string = r"I am a string newline \n and with tab \t a \"double quote\" inside"
print(raw_string)
# raw strings are also useful for things like regular expressions
# raw strings are also useful for file paths in Windows
# for example: D:\Github\Python_RTU_08_20\Diena_1_4_thonny\grupa_j6\chapter_5_strings
