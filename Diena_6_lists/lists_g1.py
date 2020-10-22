# # What is a list after all?
# # * ordered
# # * collection of arbitrary objects (anything goes in)
# # * nested (onion principle, Matroyshka)
# # * mutable - maināmas vērtības
# # * dynamic - size can change
my_list = [5, 6, "Valdis", True, 3.65, "alus"] # most common way of creating a list using [el1, el2]
print(my_list)
print(my_list[0])
my_list[1] = "Mr. 50"  # lists are mutable (unlike strings)
print(my_list[:3])
print(my_list[-2:]) # last two
print(my_list[1:4], my_list[1:-1])
print(my_list[::2])
print(my_list[1::2])
print(my_list[-1])
# how to check for existance in list
print(3.65 in my_list)
print(66 in my_list)
print("Valdis" in my_list)
print("al" in my_list)  # this is false
# # # iterate over items
needle = "al" # what we want to find in our list
for item in my_list:
    print("Checking ", item)
    if type(item) == str and needle in item:
        print(f"Found {needle=} in {item=}") # python 3.8 and up
        print(f"Found {needle} in {item}") # for python 3.7

# # #
# my_list.append()
my_list.append("Bauskas alus")
my_list.append("Valmiermuižas alus")  # IN PLACE methods, means we modify the list
print(my_list)

# example how to filter something
find_list = [] # so we have an empty list in beginning
needle = "al" 
for item in my_list:
    # if needle in item: will not work because we have non strings in list
    if type(item) == str and needle in item:
        print(f"Found {needle=} in {item=}")
        find_list.append(item)
print(f"{needle=} found in {find_list=}")
# # ps the above could be done simpler with list comprehension

# # # out of place meaning find_list stays the same
new_list = my_list + ["Kalējs", "Audējs"] # out of place addition, my_list is not modified
print(len(new_list), len(my_list))

# print(f"{str(my_list)}")
# how to convert all values to str
str_list = []
for item in my_list:
    str_list.append(str(item)) # so if item is already string nothing will happen
print(str_list)

# # list comprehensions make it even short
str_list_2 = [str(item) for item in my_list]
print(str_list_2)
print(str_list == str_list_2) # check if lists containe equal values
print(str_list is str_list_2) # check if our variables reference the same list
str_list_3 = str_list # so str_list_3 is a shortcut to same values as
print(str_list == str_list_3, str_list is str_list_3)

# # need needle of course
beer_list = [item for item in str_list if needle in item]
print(beer_list)
beer_list = beer_list[1:] #get rid of Valdis in my beer list
print(beer_list)

beer_list += ["Užavas alus"] # we create a list on demand - list literal beer_list = beer_list + ["Užavas alus"] 
# similar to beer_list.append("Užavas alus")
print(beer_list)

# # new_list += ["Malējs"]  # same as new_list = new_list + ["Malējs"]
# # new_list

print(beer_list[-1])
print(beer_list)
last_beer = beer_list.pop()  # also in place meaning i destroyed the last value
print(f"We took out {last_beer}")
print(beer_list)
beer_list.append(last_beer)
print(beer_list)

print(beer_list.count("alus")) # only exact matches
print(beer_list.index("alus"), beer_list.index("Užavas alus"))
beer_list.extend(["Labietis", "Mālpils alus"]) # again in place
print(beer_list)
has_alus = len([el for el in beer_list if "ž" in el])
print(has_alus)
has_alus = len([el for el in beer_list if "alus" in el])
print(has_alus)

beer_list.insert(2, "Cēsu sula") # so it will insert BEFORE index 2 (meaning before 3rd element)
beer_list.insert(5, "Cēsu sula")
print(beer_list)
while "Cēsu sula" in beer_list:
    print("found Cēsu sula")
    beer_list.remove("Cēsu sula")
print(beer_list)

# beer_list.remove("Cēsu sula") # again in place first match
# print(beer_list)
# beer_list.remove("alus")
# print(beer_list)
# beer_list.remove("alus")
# print(beer_list)
beer_list.reverse() # in place reversal
print(beer_list)
new_beer_list = beer_list[::-1]  # so i save the reversed list but keep the original
print(new_beer_list)

# # so if we have comparable data types inside (so same types)
new_beer_list.sort() # in place sort, modifies existing
print(new_beer_list)
sorted_by_len = sorted(new_beer_list, key=len) # out of place meaning returns new list
print(sorted_by_len)
sorted_by_len_rev = sorted(new_beer_list, key=len, reverse=True) # out of place meaning returns new list
print(sorted_by_len_rev)
print(max(beer_list), min(beer_list)) # by alphabet

numbers = [1, 4, -5, 3.16, 10, 9000, 5]
saved_sort_asc = sorted(numbers)  # out of place does not modify numbers
print(saved_sort_asc)
# # sorted(numbers, reverse=True)  # out of place does not modify numbers
# # numbers
# # numbers.sort()  # in place meaning it modifies the numbers
# # numbers
# # numbers.remove(9000)  # will remove in place first 9000 found in the list
# # numbers
# # min(numbers), max(numbers)
# print(sum(numbers))
# # our own sum
# total = 0
# for n in numbers:
#     total += n
# print(total)

sentence = "Quick brown fox jumped   over a    sleeping dog"
words = sentence.split() # default split is by whitespace convert into a list of words
print(words)
words[2] = "bear"
print(words)
# # so str(words) will not work exactly so we need something else
new_sentence = " ".join(words) # we will lose any double or triple whitespace
print(new_sentence)
funky_sentence = "*:*".join(words) # we will lose any double or triple whitespace
print(funky_sentence)

# # we can create a list of letters
# food = "kartupelis"
# letters = list(food)  # list with all letters
# print(letters)
# letters[5] = "m"
# new_word = "".join(letters) # we join by nothing so no spaces in the new word
# print(new_word)

# new_list = []
# for word in words:
#     new_list.append(word.capitalize())
# print(new_list)
# # # list comprehension same as above
# new_list_2 = [w.capitalize() for w in words]
# print(new_list_2)
# filtered_list = [w for w in words if w.startswith("b")]
# print(filtered_list)
# filtered_list = [w.upper() for w in words if w.startswith("b")]
# print(filtered_list)
# # filtered_list_2 = [w for w in words if w[0] == "b"]
# # filtered_list_2
# # filtered_list_3 = [w.upper() for w in words if w[0] == "b"]
# # filtered_list_3

# numbers = list(range(10)) # we cast to list our range object
# print(numbers)
# squares = []
# for n in numbers:  # could also use range(10)
#     squares.append(n*n)
# print(squares)
# squares_2 = [n*n for n in range(10)] # list comprehension of the above
# print(squares_2)
# even_squares = [n*n for n in range(10) if n % 2 == 0]
# print(even_squares)

# print("Whew we need a beer now don't we ?")

# # food
# # char_codes = [ord(c) for c in food]
# # char_codes
# # char_codes_list = [[f"Char:{c}", ord(c)] for c in food]
# # char_codes_list
# # print(char_codes_list[0])
# # print(char_codes_list[0][0])
# # print(char_codes_list[-1])
# # print(char_codes_list[-1][-1])
