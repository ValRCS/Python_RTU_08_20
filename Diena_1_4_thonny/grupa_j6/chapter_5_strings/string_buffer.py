# we might need to build a new string by going through another string

text = "Valdis un Oskars gāja uz veikalu un nopirka kartupeļus"
new_text = ""
for letter in text:
    if letter == "a":
        new_text += "ā" # same as new_text = new_text + "ā"
    else:
        new_text += letter
print(new_text)
# of course for this example we could have used replace
also_new_text = text.replace("a", "ā")
print(also_new_text)

# with the loop we have more control and options

# also for huge string this is not efficient
