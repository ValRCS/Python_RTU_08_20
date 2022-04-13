import string # has some useful constants
print("Having fun with string")
food = "Pizza"
print(food) 
print(food[0])  # string indexes start at 0
# print(food[1])  # un/commenting in VS Code is with ctrl+/ (cmd+/ on Mac)

food = "kartupelis" # string is immutable but we can overwrite it
print(food)

food_len = len(food)
print(food_len) # string length
print(food[9]) # string indexes start at 0 so 10th character has index 9

# How to get last character in general?
print(food[len(food)-1]) # no need for this in Python
print(food[-1]) # last character
print(food[-2]) # second last character

print(food[2])  # so we can print the 3rd character

# out of bounds indeces will raise IndexError
# print(food[10])  # IndexError: string index out of range
print(food[-10]) # not an error, prints first character
# print(food[-11]) # IndexError: string index out of range

# string slicing - next best thing after sliced bread
print(food[0:3]) # prints first 3 characters, 4th character is not included
print(food[:3]) # 0th character is default start index
print(food[3:]) # print starting from 4th character until the end
print(food[3:10]) # print starting from 4th character until the end
print(food[3:9]) # last character is not included with index 9

print(food[-3:]) # prints last 3 characters

# i can use out of bounds indexes with slicing no errors
print(food[-333:9000]) # prints everything no problems


print(food[5:10], food[5:], food[-5:], sep="\n")  # sep is a separator, single space is default

food = "Auzu putra ar krējumu"
print(food)
print(food[5:10], food[5:], food[-5:], sep="\n") 

alphabet = string.ascii_lowercase
print(alphabet)

start = 3
end = 15
step = 2
print(alphabet[start:end])  # default step is 1
print(alphabet[start:end:step])  # full slicing syntax
print(alphabet[::2]) # every other character
print(alphabet[1::2]) # every other character starting from 2nd

reverse_alphabet = alphabet[::-1] # reverse alphabet
print(reverse_alphabet)

# when to use " and when to use '
my_string = "I'm a string" # so we can use " when we want ' inside our string
print(my_string)
my_other_string = 'I\'m a string said Alice to Tortoise "Run!" ' # so we can use ' when we want " inside our string
string_with_escaped_chars = "\t\tAha \" \' \n\t\\ \\ \t \n and so on"
print(string_with_escaped_chars)
multi_line_string = """I can write anything
over multiple lines 
and I can use \n new line
I can use " and '
and I can use \t tab and son
""" # ends the multiline string with triple quotes
print(multi_line_string)

print(min(alphabet), max(alphabet), len(alphabet)) # min and max and length
print(min(food), max(food), len(food)) # min and max and length
print(ord(" "), ord("e"), ord("ē")) # ordinal number of a character - Unicode

print("Valdis" < "Voldemars") # lexicographical order
print("Valdis" < "Voldis") # lexicographical order
print("Valdis" < "Vol") # lexicographical order
# by length
print(len("Valdis") < len("Voldemars"))	# by length

# membership operator
print("al" in "Valdis")
print("putra" in food)

print(food.index("putra")) # index of first occurence of a substring
# throws error if substring is not found
# print(food.index("Neputra")) # ValueError: substring not found
print(food.find("putra")) # returns -1 if substring is not found
print(food.find("Alus")) # returns -1 if substring is not found

print(food.count("a")) # counts occurences of a substring
# count is picky it only counts non-overlapping occurences
print("AAAA".count("AA")) # counts 2 occurences - not three

print(food.replace("putra", "alus")) # replaces all occurences of a substring
new_food = food.replace("putra", "alus") # to save the results of my replace
print(new_food)

print(new_food.capitalize()) # capitalizes first letter
print(alphabet.capitalize()) # capitalizes first letter
print(new_food.upper()) # capitalizes all letters YELLING
print(new_food.lower()) # lowercases all letters whispering
print(new_food.title()) # capitalizes first letter of every word
print(new_food.swapcase()) # swaps case of all letters


# food[5] = "Z" # string is immutable, so we can't change individual characters
# string concatenation
print(food[:5])
print(food[5])
print(food[6:])
print(food[:5] + food[5] + food[6:])
print(food[:5] + "ZZ" + food[6:])
print(food[:10] + "oXo" + food[2:])  # i can slice and dice
# f-strings are a new way to concatenate strings in Python 3.6
print(f"{food[:5]}ZZ{food[6:]}")

# looping through strings
for char in food:
    print(char)

# finding needle in string and making new string
needle = "u"
new_string = ""  # typical to start with empty string
replacement_string = "_"
for char in food: # instead of char i could call it c, n, etc.
    if char == needle:
        new_string += replacement_string  # this is a bit slow on large strings
    else:
        new_string += char  

print(new_string)

c = "z"
print(c.isalpha()) # is it a letter?
c = "ķ"
print(c.isalpha() or c.isspace()) # is it a letter or space?
c = " "
print(c.isspace()) # is it a space?