# looping and cleaning strings
text = "Valda abracadabra maģija mana"
bad_symbols = "abc"
# I can loop through stings
for symbol in bad_symbols:
    print("Bad symbol", symbol)
new_text = text # i want to keep the original text
# using this approach I can clean all bad symbols from original
# so called TOP-DOWN approach
for char in bad_symbols:
    print(f"replacing all instances of {char} with nothing")
    print(f"Currently: {text}")
    new_text = new_text.replace(char, "")
print("After cleaning", new_text)

# we can check for presence of some character
# how many a are present in text

# we can check if a is present
needle = "a"
print(needle, "is present?", needle in text)
print(needle, "is present?", needle in new_text)

# i could also count how many
print(f"how many {needle} in {text}?", text.count(needle))
print(f"how many {needle} in {new_text}?", new_text.count(needle))

# by using buffer we can build strings from original strings
buffer = "" # start with nothing # so BOTTOM-UP approach
for char in text:
    print(f"Checking {char}")
    if char in bad_symbols: # so current char is undesirable
        buffer += "X" # means buffer = buffer + "X"
        # X could be any string
        # this is not efficient for huge strings
    else: # means we have normal characters
        buffer += char # we keep the original
    print("Current", buffer)
print("Buffer", buffer)


# sometimes it is useful to loop through two sequences at once
food = "Kebabs"
drink = "Alus"
# we will have a pair of variables in each iteration of loop
for f,d in zip(food,drink): # we will loop until one of zipped runs out
    print(f"f is {f} from {food}")
    print(f"d is {d} from {drink}")
    
# sometimes we need an index of what we are looping
# then we use enumerate
for i,c in enumerate(drink):
    print(f"index {i} is {c} for {drink}")