# what else can we do with strings?

# we can check for existence of a substring in a string
# we can use in operator to check for existence of a substring in a string

target = "potatoes"
print("checking for pot in potatoes", "pot" in target) # True
print("checking for tat in potatoes", "tat" in target) # True	
print("toes" in target) # True
print("toe" in target) # True
print("to" in target) # True
print("t" in target) # True

print("tomatoes" in target) # False
print("tom" in target) # False

# typically we could have a needle variable and a haystack variable
# needle is the substring we are looking for
# haystack is the string we are looking in

# for example
needle = "pot"
haystack = "potatoes"
print(needle in haystack) # True
is_needle_in_haystack = needle in haystack
print(f"So is {needle} in {haystack}?", is_needle_in_haystack)

# so we can use this for if statements

# also we have comparison operators for strings

# by default strings are compared alphabetically - lexicographically
# so we can use <, >, <=, >=, ==, !=
# for example

print("apple" < "banana") # True
print("Valdis" < "potatoes") # True - why? V is before p in alphabet ascii table
print("Valdis" < "valdis") # True - why? V is before v in alphabet ascii table

# so to compare by length we need to use len function
print(len("Valdis") < len("potatoes")) # True

# we can also use find method to find index of a substring in a string
# find returns the index of the first occurrence of the substring in the string

index_of_toes = "potatoes".find("toes") # 4
print(f"Index of toes in potatoes is {index_of_toes}")

# how about bad needle?
index_of_bad = "potatoes".find("bad") # -1
print(f"Index of bad in potatoes is {index_of_bad}")

# we also have index method which is similar to find but it raises an error if substring is not found
print("potatoes".index("toes")) # 4
# so we would use try except for uncertain cases
try:
    print("potatoes".index("bad")) # ValueError: substring not found
except ValueError:
    print("substring not found")
# let's look at some more string methods

# count
# count returns the number of occurrences of a substring in a string
print("potatoes".count("toes")) # 1
# one detail of count is that it does not overlap!
my_abbbba = "abbbba"
print(my_abbbba.count("bb")) # 2 not 3 as expected

# more useful is replace method
# replace replaces all occurrences of a substring in a string with another substring
print(my_abbbba.replace("bb", "xx")) # axxxxa
print(my_abbbba.replace("bb", "y")) # ayya
print("Voldis Voldemārs".replace("o", "a")) # Valdis Valdemārs
# we can also replace a few times
print("Voldis Voldemārs".replace("o", "a", 1)) # Valdis Valdemārs

# again strings are immutable so replace does not change the original string
# to save use new variable
new_name = "Voldis Voldemārs".replace("o", "a")
print(new_name) # Valdis Valdemārs

cat_string = "Raibi Runči Rīgā rūca rīcīgi"
cat_string_upper = cat_string.upper()
# ALL CAPS is YELLING
print(cat_string_upper) # RAIBI RUNČI RĪGĀ RŪCA RĪCĪGI 
# so lower
print(cat_string_upper.lower()) # raibi runči rīgā rūca rīcīgi
# we have also capitalize
print("capitalize", cat_string.capitalize()) # Raibi runči rīgā rūca rīcīgi
# note only the first letter is capitalized
# we can also title
print("title", cat_string.title()) # Raibi Runči Rīgā Rūca Rīcīgi
# more rare is swapcase
print("swapcase", cat_string.swapcase()) # rAIBI rUNČI rĪGĀ RŪCA rĪCĪGI

# again if we need to save we need to use a new variable

my_city = "   \t  Rīga \t \t"
print(my_city) #      Rīga
print(my_city.strip()) # Rīga without whitespace around
print(my_city.lstrip()) # Rīga without whitespace on the left
print(my_city.rstrip()) # Rīga without whitespace on the right

# lets loop through our string and check whether each character is
# a letter or a digit
# we can use isalpha and isdigit methods

my_string = "Valdis 123 🥔"
for char in my_string:
    if char.isalpha():
        print(f"Letter {char}")
    elif char.isdigit():
        print(f"Digit {char}")
    elif char.isspace():
        print(f"Space {char}")
    else:
        print(f"Other {char}")

# we can also check for whitespace

