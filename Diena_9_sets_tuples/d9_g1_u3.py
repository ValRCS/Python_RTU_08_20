def is_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
    # return set(mytext.lower().replace(" ", "")) == set(a)
    return set(mytext.lower()) >= set(a)
 
 
print(is_pangram("abcd foo "))
print(is_pangram("The quick brown  ģindenis fox jumps over the lazy dog"))
print(is_pangram("The five boxing wizards jump quickly"))

a_lv = 'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'
print(is_pangram('Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!', a=a_lv))
print(is_pangram('Čehu zeņķi ģērbj plīša frakā, mūc džungļos, tēv!', a=a_lv))
print(is_pangram('Neteikums ģērbj plīša frakā, mūc džungļos, tēv!', a=a_lv))