# we have a split method to convert a string into a list of strings
# by default split will split on whitespace
sentence = "Valdis likes to eat     apples"
words = sentence.split() # default split on whitespace
print(words)
print(type(words)) # list - we will talk about lists later - similar to array in other languages
# lists have same indexing as strings
print(words[0]) # Valdis
# last word
print(words[-1]) # apples
# unlike strings , lists are mutable, we can change them
words[0] = "Voldemārs" # Valdis is gone
print(words)
# then we might want to get back to full string - not list
# we can use join method
# we can use any string to join our list of strings
# so we could use single whitespace
new_string = " ".join(words)
print(new_string)
# only thing we lost are the extra whitespaces between eat and apples