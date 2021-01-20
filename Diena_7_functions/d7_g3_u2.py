# def is_palindrome(text):
#     clean = text.lower()
#     nospace = clean.replace(" ", "")
#     reverse = nospace[::-1]
#     return reverse == nospace

def is_palindrome(text):
    text = text.lower().replace(" ", "")
    # return "Palindroms" if text == text[::-1] else "Nav Palindroms"
    return text == text[::-1]

 
print(is_palindrome("Alus ari    ira  sula"))
print(is_palindrome("aBBa"))
print(is_palindrome("aBBaaa"))