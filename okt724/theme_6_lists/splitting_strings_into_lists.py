# let's see how we can split a string into a list
sentence = "A quick brown fox jumps over    the   \nlazy dog"
print(sentence)
# we have a nifty method called split for strings in Python
words = sentence.split() # by default it splits by space
print(words) # we get a list of words without any spaces
# let's change fox to cat
words[3] = 'cat' # we can change the value of a list
# we could have used index method to find the index of fox
# index = words.index('fox')
# print new list
print(words)

# now the slightly tricky part how do we get the string
# you might think this would work
new_str = str(words)
print(new_str) # not quite what we want, prints string of the list
# not very useful

# instead we use join method for strings
# it is a method of a string which needs a list of strings as an argument
new_str = ' '.join(words) # we use space as a separator
print(new_str) # we get the original string

# we do not have to use space as a separator
funny_string = '😀'.join(words) # we use a smiley or anything as a separator
print(funny_string) # we get a funny string