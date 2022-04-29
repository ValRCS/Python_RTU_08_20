# 3. Uzdevums 
 
def is_pangram(text:str, a = 'abcdefghijklmnopqrstuvwxyz') -> bool:
   return set(text.lower()) >= set(a)

def is_perfect_pangram(text:str, a = 'abcdefghijklmnopqrstuvwxyz') -> bool:
   return set(text.lower()) >= set(a) and len(set(text.replace(" ", "").lower())) == len(a)

print(is_pangram("The quick brown FOX jumps over the lazy dog"))

