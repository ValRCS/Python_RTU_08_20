word1 = "abba"

def is_palindrome(word1) -> bool:
    word1 = word1.lower().replace(' ','')
    reverse_word1 = word1[::-1]
    return reverse_word1 == word1
print(is_palindrome(word1))
print(is_palindrome("ABBa"))
print(is_palindrome("Alus ari    ir a sula"))
print(is_palindrome("nevajadzētu būt"))
