# we can create variables on the fly
city = "Rīga" # notice we can use Latvian text inside
print("I live in", city) # , separates values and has whitespace by default
print("I live in " + city)
# I like best the modern way since Python 3.6
# f-strings also called string interpolation
print(f"I live in {city}")
my_name = "Valdis"
drink = "beer 🍺"
print(f"My name is {my_name}. I live in {city}. I like {drink}")

# variables should be as short as possible while being descriptive
# multi word variables should be separated with _

# i can change values for variables at any time
drink = "milk 🥛"
print(f"I also like {drink}")

# avoid similar names
# Python rarely uses camelCase
# python uses snake_case
# variables should start with ASCII (english) letter
# can containe upper and lowercase
# can have _
# can have numbers
# still a4 is a bad name for a variable unless you are referring to paper A4
# short names can be used for short sections of code
a = 10
b = a + 25 # this is assignment not an equation
print(f"a is {a} and b is {b}")
b += 100 # same as b = b + 100
print(f"b is now {b}")
# best would be if we knew what a and b represent
current_month = 6 # much better than
c = 6 # much harder to read, is it day what is it?
this_is_my_current_month_for_my_party = 6 # bad name
# one,two words are ideal, 3 to 4 are okay

# if we have two different types we can not add them together
# monster = my_name + a
# i can use + on same types
medium_drink = "Fat-free " + drink
print(f"Cool my new drink {medium_drink}")
big_drink = "beer " * 5 #  a little trick
print(big_drink)

# how about adding a number inside string
# old way
drink_number = "limonāde " + str(10)
print(drink_number)
# f lets us use anything inside {}
formatted_drink = f"My numbered drink is {drink} I have case with {b} of them"
print(formatted_drink)

# i can use multiline string
big_string = """This is a multi line
text I can do whatever I want
👨‍🍼 Father’s Day
"""
print(big_string)

# i can also format multi-line strings
my_greeting = f""" I can write whatever
        My name is {my_name} 

My favorite city is {city}
"""
print(my_greeting)