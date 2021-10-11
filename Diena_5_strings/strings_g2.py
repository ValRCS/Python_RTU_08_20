import string # this has some extra string constants not required usually
print("My string Fun")


food = "kartupelis"
print(type(food))
food = "auzu putra" # we can reaasigng our variables
food = "kartupelis"
# # # # # # # # # food
# # # # # # # # # # Python Slicing syntax
print(food)
print(food[0])  # why zero index, historic reasons

food_len = len(food) # how many letters in a string or other collection

print(food_len)
print(food[9])  # so index 9 means 10th element
print(food[len(food)-1])  # not pythonic, avoid! Not needed
print(food[-1])  # this is Pythonic way of getting last character of string

print(food[-2])
print(food[2])  # what will be printed ?
print(food[-10])
# print(food[-11])  # IndexError: string index out of range

# # print(food[555]) # IndexError: string index out of range


# # # # # # # # # # when slicing we do not include the last index so 5 would be 6th element which we do not include
print(food[0:5], food[:5])  # so index 5(6th element) is not included so we get 1st 5 elements
print(food[0:3], food[:3])  # so index 3(4th element) is not included so we get 1st 3 elements
print(food[:9015])  # when slicing end index can be out of range
print(food[-3000:9015])  # when slicing beginning and end index can be out of range
# print(food[-3000:])  # when slicing beginning and end index can be out of range
# print(food[:]) #not much point for strings but for other sequences it makes a copy
# print(food)
# print(food[-2:])  # so last two characters
# print(food[-2:-1])  # so small slice similar to food[-2] but no error
print(food)
print(food[5:10], food[5:], food[-5:])
food = "Auzu putra ar avenēm un krejumu"
print(food[5:10], food[5:], food[-5:], sep="\n***\n")
print(food[5:10], food[5:], food[-5:])
# # # # # # # # print(food[400]) # so too much positive will give IndexError
# # # # # # # # print(food[-320])  # so too much negative will give IndexError
# # # # # # print(food[-320:400]) # we can do this though
# # # # # # print(food[-10:400]) # we can do this though

start = 2
end = 16
step = 3
print(food[start:end])
# # # # # print(food[5:], food[1:])
print(food)
# # print(food[0:20:2]) # step can be any whole number
# # print(food[:20:2])

# # print(food[start:end:step])
alphabet = string.ascii_lowercase
print(alphabet)
print(alphabet[start:end])
print(alphabet[start:end:step])
# # # # print(food[::2]) # this would get 2nd character of any strings
print(alphabet[1::2]) # this would get 2nd character of any strings starting with 2nd char
# # # # # # # # # # print(len(food))

# # # # # # # # # # # reversing a string
print(food[::-1])  # so we go backwards
# # my_reverse_string = food[::-1]  # if I need to save it
# # print(my_reverse_string)

print(alphabet)
reverse_alphabet = alphabet[::-1]
print(reverse_alphabet)
print(alphabet[::-2])
# # # print(alphabet[15:5:-1])

# # # words = food.split(" ")
# # # print(words)

# # # # # # # # if i need ' inside string then I can use " outside
my_text = "Alice told the rabbit 'go down the hole' and then followed"
print(my_text)
another_text = 'The bottle said "Eat me!" and Alice couldnt not write single quotes'
print(another_text)
multi_line_string = f"""We can write whatever even go to a 
new line
    or use tab
    use single ' and also "
    and so o n
    un man patīk {food}

    4wt!@#$^&
"""
print(multi_line_string)
escaped_string = "text meaning \" and also \' \n \t and of course \\ so on "
print(escaped_string)
# # # # # # # # # # food[::-2]
print(f"Min ({min(food)}), max({max(food)}), len:{len(food)}") #min and max use unicode codes
print(ord(" "), ord("e"), ord("ē"))  # Return the Unicode code point for a one-character string

# # # # # # # # # # this will not work
# food[3] = "Z" # will not work 
# # # # # # # # # # # strings are immutable so we need to create new strings
new_food = food.replace('u', 'ū') #replaces in all places by default count= can specify how many
print(new_food)
new_food = food.replace('u', 'ū', count:=2) #replaces in all places by default count= can specify how many
print(new_food)
print("X"*len(new_food)) #i can multiple strings with numbers so 20 Xses
print("*"*len(new_food)) #i can multiple strings with numbers so 20 Xses

print(food[:3])
print(food[3]) # so we will not keep this one in the new string
print(food[4:])
ze_food = food[:3] + "ZOOOZ" + food[4:] # so build a new string  # zooz of course can be any string one char or longer
print(ze_food)
ze_food_2 = f"{food[:3]}OOO{food[4:]}"
print(ze_food_2)
ze_food_2 = f"{food[:5]}*Jaunais*{food[2:]}" # this will insert new text between old text not losing anything
print(ze_food_2)
food = "mazaiSSSS karTUPelis jaukais"
print(food)
cap_food = food.capitalize() # so first word in capital letters
print(cap_food)
print(food.capitalize())
print(food.title()) # Title Gives Uppercase To Each Word
print(food.upper()) # YELLING
print(food.lower())

print(food.swapcase())

print(food.count("S"))
print(food.count("SS")) # answer should be 2 because we have SSSS
print(food.count("SSS")) # answer should be 1 because we have SSS
print(food.count("ai")) 
# # # # # # # # # # print(food.capitalize())
print(food.upper().replace("A", "Y")) # i can chain operations on strings
# # print(food[-5:].upper())
# # # # # # print(food.count('a'))
print(food.index('z')) # z is 3rd element so index is 2
print(food.index('i')) # i is 5th element so index is 4
# # print(food[4])
# print(food.index("kart")) # so index throws ValueError if not found
print(food.find("kārtis")) # if we do not want ValueError we can use find which returns -1 if not found
print(food.lower().index("kart"))
print(food.find('z'))
# # # # # # print(food.find('kart'))
# # # # # # print(food.lower().find('kart'))
print(food[10:10+4])
# # # # # # # # # # print(food.index('ž')) # index raises an error 
# # # # # # # print(food.find('ž')) # retursn -1
# # # # # # # # # print(food.find('z'))
# # # # # # # # # # print(ze_food)
# # # # # # # # # # ze_food.count("Z")
# # # # # # # # # # ze_food.find("p")
# # # # # # # # # # ze_food.index("p")
# # # # # # # # # # ze_food.find("valdis")
# # # # # # # # # # ze_food.index("valdis")
# # # # # # # # # # ze_food.find("ZZ")

# # print(food)
print("kar" in food) # so in gives us simple Boolean whether substring exists in string
print("kart" in food) # so in gives us simple Boolean whether substring exists in string
print("kart" in food.lower()) # so in gives us simple Boolean whether substring exists in string
# # print("karT" in food) # so in gives us simple Boolean whether substring exists in string
# # is_found = "kar" in food
# # print(is_found)

for c in food:
    print(c, end=":") # so instead of default newline \n i used : as endpoint

for c in food[3:8]:
    print(c)

for c in alphabet[5:11]:
    print(c)

# # # # # # # # # print(food.index('a')) 
count = 0
char = "S"
clean_text = ""
for c in food:
    if c == char:
        count += 1
    else:
        clean_text += c # create new string by adding char to old string
print(f"There are {count} {char}s in {food}")
print(f"Cleaned {clean_text=}") # this syntax is starting from Python
print(food.replace("S",""))

# # # # # # # # # # food, clean_text

# # # fresh_text = "" 
# # # for c1, c2 in zip(food, clean_text):  # you can zip many sequences
# # #     if c1 == c2:
# # #         fresh_text += c1  # also c2 would work # not great for long texts
# # #     else:  # mismatch
# # #         fresh_text += "_"
# # # print(fresh_text)

# # # # # # # # isArtFound = "art" in food
# # # # # # # # print(isArtFound)

print("Valdis" < "Voldemars")  # because 'a' , 'o' in Unicode table
print("Valdis" < "Voldis")  # because 'a' , 'o' in Unicode table
print(len("Valdis") < len("Voldemars"))  # by length

# # # # # # # # # # print("Alice said 'Run rabbit run!' and drunk something")
# # # # # # # # # # print("When we need both quotes \" \\ and also ' \n\n new lines ")
# # # # # # # # # # print(""" I can write whatever here
# # # # # # # # # # even new lines
# # # # # # # # # #             with tabs
# # # # # # # # # #              ' " " " '
# # # # # # # # # # """)
# # # # # # # # # # print(food.upper())
# # print(food.isalpha())
# # big_food = food + " banana"
# # print(big_food)
# # print(big_food.find("an"))
# # print(big_food.rfind("an"))
city = "    Rīga     "
print(city.strip())
# # # # # # # print(big_food.find("a"))
# # # # # # # print(big_food.rfind("a"))
# # # # # # # # # # sentence = "A quick brown fox run over a sleeping dog"
# # # # # # # # # # words = sentence.split()
# # # # # # # # # # print(words)

# building new string by rewriting old one
new_string =  ""
for c in alphabet:
    if c < "f":
        new_string += c # not efficient for huge strings but good for smaller ones
    else:
        new_string += "*"
print(new_string)
