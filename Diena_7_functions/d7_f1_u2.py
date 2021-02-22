def is_palindrome(text: str) -> bool:
    clean_text = text.replace(' ', '').lower()
    return clean_text == clean_text[::-1]

print(is_palindrome("Alus ari ira      sula"))
print(is_palindrome("nav palindroms.."))
print(is_palindrome("ABba"))