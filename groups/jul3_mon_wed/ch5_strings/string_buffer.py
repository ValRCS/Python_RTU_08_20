# we might need to build a new string by going through each character in string

text = "Valdis likes to eat kartupelis"
buffer = ""
# instead of replace I could offer to build a string from ground up
for character in text:
    if character == "a":
        buffer += "ā"
    else:
        buffer += character
print(buffer)
# we could have used replace for this simple example
# with buffer we can do more complex logic at the cost of more code