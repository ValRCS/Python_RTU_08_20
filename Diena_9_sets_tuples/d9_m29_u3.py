#________3uzd__________
 
# def is_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
#     alphabet = set(a)
#     text = set(mytext.lower())
#     text.discard(' ')
#     return text == alphabet

# Vai ir pangramma?
def is_pangram(mytext, a="abcdefghijklmnopqrstuvwxyz"):
    return set(a) <= set(mytext.lower())
 
 
txt = "The quick brown fox jumps over the lazy dog"
 
print(is_pangram(txt))
print(is_pangram("something else"))

a_lv = 'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'
print(len(set(a_lv)))

print(is_pangram('Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!', a=a_lv))
print(is_pangram('Čehu zeņķi ģērbj plīša frakā, mūc džungļos, tēv!', a=a_lv))
print(is_pangram('Neteikums ģērbj plīša frakā, mūc džungļos, tēv!', a=a_lv))