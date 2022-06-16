# 3.uzd
def ispangram(txt, alphabet = "abcdefghijklmnopqrstuvwxyz"):
    
    for char in alphabet:
        if char not in txt.lower():
            return False
 
    return True
 
text  = 'the quick brown fox jumps over the lazy dog'
not_pangram = 'this is not a pangram'
print(ispangram(text))
print(ispangram(not_pangram))

## 3.uzdevums
def is_pangram_2(mytext, a='abcdefghijklmnopqrstuvwxyz'):
    #  char_set = { char.lower() for char in set(mytext.replace(" ",""))}
 
     return set(a) <= set(mytext.lower())  # here it should return True or False
 
print(is_pangram_2("The five boxing wizards jump quickly"))

a_lv = 'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'
print(len(set(a_lv)))

print(is_pangram_2('Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!', a=a_lv))
print(is_pangram_2('Čehu zeņķi ģērbj plīša frakā, mūc džungļos, tēv!', a=a_lv))
print(is_pangram_2('Neteikums ģērbj plīša frakā, mūc džungļos, tēv!', a=a_lv))