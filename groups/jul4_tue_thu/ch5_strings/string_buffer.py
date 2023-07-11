# we might need to build a new string by using parts of the old string
# we can start with blank buffer string and add to it

text = "Valdis likes to eat apples."
buffer = ""

# instead of replace we can use for loop and if statement
for letter in text:
    if letter == " ":
        buffer += "_"
    elif letter == ".":
        buffer += "#"
    else:
        buffer += letter # keep original
print(buffer)
# we could have done same thing with 2 replaces
# with for loop we get more flexibility and control and more complex logic