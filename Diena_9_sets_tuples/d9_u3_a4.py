def is_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
    return set(mytext.lower()) >= set(a.lower())

print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("abcd foo"))
print(is_pangram("The five boxing wizards jump quickly"))

latvian_alphabet = "aābcčdeēfgģhiījkķlļmnņoprsštuūvzž"

my_text = "Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!"
print(is_pangram(my_text, latvian_alphabet))

from string import punctuation

def is_perfect_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
    # first we clean the text from cruft
    for char in punctuation:
        mytext = mytext.replace(char, "")
    mytext = mytext.replace(" ", "")
    mytext = mytext.lower()
    return set(mytext) == set(a) and len(set(mytext)) == len(mytext)

print(is_perfect_pangram("The quick brown fox jumps over the lazy dog"))

# so Latvian version is perfect pangram
print(is_perfect_pangram(my_text, latvian_alphabet))

# functions should work with any alphabet
print(is_perfect_pangram("abbc", a="abc"))
print(is_pangram("abbc", a="abc"))


