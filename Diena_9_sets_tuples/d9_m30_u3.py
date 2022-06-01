# 3. uzdevums
# - = - = - = - = - = - = - = - = - = - = - = - =
# def is_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
#     txt = set(mytext.lower().replace(' ', ''))
#     alphabet = set(a)
#     return txt == alphabet
 
# print(is_pangram("The quick brown fox jumps over the lazy dog"))

# Task Nr.3
 
# def is_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
#     mytext = mytext.lower()
#     for i in a:
#         if i not in mytext:
#             return False
#             break
#     return True

def is_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
    # return set(a).issubset(set(mytext.lower()))
    return set(a) <= set(mytext.lower())

print(is_pangram("The quick brown fox jumps over the lazy dog"))

a_lv = 'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'
print(len(set(a_lv)))

print(is_pangram('Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!', a=a_lv))
print(is_pangram('Čehu zeņķi ģērbj plīša frakā, mūc džungļos, tēv!', a=a_lv))
print(is_pangram('Neteikums ģērbj plīša frakā, mūc džungļos, tēv!', a=a_lv))