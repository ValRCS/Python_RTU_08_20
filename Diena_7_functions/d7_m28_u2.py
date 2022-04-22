#2. uzdevums
 
def is_palindrome(text: str) -> bool:
    clean_text = text.lower().replace(" ", "")
    return clean_text == clean_text[::-1]

print(is_palindrome("alus ari ira sula"))
print(is_palindrome("Alus ari ira      sula"))
print(is_palindrome("not palindrome"))