print("Let's use some variables!")
# Python makes it easy, just come up with name and start using it
name = "Valdis" # so variable name is pointing to string literal "Valdis"
print(name)
print("Doing some other stuff")
print("There is that name again", name)
# what are suitable names for variables in Python?
# has to start with lowercase or uppercase letter or _ underscore
# no spaces can use numbers after first character
# a, a1, a100 - ok names but a100 is a bit funny 
# better names have _ between multiple words
# my_name, buyer_name - very typical
# rarely Python projects will have so called camelCase - that is from other languages
# choosing good variable names is one of the most important problems in programming
# if your code is over multiple pages then single character variable names are not recommended
# without functions
# human brain can only hold about 5-9 (usually 7) chunks of information in our short term memory
# no need to add to this complexity
# there are some short variable names that are usually ok
# x,y,z for coordinate variables
# i, j for looping / later on loops
# t for time or temporary
# s for string
# c could be string with one character or could be counter
# a4 would be okay variable for dealing with a4 paper size
# too long is also not recommended
very_long_variable_which_is_too_hard_to_read = 100
print(very_long_variable_which_is_too_hard_to_read)
# let's combine two variables into new variable
university = "RTU"
# i can add literal strings and variables which hold strings
greeting = "I am " + name + " and I work at " + university
print(greeting)
# above is a bit a hard to get right
# so called f-strings make it easier to combine multiple variables
greeting_again = f"I am {name} and I work at {university}"
print(greeting_again)
year = 2024
full_greeting = f"It is year {year} and {university} has a new building"
print(full_greeting)

