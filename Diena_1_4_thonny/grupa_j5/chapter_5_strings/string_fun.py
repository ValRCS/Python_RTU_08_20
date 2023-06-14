# let's talk about strings in Python
print("Hello strings!"  + " " + "Hello strings again!")

food = "pizza"
print(food)
drink = "beer"
print(drink)

# strings are immutable - we cannot change them
# we can only create new strings

# strings are delimited by single or double quotes or triple quotes
# triple quotes are used for multi-line strings

# we can use f-strings to format strings

# let's start with single and double quotes
# there is no difference between single and double quotes in Python
# we can use both of them to create strings
# single quotes
single_quotes = 'single quotes'
print(single_quotes)
double_quotes = "double quotes"

# we can use double quotes inside single quotes
single_quotes_with_double_quotes = 'single quotes with "double quotes"'
print(single_quotes_with_double_quotes)

# we can use single quotes inside double quotes
double_quotes_with_single_quotes = "double quotes with 'single quotes'"
print(double_quotes_with_single_quotes)

# what can we do when we need both double and single quotes inside a string?
# we can use triple quotes
triple_quotes = """triple quotes with 'single quotes' 
and 
"double quotes" 
and so on"""
print(triple_quotes)

# we could use triple single quotes
triple_single_quotes = '''triple quotes with 
'single quotes' '''	
print(triple_single_quotes)

# then we have f-strings
# f-strings are used to format strings
# we can use f-strings to insert variables into strings
# we can use f-strings to insert expressions into strings

# let's start with variables
name = "Valdis"
age = 42

# we can use f-strings to insert variables into strings
# we use curly braces to insert variables into strings
# we use f before the string to indicate that it is an f-string

greeting = f"Hello, {name}! are you really {age} years old?"
print(greeting)

# we can use f-strings to insert expressions into strings
# we can use any valid Python expression inside curly braces
# for example, we can use arithmetic expressions
greeting = f"Hello, {name}! are you really {age + 100} years old?"
print(greeting)

# we can also format numbers inside f-strings

# we can use f-strings to format numbers

PI = 3.141592653589793238462643383279502884197169399375105820974944592307816406286
# we can't really store that much precision in a float... even though it looks like we can
# let's only show last 6 digits of PI
formatted_pi = f"PI is {PI:.6f}"
print(formatted_pi) # PI itself is not changed!

# let's talk about escape characters
# escape characters are used to insert special characters into strings
# for example, we can use escape characters to insert newlines into strings

# we use \n to insert a newline into a string
# we use \t to insert a tab into a string
# we use \\ to insert a backslash into a string
# we use \' to insert a single quote into a string
# we use \" to insert a double quote into a string
# more rarely used escape characters
# we use \r to insert a carriage return into a string
# we use \b to insert a backspace into a string - very rarely used
# we use \f to insert a form feed into a string - very rarely used

escaped_string = "this string has a \nnewline"
print(escaped_string)
escaped_string_with_everything = "this string has a \nnewline and a \ttab and a \\backslash \nand a \'single quote \nand a \"double quote"
print(escaped_string_with_everything)

# personally I like to use triple quotes to avoid escaping characters


# we can also use raw strings
# raw strings are prefixed with r
# raw strings are used to avoid escaping characters
# for example, we can use raw strings to avoid escaping backslashes
# useful for regular expressions for example
# also for file paths in Windows
raw_string = r"raw string with \my backslash"
# otherwise we would have to write \\my backslash instead
print(raw_string)