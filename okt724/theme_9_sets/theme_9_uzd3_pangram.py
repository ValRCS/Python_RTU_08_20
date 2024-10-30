# 3. Vai ir pangramma?
# uzrakstīt funkciju is_pangram, kas atgriež True, kad mytext parametrs satur visus burtus kas padoti a alfabetā.
# def diff(a,b):
#     c = a.symmetric_difference(b)
#     return not(bool(c))
 
# def is_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
#     # remove spaces
#     mytext = str(mytext.replace(" ",""))
#     # ignore uppercase, convert to set
#     mytext_set = set(mytext.lower())
#     # convert alphabet to set
#     set_a = set(a)
#     return diff(mytext_set,set_a)

# even simpler is to use subset method
def is_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
    # ignore uppercase, convert to set
    mytext_set = set(mytext.lower()) # so called normalizing
    # convert alphabet to set
    alpha_set = set(a)
    # return alpha_set.issubset(mytext_set) # we could use shorter version alpha_set <= mytext_set
    return alpha_set <= mytext_set # we do not care if there are other leters, spaces, numbers etc.
 
print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("abcd foo"))
print(is_pangram("The five boxing wizards jump quickly"))

# we could add Latvian alphabet
latvian_alphabet = "aābcčdeēfgģhiījkķlļmnņoprsštuūvzž"
# assert it has 33 letters
assert len(latvian_alphabet) == 33, "Latvian alphabet should have 33 letters" # assert will raise exception if not true
# if there is no exception it is True, and we can proceed
print(is_pangram("Ābelīte ātri ēda zāli", latvian_alphabet))

latvian_text = 'Tfū, čeh, džungļos 123456789 0 blīkšķ, zvaņģim jācērp!'
print(is_pangram(latvian_text, latvian_alphabet))

# let's find out which letter is missing from the pangram
def missing_letters(mytext, a='abcdefghijklmnopqrstuvwxyz'):
    # ignore uppercase, convert to set
    mytext_set = set(mytext.lower())
    # convert alphabet to set
    alpha_set = set(a)
    return alpha_set - mytext_set # we do not care if there are other leters, spaces, numbers etc.

print(missing_letters(latvian_text, latvian_alphabet)) 
print(missing_letters(latvian_alphabet, latvian_text)) # empty set as latvian alphabet is pangram   
