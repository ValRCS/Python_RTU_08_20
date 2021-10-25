def ispangram(my_text, a="abcdefghijklmnopqrstuvwxy"):
    for char in a:
        if char not in my_text.lower():
            return False
    return True

print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("The slow brown fox jumps over the lazy dog"))

def is_pangram(mytext, a="abcdefghijklmnopqrstuvwxyz"):
    return set(mytext.lower()) >= set(a)

print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("The slow brown fox jumps over the lazy dog"))

a_lv='aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'

print(is_pangram("Čeh, mūc – aļņu fāgs ģērbjot plīkšķ, žvindz", a=a_lv))
print(is_pangram("Nebūs", a=a_lv))