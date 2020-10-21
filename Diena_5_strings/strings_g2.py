
print("String Fun")
food = "kartupelis"
print(type(food))
food = "auzu putra"
food = "kartupelis"
# # food
# # Python Slicing syntax
print(food)
print(food[0])  # why zero, historic reasons

food_len = len(food)
print(food_len)
print(food[9])
# print(food[len(food)-1])  # not pythonic, avoid! Not needed
print(food[-1], food[-10])
print(food[-2])
# # when slicing we do not include the last index so 5 would be 6th element which we do not include
print(food[0:5], food[:5])
print(food[:9015])  # when slicing end index can be out of range

print(food[5:10], food[5:], food[-5:])
food = "Auzu putra ar avenēm"
print(food[5:10], food[5:], food[-5:], sep="\n")
# print(food[400]) # so too much positive will give IndexError
# print(food[-320])  # so too much negative will give IndexError
print(food[-320:400]) # we can do this though

# # food[5:], food[1:]
print(food[0:20:2])
print(food[:20:2])
print(food[::2])
# print(len(food))

# # reversing a string
print(food[::-1])
my_reverse_string = food[::-1] # if I need to save it
print(my_reverse_string)

my_text = "Alice told the rabbit 'go down the hole' and then followed"
print(my_text)
another_text = 'The bottle said "Eat me!" and Alice couldn not write single quotes'
print(another_text)
multi_line_string = """We can write whatever even go to a 
new line
    or use tab
    use single ' and also "
    and so o n

"""
print(multi_line_string)
escaped_string = "text meaning \" and also \' \n \t and of course \\ so on "
print(escaped_string)
# # food[::-2]
print(min(food), max(food), len(food))

# this will not work
# food[3] = "Z" # will not work
# # strings are immutable so we need to create new strings
new_food = food.replace('u', 'ū')
print(new_food)
print(food[:3])
print(food[3]) # so we will not keep this one in the new string
print(food[4:])
ze_food = food[:3] + "ZZZE" + food[4:]
print(ze_food)
food = "mazaiSSS karTUPelis"
cap_food = food.capitalize() # so first word in capital letters
print(food.capitalize())
print(food.upper())
print(food.lower())
print(food.title())
print(food.count("S"))
# print(food.capitalize())
# print(food.capitalize().replace("A", "L"))
print(food[-5:].upper())
print(food.count('a'))
print(food.index('a')) 
print(food.find('a'))
# print(food.index('ž')) # index raises an error 
print(food.find('ž'))
print(food.find('z'))
# print(ze_food)
# ze_food.count("Z")
# ze_food.find("p")
# ze_food.index("p")
# ze_food.find("valdis")
# ze_food.index("valdis")
# ze_food.find("ZZ")
for c in food:
    print(c, end=":")

# for c in food[3:8]:
#     print(c)

# print(food.index('a')) 
count = 0
char = "S"
clean_text = ""
for c in food:
    if c == char:
        count += 1
    else:
        clean_text += c
print(f"There are {count} {char}s in {ze_food}")
print(f"Cleaned {clean_text=}")

# food, clean_text

# fresh_text = ""
# for c1, c2 in zip(food, clean_text):  # you can zip many sequences
#     if c1 == c2:
#         fresh_text += c1  # also c2 would work
#     else:  # mismatch
#         fresh_text += "_"
# print(fresh_text)

# isArtFound = "art" in food
# print(isArtFound)

# print("Valdis" > "Voldemars")  # because 'a' , 'o'

# print("Alice said 'Run rabbit run!' and drunk something")
# print("When we need both quotes \" \\ and also ' \n\n new lines ")
# print(""" I can write whatever here
# even new lines
#             with tabs
#              ' " " " '
# """)
# print(food.upper())
# print(food.isalpha())
# big_food = food + " banana"
# print(big_food)
# print(big_food.find("an"))
# print(big_food.rfind("an"))
# city = "    Rīga     "
# print(city.strip())
# sentence = "A quick brown fox run over a sleeping dog"
# words = sentence.split()
# print(words)
