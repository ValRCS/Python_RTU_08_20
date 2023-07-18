# 2.3 Vai ir pangramma?
# uzrakstīt funkciju is_pangram, kas atgriež True, kad mytext parametrs satur visus burtus kas padoti a alfabetā.
def is_pangram(mytext, a='aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'):
    mytext = mytext.lower()
    text_letters = set(mytext)
    alphabet = set(a)
    return alphabet.issubset(text_letters)
# alternative - same operation would be return alphabet <= text_letters

# Latviešu panagramma ņemta no - https://jurjans.lv/lvpp/ :)
text1 = "Muļķa hipiji turpat brīvi mēģina nogaršot celofāna žņaudzējčūsku"
result1 = is_pangram(text1)
print(result1)  # True
# let's try a counter example
text2 = "Neko nevaru izdomāt"
result2 = is_pangram(text2)
print(result2)  # False

# let's try with English pangram
text3 = "The quick brown fox jumps over the lazy dog"
result3 = is_pangram(text3)
print(result3)  # False because we used Latvian alphabet as default
# to fix we simply pass English alphabet as second argument
# we will import string module to get ascii_lowercase
import string
en_alphabet = string.ascii_lowercase
print(en_alphabet)  # abcdefghijklmnopqrstuvwxyz
result3 = is_pangram(text3, en_alphabet)
print(result3)  # True

# we could write a function to check if it is proper pangram
def is_pangram_proper(mytext, a='aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'):
    mytext = mytext.lower().replace(" ", "")
    # TODO remove all punctionation
    for p in ".,!?;:()": # could use string.punctuation instead
        mytext = mytext.replace(p, "")
    text_letters = set(mytext)
    alphabet = set(a)
    # so proper pangram has to have all letters and no extra letters
    return alphabet == text_letters and len(a) == len(mytext)

# Proper Latvian pangram TODO find it
# something to do with Čeh