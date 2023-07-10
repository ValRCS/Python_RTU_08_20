# on string methods we have split method which lets us split string into list of strings

sentence = "Man ļoti patīk    jūrnieku dziesmas"
my_list = sentence.split() # by default we split by whitespace
print(my_list) # first time we get a list

# so what is a list?
# list is a collection of items
# with list we can store multiple items in one variable
# we can store different types of items in one list
# we can store lists inside lists
# we have index for each item in list
# we can change items in list - mutable
# we can add items to list - dynamic size

# one thing is we can use indexing

# we can use indexing to get individual items from list
print(my_list[0]) # each item is a string here
print(my_list[1])

# first three items
print(my_list[0:3])
# easier
print(my_list[:3])

# i can reverse list
print(my_list[::-1])
# i can even replace items in list
my_list[0] = "Viņiem"
print(my_list)

# i can add items to list
my_list.append("un")
my_list.append("jūras")
my_list.append("vēji.")
print(my_list)

# finally I can create a string from list!
new_sentence = " ".join(my_list) # my_list is a list of strings else it would not work
print(new_sentence)
# for join i could use any string even empty string
squished_sentence = "".join(my_list)
print(squished_sentence)
# how about smiley?
smiley_sentence = "😀".join(my_list)
print(smiley_sentence)

# so we decomposed a string into list of words
# did some changes to list
# and then we joined list back into a string