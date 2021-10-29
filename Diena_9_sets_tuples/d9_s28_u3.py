import string
print(string.ascii_lowercase)

def is_pangram(text, alphabet=string.ascii_lowercase):
    """
    Checks if text is a pangram.
    :param text: string
    :param alphabet: string
    :return: boolean
    """
    return set(text.lower()) >= set(alphabet)

print(is_pangram("abcd foo"))
print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("The five boxing wizards jump quickly"))

a_lv='aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'

print(is_pangram("Čeh, mūc – aļņu fāgs ģērbjot plīkšķ, žvindz", alphabet=a_lv))
print(is_pangram("Nebūs", alphabet=a_lv))