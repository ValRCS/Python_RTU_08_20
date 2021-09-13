# my_text = input(str("Please input your text so we can check if it's pangram: "))

 
def is_pangram(my_text, alphabet="abcdefghijklmnopqrstuvwxyz"):
    # return not set(alphabet) - set(my_text.lower())
    return set(alphabet) <= set(my_text.lower())

print(is_pangram("abcd foo"))
# Output -> False
print(is_pangram("The quick brown fox jumps over the lazy dog"))
# Output -> True
print(is_pangram("The five boxing wizards jump quickly"))
# Output -> True