print("String Fun")
food = "kartupelis"
food
food[0]
len(food)
food[9]
food[len(food)-1]  # not pythonic
food[-1]
food[-2]
food[0:5], food[:5]
food[5:10], food[5:9]
food[5:], food[1:]
food[1:6:2]
# reversing a string
print(food[::-1])
food[::-2]
print(min(food), max(food), len(food))

# strings are immutable so we need to create new strings
new_food = food.replace('p', 'm')
print(new_food)
ze_food = food[:3] + "ZZZE" + food[4:]
print(ze_food)
ze_food.count("Z")
ze_food.find("p")
ze_food.index("p")
ze_food.find("valdis")
ze_food.index("valdis")
ze_food.find("ZZ")
# for c in food:
#     print(c)

count = 0
char = "Z"
clean_text = ""
for c in ze_food:
    if c == char:
        count += 1
    else:
        clean_text += c
print(f"There are {count} {char}s in {ze_food}")
print(f"Cleaned {clean_text=}")

food, clean_text

fresh_text = ""
for c1, c2 in zip(food, clean_text):  # you can zip many sequences
    if c1 == c2:
        fresh_text += c1  # also c2 would work
    else:  # mismatch
        fresh_text += "_"
print(fresh_text)

isArtFound = "art" in food
print(isArtFound)

print("Valdis" > "Voldemars")  # because 'a' , 'o'

print("Alice said 'Run rabbit run!' and drunk something")
print("When we need both quotes \" \\ and also ' \n\n new lines ")
print(""" I can write whatever here
even new lines
            with tabs
             ' " " " '
""")
print(food.upper())
print(food.isalpha())
big_food = food + " banana"
print(big_food)
print(big_food.find("an"))
print(big_food.rfind("an"))
city = "    Rīga     "
print(city.strip())
sentence = "A quick brown fox run over a sleeping dog"
words = sentence.split()
print(words)
city.
