import string

def is_pangram(mytext, a_alfabet = string.ascii_lowercase):
    
    for letter in a_alfabet:
        if letter not in mytext.lower():
            return False
    return True # means we covered all letters
print(is_pangram("The five boxing wizards jump quickly"))

##############
# 3rd Task
##############

def is_pangram_2(text, alphabet = string.ascii_lowercase):
    alphabet = set(alphabet)
    lower = text.lower()
    mytext_set = set(lower.replace(" ", "")) # not required
    
    # return alphabet.issubset(mytext_set)
    return alphabet <= mytext_set # same as above line
    # i could have use <= instead of issubset

# let's test it
print(is_pangram_2("The five boxing wizards jump quickly"))
print(is_pangram_2("The five boxing wizards jump quick"))

# how about Latvian alphabet
# first we need Latvian alphabet
# https://en.wikipedia.org/wiki/Latvian_orthography
lv_a = "aābcčdeēfgģhiījkķlļmnņoprsštuūvzž"
assert len(lv_a) == 33
print(is_pangram_2("žaņa ģērbonis vēl joprojām čukst", lv_a))
print(is_pangram_2("'Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!'", lv_a))
print(is_pangram_2("Čehu zeņķi ģērbj plīša frakā, mūc džungļos, tēv!", lv_a))
# so last two are pangrams, but first one is not