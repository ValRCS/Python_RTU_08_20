# a1 = 3
# a2 = 5
# a3 = 8
# a1064 = 332 # not a very good way to store a lot of data
# # # # # # # # # # # # # There has to be a better way

# # # # # # # # # # # # # # # What is a list after all?
# # # # # # # # # # # # # # # * ordered
# # # # # # # # # # # # # # # * collection of arbitrary objects (anything goes in)
# # # # # # # # # # # # # # # * nested (onion principle, Matroyshka) 2D,3D etc list possible
# # # # # # # # # # # # # # # * mutable - maināmas vērtības, we can change values in the list
# # # # # # # # # # # # # # # * dynamic - size can change
# # # # # # # # # # # # # trade_off - not the most efficient size wise - memory usage about 8x normal C array
# # # # if need to save memory we will need to use libraries such as numpy for storing similar data
# # # # # best use for lists is homogenous objects - same type for all in collection
# # # # # # #  
# # # we use square brackets to designate a list
my_list = [5, 6, "Valdis", True, 3.65, "alus"] # most common way of creating a list using [el1, el2]
print(my_list) # [5, 6, 'Valdis', True, 3.65, 'alus']
print(type(my_list)) # <class 'list'>

# Access
#
# # # # lists have dual indexing - first index is 0, last index is -1
print(my_list[0]) # so list index starts at 0 for the first element
print(my_list[-1], my_list[5])  # last element has index -1, 6th element has index 5

# list length
print(len(my_list)) # 6

# # # # lists are mutable - can change contents at any time
my_list[1] = "Mr. 50"  # lists are mutable (unlike strings) types inside also will change on the run
print(my_list) # so we have a new value and even a new data type (string) inside our 2nd element

try:
    my_list[9] = "no such index" # we will need to use a different method to add elements
except IndexError as e:
    print("IndexError", e)
    print("You can not add elements to list like this outside of the list length")


# # # # looping through lists
# # # # # # variable el is created the first time we go through our loop
for el in my_list: # el is arbitrary name, can be anything, i, n, it, item, etc
    print(el, "is type", type(el))
    # i could do more stuff with the element here
print("el after going through my_list", el)  # last assignment is still available after loop ends

# # # # idiomatic Python to loop through lists with index, default start is 0
for i,el in enumerate(my_list): # if we need index, this is Pythonic way
    print(f"Item no. {i} is {el} == {my_list[i]}")  #the last part is not needed if we use enumerate

# # # # length of my_list
# print(len(my_list))

# # anti-pattern - avoid
# for i in range(len(my_list)): # this way is not encouraged
#     print(f"Item no. {i} is {my_list[i]}")

# # # # default start is 0 but we can customize it
for i,el in enumerate(my_list, start=101): # if we need index, this is Pythonic way, here we start
    print(f"Item no. {i} is {el}")

# # # # # # # slicing works just like in strings
print(my_list[:3]) # so we only print the first 3 elements from the list
print(my_list[-2:]) # last two
print(my_list[1:4], my_list[1:-1])
print(my_list[::2]) # jumping over every 2nd one

# # # # creating a list of numbers using list and range
# # # notice list constructor is used here, avoid using list as variable name!!
my_numbers = list(range(0, 120, 10)) # no 0 lidz 110 by step 10, also shows how to create a list from another sequence like object
print(my_numbers)
print(my_numbers[1:4]) # slicing, remember 40 is not included!
print(my_numbers[::2]) # even starting with 0, 20, 40, 60, 80, 100   
print(my_numbers[::3]) # nums starting with 00, 30, 60, 90
print(my_numbers[1::2]) # all odd indexed numbers, index 10, 30, 50, 70, 90, 110
# # # # # # # # # # print(my_list[1::2]) # start with 2nd element and then take every 2nd element
print(my_numbers[::-1]) # reverse
print(list(reversed(my_numbers))) # same as above line but a bit slower
print(reversed(my_numbers)) # this we would use when we do not need the list completely

for n in reversed(my_numbers): # less memory usage than my_numbers[::-1], which creates a new list
    print("num", n)

# # # # if we have similar items in list, for example numbers(int,float), or just strings
print(sum(my_numbers), len(my_numbers), min(my_numbers), max(my_numbers))
# # print(sum(my_list)) # will not work because my_list has different types inside

# if i had forgotten about sum I could do the following 
total = 0
for n in my_numbers:
    total += n
print(total)

# if i did not know about min
my_min = my_numbers[0]
for n in my_numbers:
    if n < my_min:
        my_min = n
print(my_min) # again no need if we know abou min function

# # # from distutils.command.clean import clean
# # # from distutils.util import split_quoted
# # # from os import stat
# # # from re import L
import statistics # for fancier statistics

# simple average
print(sum(my_numbers) / len(my_numbers))

# # # from numpy import square # built in library
# # # # if we need fancier statistics, we can use numpy - external library
print(statistics.mean(my_numbers), sum(my_numbers)/len(my_numbers))

my_numbers[6] = 100 # we change 7th element
print(my_numbers)
print(statistics.mean(my_numbers), statistics.median(my_numbers), statistics.mode(my_numbers))

# # # # how to add elements to a list?
# # # since list is dynamic, we can add elements to it
print(my_numbers)
my_numbers.append(50)  # so called IN PLACE operation changes the list 
# notice we did not use assignment =
print(my_numbers)
my_numbers.append(100)
my_numbers.append(-10)
print(my_numbers)

new_list = sorted(my_numbers) # OUT OF PLACE keeps the original, we can use sorted() to create a new list
print("NEW LIST:", new_list)
print("OLD LIST:", my_numbers)  # still not sorted!
my_numbers.sort()  # IN PLACE changes my_numbers order, so original order is lost
# # # notice IN PLACE methods usually return None - they do not return anything
print("OLD LIST:", my_numbers)
# comparing lists
print("Lists have same elements - same content?", my_numbers == new_list)
print("Lists are actually the same (point to same memory)?", my_numbers is new_list)  # this is false, because they are different objects
# print memory location
print(id(my_numbers), id(new_list))
print("TOP 5 ascending", my_numbers[-5:])
print("TOP 5 descending", my_numbers[-5:][::-1])
print("BOTTOM 5", my_numbers[:5])
my_numbers.sort(reverse=True) # of course I could do my_numbers.sort()[::-1]
print(my_numbers)

# # if i had values in list that are not comparable (let's say string and number ) then sort would not work

# # # saving values in a list while looping
my_list = []  # notice we overwrite old my_list with empty list
# print(my_list) # i could have used another list of course, but think ecologically :)
# # # # while True:
# while True:
#     user_input = input("Enter q(Q) to quit or a number otherwise ")
#     if user_input.lower().startswith('q'): 
#         print("Quitting")
#         break
#     # now we try to convert input to float
#     try:
#         num = float(user_input)  # 
#     except ValueError: # we catch a specific error
#         print(f"Sorry {user_input} is not a number! Please try again")
#         continue # back to front of while , ignoring rest of loop below
#     my_list.append(num)  # here we are assured that we have a number
#     print(my_list)

# print("After quitting my_list is:", my_list)

# # # # making an empty list
empty_list = [] 
also_empty_list = list() # less used but same as above
print(empty_list, also_empty_list)
# # # # of course we can add more elements to the list later (with append and other methods)

# # # i can convert other sequences to lists
food = "kartupelis"
print(food)
food_chars = list(food) # so type casing just like str, int, float, bool etc
print(food_chars) # technically those are not chars but tiny strings
food_chars[5] = "m" # we can mutate the list elements
print(food_chars)
maybe_food = str(food_chars) # not quite what we need, but it is a string
print(maybe_food) # just a string of what printing a list would look like
# # # # # we use join to join a list of chars into a string
food_again = "".join(food_chars) # "" shows what we are putting between each character
print(food_again)
print(" ".join(food_chars))
funny_food = "*_*".join(food_chars) # "" shows what we are putting between each character
print(funny_food)
emoji_food = "🍠".join(food_chars) # "" shows what we are putting between each character
print(emoji_food)

# # # # how to split a string into a list?
my_separator = "p"
print("kartupelis".split("p")) # i could split string by something
split_potato = "kartupelis".split(my_separator) # i could split string by something
print(split_potato)
# # # # back to original
print(my_separator.join(split_potato)) # join list of chars into a string

sentence = "A quick brown fox jumped      over a sleeping \t \n dog box and then ran away."
print(sentence)
words = sentence.split(" ") # split by space so we will have some empty strings
print(words) # list with words
words_only = sentence.split() # split by any number of whitespaces (tabs, newlines, spaces etc)
print(words_only) # list with words
letters = list(sentence)
print(letters) # list of chars

# # # # # membership testing
print("fox" in words)  # linear check O(n) - checking depends on number of items
print("ox" in words) # False because ox is not in words but fox is!
# while we pause let's think how we could check for partial match in a list
needle = "ox"
matches = [] # empty list to store matches
# now we loop through words and check if needle is in word
for word in words:
    if needle in word:
        print(f"Found {needle} in {word}")
        matches.append(word)
print(matches)
# Note: there is alsos a shorter way of doing such filtering using list comprehensions

print(words.index("fox")) # raises IndexError if not found
try:
    print(words.index("ox")) # raises IndexError if not found
except ValueError:
    print("ox not found")

words[3] = words[3].upper()*2 # i can do something with smaller elements in a list
words[-1] = "bear."
print(words)
new_sentence = ", ".join(words)
print(new_sentence)
new_normal_sentence = " ".join(words)
print(new_normal_sentence)
print(" ".join(words_only))  # here we lose the extra whitespace

# what to do if we want to convert list of numbers to a string?

try:
    print(" ".join(my_numbers))  # will not work because we have numbers in the list
except TypeError:
    print("Cannot join list of numbers to a string")    

# solution make a new list of strings
my_string_numbers = []
for n in my_numbers:
    my_string_numbers.append(str(n)) # note the str() type casting
print(my_string_numbers)
# side note min and max will work differently on strings..
print(min(my_string_numbers))
print(max(my_string_numbers))

# at least we can join our numbers together
# lets use some funny emoji separator
# how about a sun  emoji ?
emoji_sep = "🌞"
my_joined_numbers = emoji_sep.join(my_string_numbers)
print(my_joined_numbers)

# we can use any and all to check truthy values in a list
# all will return True if all elements are truthy
# any will return True if any element is truthy

my_list = [1,2,3,4,5,6,7,8,9,10]
print(all(my_list)) # all will return True if all elements are truthy

# all falsy values are False
# in Python those are 
# False, None, 0, 0.0, 0j, Decimal(0), Fraction(0, 1), [], (), {}, set(), range(0)
# everything else is truthy

# lets append 0 to our list
my_list.append(0)
print(my_list)
print(all(my_list)) # all will return False if one element is falsy
print(any(my_list)) # any will return True if at least one element is truthy

# lets use all to check if my_numbers are all positive
print(all([n > 0 for n in my_numbers])) # all will return False if one element is falsy
print(any([n > 0 for n in my_numbers])) # any will return True if at least one element is truthy
print([n > 0 for n in my_numbers]) # our first list comprehension

# list comprehension lets us make lists from some iterables (lists, strings, tuples, sets, dicts)
squares = [n**2 for n in my_numbers] # so loop through my_numbers and square each number
print(squares)

# we can also use list comprehension to filter out some values
# lets filter out values which are not over 50
over_50= [n for n in my_numbers if n > 50]
print(over_50)

# i can also combine
# lets filter out values which are not over 50 and square them
is_spring = True
over_50_squares = [n**2 for n in my_numbers if n > 50 and is_spring]
print(over_50_squares)

# we could do the same thing with regular loop
also_over_50_squares = []
for n in my_numbers:
    if n > 50:
        also_over_50_squares.append(n**2)
print(also_over_50_squares)

# use list comprehension for simple things
# use regular loops for more complex things


# # # # # # # type_list = [type(el) for el in my_list]
# # # # # # # print(type_list)
# # # # # # # type_is_str = [type(el) is str for el in my_list]
# # # # # # # print(type_is_str)
# # # # # # # print(any(type_is_str)) # Existence just one is enough
# # # # # # # print(all(type_is_str)) # ALl need to be true
# # # # # # # print(any([0,1,1,0,1]))
# # # # # # # print(all([0,1,1,0,1]))
# # # # # # # print(any([True,True,False]))
# # # # # # # print(all([True,True,False]))
# # # # # # # print(all([True,True,True]))

# # # # # # # # so one liner to see if all elements are strings
# # # # # # # print(all([type(el) is str for el in my_list]))

my_list = [5, 6, "Valdis", True, 3.65, "alus"] # list of different types
print(my_list)
print("alus" in my_list)  # True
print("al" in my_list)  # False because in needs a exact match


needle = "al" # what we want to find in our list
for item in my_list:
    print("Checking ", item)
    if type(item) is str and needle in item: # not all types have in operator
        print(f"Found {needle=} in {item=}") # python 3.8 and up, good for debugging
        print(f"Found needle={needle} in item={item}") # for python 3.6, 3.7 and up

clean_list = []
for item in my_list:
    if type(item) is str and needle in item:
        clean_list.append(item)
print(clean_list)

# # we can use list comprehension to filter out the items
also_clean_list = [item for item in my_list if type(item) is str and needle in item]
print(also_clean_list)

my_list = clean_list # this is not copy I just add alias for clean_list
# original my_list will be garbage collected by Python automatically
print(my_list)

# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # my_list.append()
my_list.append("Bauskas alus") # adds "Bauskas alus" at the end of my_list
my_list.append("Valmiermuižas alus")  # IN PLACE methods, means we modify the list
print(my_list)

my_list = my_list + ["Tērvetes alus"] # OUT OF PLACE we create a new list (in this case overwriting the old one)
print(my_list)
my_list += ["Mārītes alus"] # OUT OF PLACE we create a new list (in this case adding to the old one)	
# # # # # # my_list = my_list.__add__(["Mālpils alus"]) # this is same as + above, also OUT OF PLACE
print(my_list)

# # # # # # # # # # # # # # example how to filter something
# # find_list = [] # so we have an empty list in beginning
# # needle = "al" 
# # for item in my_list: # i can reuse item in the loop
# #     # if needle in item: will not work because we have non strings in list
# #     if type(item) is str and needle in item:
# #         print(f"Found {needle=} in {item=}")
# #         find_list.append(item)
# # print(f"{needle=} found in {find_list=}")

# # # # # # # # # # # # # # # ps the above could be done simpler with list comprehension
# # also_find_list = [item for item in my_list if type(item) is str and needle in item]
# # print(also_find_list)

# square_list= []
# for n in range(10):
#     square_list.append(n**2)
# print(square_list)

# # shorter with list comprehension
# square_list_also = [n**2 for n in range(10)]  # if is optional
# print(square_list_also)


# # # # # # # # # # # # # # # # # out of place meaning find_list stays the same
new_list = my_list + ["Kalējs", "Audējs"] # out of place addition, my_list is not modified
print(len(new_list), len(my_list))
print(my_list)
print(new_list)

# # # # find_list += ["Malējs", "Salīgais"] # shorthand for new_list = new_list + [new items ] so flattened
# # # # print(find_list)

my_list.append(["Svarīgais", "Mazais","Jaukais"]) #notice append added a list a s nested
print(my_list)
# # # # # # # # we have nesting now, one list inside another
print(my_list[-1])  # accessing inner list
print(my_list[-1][-1], my_list[-1][1]) # in this case for size 2 1 and -1 give same results

# # # we can use list extend to add more lists in a flat list
my_list.extend(["Fantastiskais", "Lapsa", "Kūmiņš"]) # very similar to += IN PLACE, so call flat
print(my_list)

# # # # # # print(find_list[-3])
# # # # # # print(find_list[-3][0], find_list[12][0], new_list[14][0])

# # # # # # # # # print(f"{str(my_list)}") # not quite what we want

# # # # # # # # # # # # how to convert all values to str
# print(my_list)
# str_list = []
# for item in my_list:
#     str_list.append(str(item)) # so if item is already string nothing will happen
# print(str_list)

# # # # # # # # # # # # # # # # list comprehensions make it even short
# str_list_2 = [str(item) for item in my_list]
# print(str_list_2)

# print("Values inside lists are equal", str_list == str_list_2) # check if 1st level values are equal
# print("variables point to same list?", str_list is str_list_2) # check if values are same object (reside in the same memory space), here False
# str_list_alias = str_list  # just a shortcut/pointer/alias NOT A COPY!
# print("variables point to same list?", str_list is str_list_alias) # check if values are same object (reside in the same memory space), here True
# print("Values inside lists are equal", str_list == str_list_alias) # check if 1st level values are equal

# str_list_alias[2] = "Changed something"
# print(str_list) # original will change too
# print(str_list_alias)
# print(str_list_2)  # unrelated list will not change

# # # # how to make a shallow copy of a list
# str_list_copy = str_list.copy() # this is a shallow copy, so it will not copy the nested lists
# # # # str_list_copy starts living its own life, so it will not be the same as str_list
# # print(find_list)
# # find_list = find_list[1:] # take off first value
# # print(find_list)

# lets make a copy of my list
my_list_copy = my_list.copy() # makes a shallow copy
# shallow means that it will not copy the nested lists - deeper copies are possible
find_list = my_list[1:] # take off first value, this might be slow on large list
print(find_list)

popped_value = find_list.pop()  # IN PLACE pops last value and RETURNS it
print(popped_value) # this is the value we popped
print(find_list) # this is the list without the popped value

find_list = find_list[:-3]  # find list without last 3 values
print(find_list)

# # # # more about list comprehensions
# # # print(my_numbers)
# # # squares = [n**2 for n in reversed(my_numbers)] # go through all my numbers and square them
# # # print(squares)
# # # squares_2d = [[n, n**2] for n in reversed(my_numbers)]
# # # print(squares_2d)
# # # print(squares_2d[-2]) # 
# # # print(squares_2d[-2][0]) # 100
# # # # # # # wierd_squares = [n*n or 9000 for n in my_numbers] # we could utilie or for 0, generally do not recommend this trick
# # # # # # # print(wierd_squares)

# # # zeros = [0 for _ in range(20)] # so list of 20 zeros
# # # print(zeros)
# # # also_zeros = [0]*20
# # # print(also_zeros)

# # my_numbers = list(range(14))
# # print("original", my_numbers)
# # odd_squares = [n*n for n in my_numbers if n%2 == 1] # so do something and also filter
# # print(odd_squares)

# # # odd_squares_2d = [[n, n*n, n**3, n**4] for n in my_numbers if n%2 == 1] # so do something and also filter
# # # print(odd_squares_2d)

# # # # # # # # same idea as above, but better for more complicated logic
# # odd_squares_also = []
# # even_cubes = []
# # for n in my_numbers:
# #     if n%2 == 1:
# #         odd_squares_also.append(n*n)
# #         # advantage of long approach is that here we can do more stuff,print etc
# #     else: # no reminder thus it is even
# #         even_cubes.append(n**3) 
# # print(odd_squares_also)
# # print(even_cubes)

# # # # # print(needle)
# # # # # # # # # # # # # need needle of course
# # # # # # # # # # so i can add if as filter to list comprehension
# # # # beer_list = [item for item in str_list if needle in item] 
# # # # print(beer_list)
# # # # beer_list = beer_list[1:] #get rid of Valdis (first element with index 0) in my beer list
# # # # print(beer_list)

beer_list = find_list # just a shortcut NOT a copy!
beer_list += ["Užavas alus"] # we create a list on demand - list literal beer_list = beer_list + ["Užavas alus"] 
# # # # # # similar to beer_list.append("Užavas alus")
print(beer_list)

# # # # # # # # # # squares = [num*num for num in range(10)] # so we come up with num on the spot
# # # # # # # # # # print(squares)
# # # # # # # squares_matrix = [[num, "squared", num*num] for num in range(10)]
# # # # # # # print(squares_matrix) # so list of lists (2d array basically)
# # # # # # # print(squares_matrix[9][2], squares_matrix[-1][-1])

# # # # # beer_list += ["Malējs"]  # same as new_list = new_list + ["Malējs"]
# # # # # # # # # # new_list

# # # # # print(beer_list[-1])
# # # # # print(beer_list)
# # # # # last_beer = beer_list[-1]
# # # # # beer_list = beer_list[:-1] #so i get rid of last element
# # # # # print(last_beer, beer_list)
# # # # # beer_list.append("Malējs")
# # # # # print(beer_list)
# # # # # last_beer = beer_list.pop()  # also in place meaning i destroyed the last value
# # # # # print(last_beer, beer_list)

# # # # # print(f"We took out {last_beer}")
# # # # # print(beer_list)
# # # # # beer_list.append(last_beer)
# # # # # print(beer_list)

# # beer_list = find_list.copy() # creates a shallow copy - shallow means only first level, not nested

beer_count = 0
for el in beer_list:
    if "alus" in el:
    # if "alus" == el: # so count will be for exact matches
        beer_count += 1
print(f"beer_count is {beer_count}")

# # # # # # # # # # # so above count can be done with count method
print(beer_list.count("alus")) # only exact matches
# # print(beer_list.index("alus")) # will be 0 since we start counting with 0
# # # print(beer_list.find("Mālenīetis")) # find does not exist for lists, unlike string
# # # # beer_list.extend(["Labietis", "Mālpils alus"]) # again in place similar to +=
# # # # # print(beer_list)
# # # # # beer_with_zh = [el for el in beer_list if "ža" in el]
# # # # # print(beer_with_zh)
# # # # # print(len(beer_with_zh))
# # # # # # # # # # beer_in_description = [el for el in beer_list if "alus" in el]
# # # # # # # # # # print(beer_in_description)
# # # # # # # # # # # has_alus_count = len([el for el in beer_list if "alus" in el])
# # # # # # # # # # # print(has_alus_count)

# # print("Testing some beers")
# # beer_list = ["Valdis", "Užavas alus", "Malējs", "Mālpils alus", "Labietis", "Žaža"]
# # print(beer_list)
# # beer_list = beer_list[1:] # so we get rid of first element

print(beer_list)
beer_list.insert(2, "Cēsu sula") # so it will insert BEFORE index 2 (meaning before 3rd element)
print(beer_list)
beer_list.insert(5, "Cēsu sula") # in general we want append instead of insert for speed
print(beer_list)
# i could use list comprehension to remove all Cēsu sula OUT OF PLACE - new list created!
clean_beers = [el for el in beer_list if not el == "Cēsu sula"]
print(clean_beers)
beer_list.remove("Cēsu sula") # removes first occurance IN PLACE
print(beer_list)

while "Cēsu sula" in beer_list: # careful with looping and changing element size
    print("found Cēsu sula")
    beer_list.remove("Cēsu sula")
print(beer_list)
# # clean_beers = [el for el in beer_list if not el == "Cēsu sula"]
# # print(clean_beers)

# # # # pop 
# # # last_element = clean_beers.pop()
# # # print("last element taken out", last_element)
# # # print(clean_beers)
# # # # # # # # alternative would be a while loop
# # # # # # while "Cēsu sula" in beer_list.copy(): # careful with looping and changing element size
# # # # # #     print("found Cēsu sula")
# # # # # #     beer_list.remove("Cēsu sula")
# # # # # # # print(beer_list)

# # # # # # # # beer_list.remove("Cēsu sula") # again in place first match error if not found
# # # # # # # print(beer_list)
# # # # # # # # # # # # # # # beer_list.remove("alus")
# # # # # # # # # # # # # # # print(beer_list)
# # # # # # # # # # # # # # # beer_list.remove("alus")
# # # # # # # # # # # # # # # print(beer_list)

beer_list.reverse() # in place reversal
print(beer_list)
new_beer_list = beer_list[::-1]  # OUT OF PLACE so i save the reversed list but keep the original
print(new_beer_list)

# # # # # # # # # # # # # # # # so if we have comparable data types inside (so same types)
beer_list.sort() # in place sort, modifies existing
print(beer_list)
# # # # # # num_list = [1,2,3,0, -5.5, 2.7, True, False, 0.5, 0] # we can compare int, float and bool
# # # # # # print(num_list)
# # # # # # newly_sorted = sorted(num_list) # OUT OF PLACE sort we get a new list
# # # # # # print(newly_sorted)
# # # # # # # print(num_list.sort()) # returns None! because IN PLACE
# # # # # # # print(num_list)

# # # # # # # # sorted_by_len = sorted(new_beer_list, key=len) # out of place meaning returns new list
# # # # # # # # print(sorted_by_len)
# # # # # # # # # # # sorted_by_len_rev = sorted(new_beer_list, key=len, reverse=True) # out of place meaning returns new list
# # # # # # # # # # # print(sorted_by_len_rev)
# # # # # # # # # # # print( min(beer_list), max(beer_list)) # by alphabet

# # # # # # # # if we have similar/homogenous data types we can do more operations
# # # # # # # numbers = [1, 4, -5, 3.16, 10, 9000, 5]
# # # # # # # print(min(numbers),max(numbers), sum(numbers), sum(numbers)/len(numbers))
# # # # # # # avg = round(sum(numbers)/len(numbers), 2)
# # # # # # # print(avg)

# # # # # # # # # # # saved_sort_asc = sorted(numbers)  # out of place does not modify numbers
# # # # # # # # # # # print(saved_sort_asc)
# # # # # # # # # # # # # # # # sorted(numbers, reverse=True)  # out of place does not modify numbers
# # # # # # # # # # # print(numbers)
# # # # # # # # # # # print(numbers.sort()) # in place meaning it modifies the numbers
# # # # # # # # # # # print(numbers)
# # # # # # # # # # # # # # # # numbers.remove(9000)  # will remove in place first 9000 found in the list
# # # # # # # # # # # # # # # # numbers
# # # # # # # # # # # # # # # # min(numbers), max(numbers)
# # # # # # # # # print(sum(my_numbers), min(my_numbers), max(my_numbers))
# # # # # # # # # # # # # # # our own sum
# # # # # # # # # total = 0
# # # # # # # # # for n in my_numbers:
# # # # # # # # #     total += n
# # # # # # # # #     # useful if we want to do more stuff with individual elements in list
# # # # # # # # # print(total)

# # # # # # # # # # sentence = "Quick brown fox jumped   over a    sleeping dog"
# # # # # # # # # # words = sentence.split() # default split is by whitespace convert into a list of words
# # # # # # # # # # print(words)
# # # # # # # # # # words[2] = "bear" # i can a modify a list
# # # # # # # # # # print(words)
# # # # # # # # # # # # # # # # so str(words) will not work exactly so we need something else
# # # # # # # # # # print(str(words)) # not what we want)
# # # # # # # # # # new_sentence = " ".join(words) # we will lose any double or triple whitespace
# # # # # # # # # # print(new_sentence)
# # # # # # # # # # compressed_sent = "".join(words) # all words together
# # # # # # # # # # print(compressed_sent)
# # # # # # # # # # funky_sentence = "*:*".join(words) # we will lose any double or triple whitespace
# # # # # # # # # # print(funky_sentence)

# # # # # # # # # # # # # # # # we can create a list of letters
# # # # # # # # # # food = "kartupelis"
# # # # # # # # # # letters = list(food)  # list with all letters
# # # # # # # # # # print(letters)
# # # # # # # # # # letters[5] = "m"
# # # # # # # # # # new_word = "".join(letters) # we join by nothing so no spaces in the new word
# # # # # # # # # # print(new_word)

# # # # # # # # print(words)
# # # # # # # # new_list = []
# # # # # # # # for word in words:
# # # # # # # #     new_list.append(word.capitalize())
# # # # # # # # print(new_list)
# # # # # # # # # # # # # # # # # list comprehension same as above
# # # # # # # # new_list_2 = [w.capitalize() for w in words]
# # # # # # # # print(new_list_2)
# # # # # # # # # # filtered_list = [w for w in words if w.startswith("b")]
# # # # # # # # # # print(filtered_list)
# # # # # # # # # # filtered_list = [w.upper() for w in words if w.startswith("b")]
# # # # # # # # # # print(filtered_list)
# # # # # # # # # # # # # # # # filtered_list_2 = [w for w in words if w[0] == "b"]
# # # # # # # # # # # # # # # # filtered_list_2
# # # # # # # # # # # # # # # # filtered_list_3 = [w.upper() for w in words if w[0] == "b"]
# # # # # # # # # # # # # # # filtered_list_3

# # # # # # # # # # print("Hello")

# # # # # # # # # # # # # # # numbers = list(range(10)) # we cast to list our range object
# # # # # # # # # # # # # # # print(numbers)
# # # # # # # # # # squares = []
# # # # # # # # # # for n in range(10):  # could also use range(10)
# # # # # # # # # #     squares.append(n*n)
# # # # # # # # # # print(squares)
# # # # # # # # # # squares_2 = [n*n for n in range(10)] # list comprehension of the above
# # # # # # # # # # print(squares_2)
# # # # # # # # # # even_squares = [n*n for n in range(10) if n % 2 == 0]
# # # # # # # # # # print(even_squares)

# # # # # # # # # # # # # # # print("Whew we need a beer now don't we ?")

# # # # # # # # # # # # # # # # food
# # # # # # # # # # # print(food)
# # # # # # # # # # # char_codes = [ord(c) for c in food]
# # # # # # # # # # # print(char_codes)
# # # # # # # # # # # char_codes_list = [[f"Char:{c}", ord(c)] for c in food]
# # # # # # # # # # # print(char_codes_list)
# # # # # # # # # # # # # # # # print(char_codes_list[0])
# # # # # # # # # # # # # # # # print(char_codes_list[0][0])
# # # # # # # # # # # # # # # # print(char_codes_list[-1])
# # # # # # # # # # # # # # # # print(char_codes_list[-1][-1])
# # # # # # # # # # # # # # so list of lists of characters 
# # # # # # # # # # # # # chars = [[c for c in list(word)] for word in sentence.split()]
# # # # # # # # # # # # # print(chars)

# # # # # print(my_numbers)
# # # # # number_alias = my_numbers  # shortcut to same data
# # # # # number_copy = my_numbers.copy() # creates shallow(1st level copy of list)
# # # # # another_copy = my_numbers[:] # this is also a copy, but less clear
# # # # # number_alias[5] = 5000
# # # # # print(number_alias)
# # # # # print(my_numbers)
# # # # # print(number_alias is my_numbers) # so both variables point to same list
# # # # # number_copy[-1] = 9000
# # # # # print(number_copy)
# # # # # print(another_copy)

# # # # # last thing if we loop through a list we DO NOT add or remove elemnts from the list!!

# # # # # TWO solutions
# # # # # use list comprehension to create a new list

# # # # # or loop through my_list.copy() and then we can modify the original list

# # print(beer_list)
# # beer_list.clear() # IN PLACE CLEAR the list, destroys all elements in the list!!
# # print(beer_list)


# lets create a two dimensional list of numbers and their squares
numbers = list(range(10))
squares = [n*n for n in numbers]
print(numbers)
print(squares)
# now we want to create a list of lists
# we can do this with list comprehension
# we can also do this with a loop

# list comprehension
# we create a list of lists

list_of_lists = [[n, n*n] for n in numbers]
print(list_of_lists)
# so to get values for 5 we do
print(list_of_lists[5])
# just the square of 5
print(list_of_lists[5][1]) # also works with negative indexes so -1 is the last element

# now let's do the same with a loop
# we create a list of lists
list_of_lists_2 = []
for n in numbers:
    list_of_lists_2.append([n, n*n]) # so we add a list of two elements to our list
print(list_of_lists_2)

# the results are identical but the lists are different in memory
print("Same objects in memory?", list_of_lists is list_of_lists_2) # False because memory address is different
print("Contents same?", list_of_lists == list_of_lists_2) # True because contents are the same

# let's create some big lists
# big_list = list(range(1_000_000))
# huge_list = list(range(100_000_000)) # this will take a while to create
# you would think 100M integers would take 800M bytes of memory but it doesn't
# but lists are not stored in contiguous memory and not efficient for large lists


sudoko_board_list = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print(*sudoko_board_list, sep="\n") # little trick * unpacks the list

# faster to make with list comprehension
sudoko_board_list_2 = [[0 for _ in range(9)] for _ in range(9)]
# even better if 9 was a variable
print(*sudoko_board_list_2, sep="\n")

print("*" * 80)
# lets put some numbers in the board
sudoko_board_list_2[0][0] = 1
sudoko_board_list_2[0][1] = 2
sudoko_board_list_2[0][2] = 3
# last row
sudoko_board_list_2[-1][-1] = 9
sudoko_board_list_2[-1][-2] = 8
sudoko_board_list_2[-1][-3] = 7
print(*sudoko_board_list_2, sep="\n")


# input("Press Enter to create alias for huge list...")

# huge_list_alias = huge_list # simple alias/reference to same list so no memory used

# input("Press Enter to create copy of huge list...")

# huge_list_copy = huge_list.copy() # creates a shallow copy of the list so memory used

# input("Press Enter to finish...")

# last think is when looping through a list we should NOT add or remove elements from the list
# you have two options
# use list comprehension to create a new list

# or loop through my_list.copy() and then we can modify the original list

for n in my_numbers.copy(): # important to use copy() here
    if n > 5:
        my_numbers.remove(n)
print(my_numbers)

