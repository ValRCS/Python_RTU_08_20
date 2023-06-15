# we have various built in methods for strings

# let's check for existence of a substring

haystack = "kartupelis"
print("kart" in haystack)
print("kart" not in haystack)

needle = "kart"
if needle in haystack:
    print(f"Found {needle} in {haystack}")
else:
    print(f"Did not find {needle} in {haystack}")

needle = "art"
if needle in haystack:
    print(f"Found {needle} in {haystack}")
else:    
    print(f"Did not find {needle} in {haystack}")

# then we have string comparison - lexicographical order!
# so we compare character by character
# if first character is the same then we compare second character
# if second character is the same then we compare third character
# we use Unicode code point values for comparison
# so we compare the integer values of the characters

print(f"Compare 'a' and 'b' {ord('a')} {ord('b')}", 'a' < 'b')
print("Valdis" < "Voldemars") # again because of Unicode code points
print("Valdis" < "valdis") # again because of Unicode code points
# upper case letters are before lower case letters

# again if we need to compare length we can use len function
print(len("Valdis") < len("Voldemars"))

# now let's talk about finding substrings
# we can use find method

print(haystack.find("art"))
# so find returns the index of the first character of the substring
print(haystack.find("tel")) # -1 means not found

# how about tupelis in kartupelis?
print(haystack.find("tupelis"))

# we also have index method
print(haystack.index("tupelis"))
# difference between find and index is that index will throw an error
# if substring is not found

# print(haystack.index("tel")) # this will throw an error
try:
    print(haystack.index("tel"))
except ValueError as err:
    print("ValueError", err)

# so now let's look at count
print(haystack.count("tupelis"))

# count uses non-overlapping substrings!!
print("aaaa".count("aa")) # 2 not 3 !

# replace is much more useful
my_karkakis = haystack.replace("tupelis", "kakis")
print(my_karkakis)
# i can change all k to capital K
print(my_karkakis.replace("k", "K"))
# if i want to save the result i need to assign it to a variable
my_karkakis = my_karkakis.replace("k", "KK") # i overwrite my_karkakis

# we can also use replace to remove characters
print(my_karkakis.replace("K", "")) # again save to a variable if needed

# we can also use replace to remove substrings
print(haystack.replace("kartu", "")) # again save to a variable if needed

# we can specify how many times we want to replace
print("abbbbba".replace("b", "c", 3)) # only first three
# again save to a variable if needed

cat_string = "Raibi Runči Rīgā Rūc riktīgi"
print(cat_string)
# we lowercase everything
print(cat_string.lower())
# uppercase - YELLING
print(cat_string.upper())
# we can capitalize first letter - rest will be lowercased
print(cat_string.capitalize())
# we can title case - every word will be capitalized
print(cat_string.title())
# rarely used but we can swap case
print(cat_string.swapcase())
# again save results to a variable if needed
cat_yell = cat_string.upper()

# we can also clean up whitespace
dirty_city = "  Rīga  \n\t  \t"
# print(dirty_city)
print(dirty_city.strip()) # removes whitespace from both ends
print(dirty_city.lstrip()) # removes whitespace from left end
print(dirty_city.rstrip()) # removes whitespace from right end
# again i can save results to a variable if needed
clean_city = dirty_city.strip()

# we also have methods too check if string starts or ends with something
print("Valdis".startswith("Val"))
print("Valdis".endswith("dis"))
print("Valdis".endswith("dis!"))
# compare with in operator

# finally we can check each character in a string

my_string = "Valdis 123 🧑‍🏫"

for character in my_string:
    if character.isalpha():
        print(f"{character} is a letter")
    elif character.isdigit():
        print(f"{character} is a digit")
    elif character.isspace():
        print(f"{character} is a space")
    else:
        print(f"{character} is something else")

print("Valdis".center(20)) # we can center a string with default fillchar
print("Valdis".center(20, "*")) # we can center a string