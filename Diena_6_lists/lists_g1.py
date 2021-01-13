# # # a1 = 3
# # # a2 = 5
# # # a3 = 8
# # # There has to be a better way

# # # # # What is a list after all?
# # # # # * ordered
# # # # # * collection of arbitrary objects (anything goes in)
# # # # # * nested (onion principle, Matroyshka)
# # # # # * mutable - maināmas vērtības
# # # # # * dynamic - size can change
# # # trade_off - not the most efficient 
my_list = [5, 6, "Valdis", True, 3.65, "alus"] # most common way of creating a list using [el1, el2]
print(my_list)
print(type(my_list))
print(my_list[0]) # so list index starts at 0 for the first element
my_list[1] = "Mr. 50"  # lists are mutable (unlike strings)
print(my_list[:3])
print(my_list[-2:]) # last two
print(my_list[1:4], my_list[1:-1])
print(my_list[::2]) # jumping over every 2nd one
print(my_list[1::2])
print(my_list[-1])
# print(reversed(my_list)) # returns an iterator
print(list(reversed(my_list))) # so we need to cast it to list
print(my_list[::-1]) # so same as above when used on a list
print(list("kartupelis")) # can create a list out of string
print("kartupelis".split("p")) # i could split string by something
# # # # how to check for existance in list
print(3.65 in my_list)
print(66 in my_list)
print("Valdis" in my_list)
print("al" in "Valdis", "al" in my_list[2])
print("al" in my_list)  # this is false
# # # # # # iterate over items
needle = "al" # what we want to find in our list
for item in my_list:
    print("Checking ", item)
    if type(item) == str and needle in item: # not all types have in operator
        print(f"Found {needle=} in {item=}") # python 3.8 and up
        print(f"Found needle={needle} in item={item}") # for python 3.7

# # # # # #
# # # # my_list.append()
my_list.append("Bauskas alus") # adds "Bauskas alus" at the end of my_list
my_list.append("Valmiermuižas alus")  # IN PLACE methods, means we modify the list
print(my_list)

# # # # example how to filter something
find_list = [] # so we have an empty list in beginning
needle = "al" 
for item in my_list:
    # if needle in item: will not work because we have non strings in list
    if type(item) == str and needle in item:
        print(f"Found {needle=} in {item=}")
        find_list.append(item)
print(f"{needle=} found in {find_list=}")
# # # # ps the above could be done simpler with list comprehension

# # # # # # out of place meaning find_list stays the same
new_list = my_list + ["Kalējs", "Audējs"] # out of place addition, my_list is not modified
print(len(new_list), len(my_list))
print(my_list)
print(new_list)

new_list += ["Malējs", "Salīgais"] # shorthand for new_list = new_list + [new items ]
new_list.append(["Svarīgais", "Mazais"]) #notice append added a list a s nested
print(new_list)
new_list.extend(["Fantastiskais", "Lapsa"]) # very similar to +=
print(new_list)

print(f"{str(my_list)}") # not quite what we want
# # # how to convert all values to str
str_list = []
for item in my_list:
    str_list.append(str(item)) # so if item is already string nothing will happen
print(str_list)

# # # # # list comprehensions make it even short
str_list_2 = [str(item) for item in my_list]
print(str_list_2)

print("Lists have equal values inside?",str_list == str_list_2) # check if lists containe equal values
print("Lists are physically same?", str_list is str_list_2) # check if our variables reference the same list
str_list_3 = str_list # so str_list_3 is a shortcut to same values as
print(str_list == str_list_3, str_list is str_list_3)

# print(needle)
# # # # need needle of course
# so i can add if as filter to list comprehension
beer_list = [item for item in str_list if needle in item] 
print(beer_list)
beer_list = beer_list[1:] #get rid of Valdis (first element with index 0) in my beer list
print(beer_list)

beer_list += ["Užavas alus"] # we create a list on demand - list literal beer_list = beer_list + ["Užavas alus"] 
# # similar to beer_list.append("Užavas alus")
print(beer_list)

squares = [num*num for num in range(10)]
print(squares)
squares_matrix = [[num, "squared", num*num] for num in range(10)]
print(squares_matrix) # so list of lists (2d array basically)
print(squares_matrix[9][2], squares_matrix[-1][-1])

beer_list += ["Malējs"]  # same as new_list = new_list + ["Malējs"]
# new_list

print(beer_list[-1])
print(beer_list)
# # # last_beer = beer_list[-1]
# # # beer_list = beer_list[:-1]
last_beer = beer_list.pop()  # also in place meaning i destroyed the last value
print(last_beer, beer_list)

print(f"We took out {last_beer}")
print(beer_list)
beer_list.append(last_beer)
print(beer_list)

beer_count = 0
for el in beer_list:
    # if "alus" in el:
    if "alus" == el: # so count will be for exact matches
        beer_count += 1
print(beer_count)

print(beer_list.count("alus")) # only exact matches
print(beer_list.index("alus"), beer_list.index("Užavas alus"))
beer_list.extend(["Labietis", "Mālpils alus"]) # again in place similar to +=
print(beer_list)
beer_with_zh = [el for el in beer_list if "ža" in el]
print(beer_with_zh)
print(len(beer_with_zh))
has_alus_count = len([el for el in beer_list if "alus" in el])
print(has_alus_count)

beer_list.insert(2, "Cēsu sula") # so it will insert BEFORE index 2 (meaning before 3rd element)
print(beer_list)
beer_list.insert(5, "Cēsu sula")
print(beer_list)
beer_list.remove("Cēsu sula") # removes first occurance
print(beer_list)
clean_beers = [el for el in beer_list if el != "Cēsu sula"]
print(clean_beers)
while "Cēsu sula" in beer_list: # careful with looping and changing element size
    print("found Cēsu sula")
    beer_list.remove("Cēsu sula")
print(beer_list)

# # # # beer_list.remove("Cēsu sula") # again in place first match
# # # # print(beer_list)
# # # # beer_list.remove("alus")
# # # # print(beer_list)
# # # # beer_list.remove("alus")
# # # # print(beer_list)

beer_list.reverse() # in place reversal
print(beer_list)
new_beer_list = beer_list[::-1]  # so i save the reversed list but keep the original
print(new_beer_list)

# # # # # so if we have comparable data types inside (so same types)
new_beer_list.sort() # in place sort, modifies existing
print(new_beer_list)
num_list = [1,2,3,0, -5.5, 2.7, True, False, 0.5, 0] # we can compare int, float and bool
print(num_list)
print(num_list.sort()) # returns None!
print(num_list)

sorted_by_len = sorted(new_beer_list, key=len) # out of place meaning returns new list
print(sorted_by_len)
sorted_by_len_rev = sorted(new_beer_list, key=len, reverse=True) # out of place meaning returns new list
print(sorted_by_len_rev)
print( min(beer_list), max(beer_list)) # by alphabet

numbers = [1, 4, -5, 3.16, 10, 9000, 5]
print(min(numbers),max(numbers), sum(numbers), sum(numbers)/len(numbers))
avg = round(sum(numbers)/len(numbers), 2)
print(avg)

saved_sort_asc = sorted(numbers)  # out of place does not modify numbers
print(saved_sort_asc)
# # # # # sorted(numbers, reverse=True)  # out of place does not modify numbers
print(numbers)
print(numbers.sort()) # in place meaning it modifies the numbers
print(numbers)
# # # # # numbers.remove(9000)  # will remove in place first 9000 found in the list
# # # # # numbers
# # # # # min(numbers), max(numbers)
# # # # print(sum(numbers))
# # # # # our own sum
# total = 0
# for n in numbers:
#     total += n
#     # useful if we want to do more stuff with individual elements in list
# print(total)

sentence = "Quick brown fox jumped   over a    sleeping dog"
words = sentence.split() # default split is by whitespace convert into a list of words
print(words)
words[2] = "bear" # i can a modify a list
print(words)
# # # # # so str(words) will not work exactly so we need something else
print(str(words)) # not what we want)
new_sentence = " ".join(words) # we will lose any double or triple whitespace
print(new_sentence)
compressed_sent = "".join(words) # all words together
print(compressed_sent)
funky_sentence = "*:*".join(words) # we will lose any double or triple whitespace
print(funky_sentence)

# # # # # we can create a list of letters
food = "kartupelis"
letters = list(food)  # list with all letters
print(letters)
letters[5] = "m"
new_word = "".join(letters) # we join by nothing so no spaces in the new word
print(new_word)

new_list = []
for word in words:
    new_list.append(word.capitalize())
print(new_list)
# # # # # # list comprehension same as above
new_list_2 = [w.capitalize() for w in words]
print(new_list_2)
filtered_list = [w for w in words if w.startswith("b")]
print(filtered_list)
filtered_list = [w.upper() for w in words if w.startswith("b")]
print(filtered_list)
# # # # # filtered_list_2 = [w for w in words if w[0] == "b"]
# # # # # filtered_list_2
# # # # # filtered_list_3 = [w.upper() for w in words if w[0] == "b"]
# # # # # filtered_list_3

# # # # numbers = list(range(10)) # we cast to list our range object
# # # # print(numbers)
# # # # squares = []
# # # # for n in numbers:  # could also use range(10)
# # # #     squares.append(n*n)
# # # # print(squares)
# # # # squares_2 = [n*n for n in range(10)] # list comprehension of the above
# # # # print(squares_2)
# # # # even_squares = [n*n for n in range(10) if n % 2 == 0]
# # # # print(even_squares)

# # # # print("Whew we need a beer now don't we ?")

# # # # # food
# # # # # char_codes = [ord(c) for c in food]
# # # # # char_codes
# # # # # char_codes_list = [[f"Char:{c}", ord(c)] for c in food]
# # # # # char_codes_list
# # # # # print(char_codes_list[0])
# # # # # print(char_codes_list[0][0])
# # # # # print(char_codes_list[-1])
# # # # # print(char_codes_list[-1][-1])
# # # so list of lists of characters 
# # chars = [[c for c in list(word)] for word in sentence.split()]
# # print(chars)
