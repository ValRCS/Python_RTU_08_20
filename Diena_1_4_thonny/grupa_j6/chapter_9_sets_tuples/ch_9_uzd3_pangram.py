import string

def is_pangram(mytext, alphabet=string.ascii_lowercase):
    # alphabet = set(string.ascii_lowercase)
    alphabet = set(alphabet)
    text = mytext.lower().replace(" ", "")
    text_chars = set(text)
    # return text_chars == alphabet # this would be for proper pangram
    return alphabet <= text_chars # this would be for pangram
# we tested whether set of all alphabet letters is a subset of set of all letters in text
 
text = "The quick brown fox jumps over the lazy dog"
result = is_pangram(text)
print(result)
print(is_pangram("The quick brown fox jumps over the lazy dog!"))

latvian_alphabet = "aābcčdeēfgģhiījkķlļmnņoprsštuūvzž"
assert len(latvian_alphabet) == 33

print(is_pangram("Ārā žņaud žurkas, ķērpis blīkšķ, cits gudri čukst.", latvian_alphabet))
print(is_pangram("Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!", latvian_alphabet))