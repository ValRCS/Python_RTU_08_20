# def is_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
#     test = set(mytext.lower().replace(" ",""))
#     return test.issubset(a)


def is_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
    return set(a) <= set(mytext.lower())

print(is_pangram("The five boxing wizards jump quickly"))
print(is_pangram("Nevajadzētu būt"))

a_lv = 'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'
print(is_pangram('Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!', a=a_lv))
print(is_pangram('Čehu zeņķi ģērbj plīša frakā, mūc džungļos, tēv!', a=a_lv))
print(is_pangram('Neteikums ģērbj plīša frakā, mūc džungļos, tēv!', a=a_lv))

lat_text = "Muļķa hipiji mēģina brīvi nogaršot celofāna žņaudzējčūsku."

print(is_pangram(lat_text, a=a_lv))