def is_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
    a_set = set(a)
    # normalize text
    mytext_set = set(mytext.replace(" ", "").lower())
    return a_set <= mytext_set
    # return a_set.issubset(mytext_set) # same as previous line
 
print(is_pangram("abcd foo")) # False
print(is_pangram("The quick brown fox jumps over the lazy dog")) # True
print(is_pangram("The five boxing wizards jump quickly")) 

latvian_alphabet = "aābcčdeēfgģhiījkķlļmnņoprsštuūvzž"
assert len(latvian_alphabet) == 33
print(is_pangram("Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!")) # True
# so perfect pangram is one where each letter is used exactly once
print(is_pangram("Čehu zeņķi ģērbj plīša frakā, mūc džungļos, tēv!")) # True
# TODO find Latvian pangram