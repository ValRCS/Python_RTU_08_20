# def is_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
#     alphabet = set(a)
#     return set(mytext.lower()) >= alphabet
def is_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
    return set(mytext.lower()) >= set(a)
    
print(is_pangram("abcdefghijklmnopqrstuvwxyz"))
print(is_pangram("The quick fox jumps over the sleeping dog"))
print(is_pangram("When zombies arrive quickly fax Judge Pat"))
print(is_pangram("The quick brown  fox jumps over the lazy dog"))

import string
print(string.ascii_lowercase)