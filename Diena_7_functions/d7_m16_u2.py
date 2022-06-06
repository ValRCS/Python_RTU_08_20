# 2.uzd.
def is_palindrome(text:str) -> bool:
    text = str(text) # will do nothing if already a string
    text = text.lower().replace(' ', '')
    return text == text[::-1]


print(is_palindrome("madam"))
print(is_palindrome("Alus   a   ri      ira   sula"))
print(is_palindrome("Nav palindroms"))
print(is_palindrome("")) # True
print(is_palindrome("   ")) # True
print(is_palindrome(777)) # True

def is_larger(a: int, b: int) -> bool:
    return a > b # i could add more logic here with and, or, not 

print(is_larger(2,3))
print(is_larger(32,3))