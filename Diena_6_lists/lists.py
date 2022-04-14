# a1 = 3
# a2 = 5
# a3 = 8
# # # # # # # # # There has to be a better way

# # # # # # # # # # # What is a list after all?
# # # # # # # # # # # * ordered
# # # # # # # # # # # * collection of arbitrary objects (anything goes in)
# # # # # # # # # # # * nested (onion principle, Matroyshka)
# # # # # # # # # # # * mutable - maināmas vērtības
# # # # # # # # # # # * dynamic - size can change
# # # # # # # # # trade_off - not the most efficient size wise
# best use for lists is homogenous objects - same type for all in collection
# # #  
my_list = [5, 6, "Valdis", True, 3.65, "alus"] # most common way of creating a list using [el1, el2]
print(my_list)
print(type(my_list))

print(my_list[0]) # so list index starts at 0 for the first element
print(my_list[-1], my_list[5])
my_list[1] = "Mr. 50"  # lists are mutable (unlike strings) types inside also will change on the run
print(my_list)
# # print(my_list[-1])

# # # variable el is created the first time we go through our loop
for el in my_list:
    print(el, "is type", type(el))
print("el after going through my_list", el)  # last assignment is still available after loop ends

for i,el in enumerate(my_list): # if we need index, this is Pythonic way
    print(f"Item no. {i} is {el}")
print(len(my_list))

# for i in range(len(my_list)): # this way is not encouraged
#     print(f"Item no. {i} is {my_list[i]}")

# default start is 0 but we can customize it
for i,el in enumerate(my_list, start=101): # if we need index, this is Pythonic way, here we start
    print(f"Item no. {i} is {el}")

# # # slicing works just like in strings
print(my_list[:3]) # so we only print the first 3 elements from the list
print(my_list[-2:]) # last two
# # print(my_list[1:4], my_list[1:-1])
# # print(my_list[::2]) # jumping over every 2nd one

my_numbers = list(range(0,120, 10)) # no 0 lidz 11, also shows how to create a list from another sequence like object
print(my_numbers)
print(my_numbers[1:4]) # slicing
print(my_numbers[::2]) # even starting with 0, 2, 4
print(my_numbers[::3]) # nums starting with 00, 30
print(my_numbers[1::2]) # all odd indexed numbers, index 1, 3, 5, 7
# # # # # # print(my_list[1::2]) # start with 2nd element and then take every 2nd element
# # print(my_list[-1], my_list[len(my_list)-1]) # last element, we use the short syntax
print(my_numbers[::-1])
print(list(reversed(my_numbers))) # same as above line but a bit slower
print(reversed(my_numbers)) # this we would use when we do not need the list completely

for n in reversed(my_numbers): # less memory usage than my_numbers[::-1]
    print("num", n)

# if we have similar items in list
print(sum(my_numbers), len(my_numbers), min(my_numbers), max(my_numbers))
import statistics
print(statistics.mean(my_numbers), sum(my_numbers)/len(my_numbers))
my_numbers[6] = 6000 # we change 7th element
print(my_numbers)

# how to add elements to a list?

my_numbers.append(50)  # so called IN PLACE operation changes the list 
print(my_numbers)
my_numbers.append(-10)
print(my_numbers)

new_list = sorted(my_numbers) # OUT OF PLACE keeps the original
print("NEW LIST:", new_list)
print("OLD LIST:", my_numbers)  # still not sorted!
my_numbers.sort()  # IN PLACE changes my_numbers order
print("OLD LIST:", my_numbers)
print("TOP 5 ascending", my_numbers[-5:])
print("TOP 5 descending", my_numbers[-5:][::-1])
print("BOTTOM 5", my_numbers[:5])
my_numbers.sort(reverse=True) # of course I could do my_numbers.sort()[::-1]
print(my_numbers)

# my_list = []
# while True:
#     user_input = input("Enter q to quit or a number otherwise")
#     if user_input.lower()[0] == "q": # input will give us at least one char 
#         print("Quitting")
#         break
#     try:
#         num = float(user_input)  # 
#     except ValueError:
#         print("Sorry not a number! Please try again")
#         continue # back to front of while
#     my_list.append(num)
#     print(my_list)

# print("After quitting my_list is:", my_list)

# # # my_reversed_numbers = my_numbers[::-1]
# # # print(my_reversed_numbers)
# # # # # # print(reversed(my_list)) # returns an iterator - so not a list but sort of prepared to list collection
# # # # # # print(list(reversed(my_list))) # so we need to cast it to list
# # # # # # print(my_list[::-1]) # so same as above when used on a list

empty_list = [] 
also_empty_list = list() # less used but same as above
print(empty_list, also_empty_list)
food = "kartupelis"
print(food)
food_chars = list(food) # so type casing just like str, int, float, bool etc
print(food_chars)
food_chars[5] = "m"
print(food_chars)
maybe_food = str(food_chars) # not quite
print(maybe_food) # just a string of what printing a list would look like
# we use join to join a list of chars into a string
food_again = "".join(food_chars) # "" shows what we are putting between each character
print(food_again)
print(" ".join(food_chars))
funny_food = "*_*".join(food_chars) # "" shows what we are putting between each character
print(funny_food)
# # # # print(list("kartupelis")) # can create a list out of string
print("kartupelis".split("p")) # i could split string by something
sentence = "A quick brown fox jumped      over a sleeping dog"
print(sentence)
words = sentence.split(" ") # split by space
print(words) # list with words
words_only = sentence.split() # split by any number of whitespaces
print(words_only) # list with words

# membership testing
print("fox" in words)  # linear check O(n) - checking depends on number of items
print(words.index("fox"))
words[3] = words[3].upper()*2 # i can do something with smaller elements in a list
words[-1] = "bear."
print(words)
new_sentence = ", ".join(words)
print(new_sentence)
new_normal_sentence = " ".join(words)
print(new_normal_sentence)
# # # # # # # # # # # how to check for existance in list
# # print(my_list)
# print(3.65 in my_list)
# print(66 in my_list)
# print("Valdis" in my_list)
# print(my_list[2]) # Valdis
# print("al" in "Valdis", "al" in my_list[2])
# print("al" in my_list)  # this is false,because in needs a exact match
# # # # # # # # # # # # # iterate over items
# # print("*"*20)
# # for it in my_list:
# #     print(it)

# # # type_list = [type(el) for el in my_list]
# # # print(type_list)
# # # type_is_str = [type(el) is str for el in my_list]
# # # print(type_is_str)
# # # print(any(type_is_str)) # Existence just one is enough
# # # print(all(type_is_str)) # ALl need to be true
# # # print(any([0,1,1,0,1]))
# # # print(all([0,1,1,0,1]))
# # # print(any([True,True,False]))
# # # print(all([True,True,False]))
# # # print(all([True,True,True]))

# # # # so one liner to see if all elements are strings
# # # print(all([type(el) is str for el in my_list]))

print(my_list)
print("al" in my_list)  # False because in needs a exact match


needle = "al" # what we want to find in our list
for item in my_list:
    print("Checking ", item)
    if type(item) is str and needle in item: # not all types have in operator
        print(f"Found {needle=} in {item=}") # python 3.8 and up, good for debugging
        print(f"Found needle={needle} in item={item}") # for python 3.6, 3.7 and up

# # # # # # # # # # # # #
# # # # # # # # # my_list.append()
my_list.append("Bauskas alus") # adds "Bauskas alus" at the end of my_list
my_list.append("Valmiermuižas alus")  # IN PLACE methods, means we modify the list
print(my_list)

my_list = my_list + ["Tērvetes alus"] # OUT OF PLACE we create a new list (in this case overwriting the old one)
print(my_list)
# # my_list = my_list.__add__(["Mālpils alus"]) # this is same as + above, also OUT OF PLACE
# # print(my_list)

# # # # # # # # # # # example how to filter something
find_list = [] # so we have an empty list in beginning
needle = "al" 
for item in my_list: # i can reuse item in the loop
    # if needle in item: will not work because we have non strings in list
    if type(item) == str and needle in item:
        print(f"Found {needle=} in {item=}")
        find_list.append(item)
print(f"{needle=} found in {find_list=}")
# # # # # # # # # # # ps the above could be done simpler with list comprehension
also_find_list = [item for item in my_list if type(item) == str and needle in item]
print(also_find_list)

# # # # # # # # # # # # # out of place meaning find_list stays the same
# # new_list = my_list + ["Kalējs", "Audējs"] # out of place addition, my_list is not modified
# # print(len(new_list), len(my_list))
# # print(my_list)
# # print(new_list)

find_list += ["Malējs", "Salīgais"] # shorthand for new_list = new_list + [new items ] so flattened
print(find_list)
find_list.append(["Svarīgais", "Mazais"]) #notice append added a list a s nested
print(find_list)
# # # # we have nesting now, one list inside another
print(find_list[-1])
print(find_list[-1][-1], find_list[-1][1]) # in this case for size 2 1 and -1 give same results

find_list.extend(["Fantastiskais", "Lapsa"]) # very similar to += IN PLACE, so call flat
print(find_list)

# # print(find_list[-3])
# # print(find_list[-3][0], find_list[12][0], new_list[14][0])

# # # # # print(f"{str(my_list)}") # not quite what we want

# # # # # # # # how to convert all values to str
print(my_list)
str_list = []
for item in my_list:
    str_list.append(str(item)) # so if item is already string nothing will happen
print(str_list)

# # # # # # # # # # # # list comprehensions make it even short
str_list_2 = [str(item) for item in my_list]
print(str_list_2)

print("Values inside lists are equal", str_list == str_list_2) # check if 1st level values are equal
print("variables point to same list?", str_list is str_list_2) # check if values are same object (reside in the same memory space), here False
str_list_alias = str_list  # just a shortcut/pointer/alias
print("variables point to same list?", str_list is str_list_alias) # check if values are same object (reside in the same memory space), here True
print("Values inside lists are equal", str_list == str_list_alias) # check if 1st level values are equal

str_list_alias[2] = "Changed something"
print(str_list)
print(str_list_alias)
print(str_list_2)

str_list_copy = str_list.copy() # this is a shallow copy, so it will not copy the nested lists
# str_list_copy starts living its own life, so it will not be the same as str_list

print(my_numbers)
squares = [n**2 for n in reversed(my_numbers)] # go through all my numbers and square them
print(squares)
squares_2d = [[n, n**2] for n in reversed(my_numbers)]
print(squares_2d)
# # # wierd_squares = [n*n or 9000 for n in my_numbers] # we could utilie or for 0, generally do not recommend this trick
# # # print(wierd_squares)

zeros = [0 for _ in range(20)] # so list of 20 zeros
print(zeros)
also_zeros = [0]*20
print(also_zeros)

my_numbers = list(range(14))
odd_squares = [n*n for n in my_numbers if n%2 == 1] # so do something and also filter
print(odd_squares)

odd_squares_2d = [[n, n*n, n**3, n**4] for n in my_numbers if n%2 == 1] # so do something and also filter
print(odd_squares_2d)

# # # # same idea as above, but better for more complicated logic
odd_squares_also = []
even_cubes = []
for n in my_numbers:
    if n%2 == 1:
        odd_squares_also.append(n*n)
        # advantage of long approach is that here we can do more stuff,print etc
    else: # no reminder thus it is even
        even_cubes.append(n**3) 
print(odd_squares_also)
print(even_cubes)
# # # print(str_list) 
# # # print(str_list_2)

# # print("Lists have equal values inside?",str_list == str_list_2) # check if lists containe equal values
# # print("Lists are physically same?", str_list is str_list_2) # check if our variables reference the same list
# # str_list_3 = str_list # so str_list_3 is a shortcut to same values as, NOT A COPY!
# # print(str_list == str_list_3, str_list is str_list_3)
# # str_list_copy = str_list.copy() # create a new list with same values
# # print(str_list == str_list_copy, str_list is str_list_copy)

# # str_list[3] = "Voldemārs"
# # print(str_list)
# # print(str_list_3)
# # print(str_list_copy)
# # print(id(str_list))
# # print(id(str_list_3))
# # print(id(str_list_copy))

# print(needle)
# # # # # # # # # need needle of course
# # # # # # so i can add if as filter to list comprehension
beer_list = [item for item in str_list if needle in item] 
print(beer_list)
beer_list = beer_list[1:] #get rid of Valdis (first element with index 0) in my beer list
print(beer_list)

beer_list += ["Užavas alus"] # we create a list on demand - list literal beer_list = beer_list + ["Užavas alus"] 
# # # # # # similar to beer_list.append("Užavas alus")
# # print(beer_list)

# # # # # # squares = [num*num for num in range(10)] # so we come up with num on the spot
# # # # # # print(squares)
# # # squares_matrix = [[num, "squared", num*num] for num in range(10)]
# # # print(squares_matrix) # so list of lists (2d array basically)
# # # print(squares_matrix[9][2], squares_matrix[-1][-1])

# beer_list += ["Malējs"]  # same as new_list = new_list + ["Malējs"]
# # # # # # new_list

# print(beer_list[-1])
# print(beer_list)
# last_beer = beer_list[-1]
# beer_list = beer_list[:-1] #so i get rid of last element
# print(last_beer, beer_list)
# beer_list.append("Malējs")
# print(beer_list)
# last_beer = beer_list.pop()  # also in place meaning i destroyed the last value
# print(last_beer, beer_list)

# print(f"We took out {last_beer}")
# print(beer_list)
# beer_list.append(last_beer)
# print(beer_list)

# beer_count = 0
# for el in beer_list:
#     if "alus" in el:
#     # if "alus" == el: # so count will be for exact matches
#         beer_count += 1
# print(beer_count)

# # # # # # # so above count can be done with count method
# print(beer_list.count("alus")) # only exact matches
# # # print(beer_list.index("alus")) # will be 0 since we start counting with 0
# # # # # print(beer_list.find("Mālenīetis")) # find does not exist for lists, unlike string
beer_list.extend(["Labietis", "Mālpils alus"]) # again in place similar to +=
# print(beer_list)
# beer_with_zh = [el for el in beer_list if "ža" in el]
# print(beer_with_zh)
# print(len(beer_with_zh))
# # # # # # beer_in_description = [el for el in beer_list if "alus" in el]
# # # # # # print(beer_in_description)
# # # # # # # has_alus_count = len([el for el in beer_list if "alus" in el])
# # # # # # # print(has_alus_count)

print(beer_list)
beer_list.insert(2, "Cēsu sula") # so it will insert BEFORE index 2 (meaning before 3rd element)
print(beer_list)
beer_list.insert(5, "Cēsu sula") # in general we want append instead of insert for speed
print(beer_list)
beer_list.remove("Cēsu sula") # removes first occurance IN PLACE
print(beer_list)

clean_beers = [el for el in beer_list if el != "Cēsu sula"]
print(clean_beers)
# # # # alternative would be a while loop
# # while "Cēsu sula" in beer_list.copy(): # careful with looping and changing element size
# #     print("found Cēsu sula")
# #     beer_list.remove("Cēsu sula")
# # # print(beer_list)

# # # # beer_list.remove("Cēsu sula") # again in place first match error if not found
# # # print(beer_list)
# # # # # # # # # # # beer_list.remove("alus")
# # # # # # # # # # # print(beer_list)
# # # # # # # # # # # beer_list.remove("alus")
# # # # # # # # # # # print(beer_list)

# # # beer_list.reverse() # in place reversal
# # # print(beer_list)
# # # new_beer_list = beer_list[::-1]  # so i save the reversed list but keep the original
# # # print(new_beer_list)

# # # # # # # # # # # # so if we have comparable data types inside (so same types)
# # beer_list.sort() # in place sort, modifies existing
# # print(beer_list)
# # num_list = [1,2,3,0, -5.5, 2.7, True, False, 0.5, 0] # we can compare int, float and bool
# # print(num_list)
# # newly_sorted = sorted(num_list) # OUT OF PLACE sort we get a new list
# # print(newly_sorted)
# # # print(num_list.sort()) # returns None! because IN PLACE
# # # print(num_list)

# # # # sorted_by_len = sorted(new_beer_list, key=len) # out of place meaning returns new list
# # # # print(sorted_by_len)
# # # # # # # sorted_by_len_rev = sorted(new_beer_list, key=len, reverse=True) # out of place meaning returns new list
# # # # # # # print(sorted_by_len_rev)
# # # # # # # print( min(beer_list), max(beer_list)) # by alphabet

# # # # if we have similar/homogenous data types we can do more operations
# # # numbers = [1, 4, -5, 3.16, 10, 9000, 5]
# # # print(min(numbers),max(numbers), sum(numbers), sum(numbers)/len(numbers))
# # # avg = round(sum(numbers)/len(numbers), 2)
# # # print(avg)

# # # # # # # saved_sort_asc = sorted(numbers)  # out of place does not modify numbers
# # # # # # # print(saved_sort_asc)
# # # # # # # # # # # # sorted(numbers, reverse=True)  # out of place does not modify numbers
# # # # # # # print(numbers)
# # # # # # # print(numbers.sort()) # in place meaning it modifies the numbers
# # # # # # # print(numbers)
# # # # # # # # # # # # numbers.remove(9000)  # will remove in place first 9000 found in the list
# # # # # # # # # # # # numbers
# # # # # # # # # # # # min(numbers), max(numbers)
# # # # # print(sum(my_numbers), min(my_numbers), max(my_numbers))
# # # # # # # # # # # our own sum
# # # # # total = 0
# # # # # for n in my_numbers:
# # # # #     total += n
# # # # #     # useful if we want to do more stuff with individual elements in list
# # # # # print(total)

# # # # # # sentence = "Quick brown fox jumped   over a    sleeping dog"
# # # # # # words = sentence.split() # default split is by whitespace convert into a list of words
# # # # # # print(words)
# # # # # # words[2] = "bear" # i can a modify a list
# # # # # # print(words)
# # # # # # # # # # # # so str(words) will not work exactly so we need something else
# # # # # # print(str(words)) # not what we want)
# # # # # # new_sentence = " ".join(words) # we will lose any double or triple whitespace
# # # # # # print(new_sentence)
# # # # # # compressed_sent = "".join(words) # all words together
# # # # # # print(compressed_sent)
# # # # # # funky_sentence = "*:*".join(words) # we will lose any double or triple whitespace
# # # # # # print(funky_sentence)

# # # # # # # # # # # # we can create a list of letters
# # # # # # food = "kartupelis"
# # # # # # letters = list(food)  # list with all letters
# # # # # # print(letters)
# # # # # # letters[5] = "m"
# # # # # # new_word = "".join(letters) # we join by nothing so no spaces in the new word
# # # # # # print(new_word)

# # # # print(words)
# # # # new_list = []
# # # # for word in words:
# # # #     new_list.append(word.capitalize())
# # # # print(new_list)
# # # # # # # # # # # # # list comprehension same as above
# # # # new_list_2 = [w.capitalize() for w in words]
# # # # print(new_list_2)
# # # # # # filtered_list = [w for w in words if w.startswith("b")]
# # # # # # print(filtered_list)
# # # # # # filtered_list = [w.upper() for w in words if w.startswith("b")]
# # # # # # print(filtered_list)
# # # # # # # # # # # # filtered_list_2 = [w for w in words if w[0] == "b"]
# # # # # # # # # # # # filtered_list_2
# # # # # # # # # # # # filtered_list_3 = [w.upper() for w in words if w[0] == "b"]
# # # # # # # # # # # filtered_list_3

# # # # # # print("Hello")

# # # # # # # # # # # numbers = list(range(10)) # we cast to list our range object
# # # # # # # # # # # print(numbers)
# # # # # # squares = []
# # # # # # for n in range(10):  # could also use range(10)
# # # # # #     squares.append(n*n)
# # # # # # print(squares)
# # # # # # squares_2 = [n*n for n in range(10)] # list comprehension of the above
# # # # # # print(squares_2)
# # # # # # even_squares = [n*n for n in range(10) if n % 2 == 0]
# # # # # # print(even_squares)

# # # # # # # # # # # print("Whew we need a beer now don't we ?")

# # # # # # # # # # # # food
# # # # # # # print(food)
# # # # # # # char_codes = [ord(c) for c in food]
# # # # # # # print(char_codes)
# # # # # # # char_codes_list = [[f"Char:{c}", ord(c)] for c in food]
# # # # # # # print(char_codes_list)
# # # # # # # # # # # # print(char_codes_list[0])
# # # # # # # # # # # # print(char_codes_list[0][0])
# # # # # # # # # # # # print(char_codes_list[-1])
# # # # # # # # # # # # print(char_codes_list[-1][-1])
# # # # # # # # # # so list of lists of characters 
# # # # # # # # # chars = [[c for c in list(word)] for word in sentence.split()]
# # # # # # # # # print(chars)

# print(my_numbers)
# number_alias = my_numbers  # shortcut to same data
# number_copy = my_numbers.copy() # creates shallow(1st level copy of list)
# another_copy = my_numbers[:] # this is also a copy, but less clear
# number_alias[5] = 5000
# print(number_alias)
# print(my_numbers)
# print(number_alias is my_numbers) # so both variables point to same list
# number_copy[-1] = 9000
# print(number_copy)
# print(another_copy)

# last thing if we loop through a list we DO NOT add or remove elemnts from the list!!

# TWO solutions
# use list comprehension to create a new list

# or loop through my_list.copy() and then we can modify the original list


