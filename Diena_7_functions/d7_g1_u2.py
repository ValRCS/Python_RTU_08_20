# def is_palindrome(text):
#     text_lower = text.lower()
#     text_final = text_lower.replace(" ","")
#     text_reversed = text_final[::-1]
#     return text_final == text_reversed

# good balance between readability and space
# def is_palindrome(text):
#     clean_text = text.lower().replace(" ", "")
#     return clean_text == clean_text[::-1]

def is_palindrome(text):
    return text.lower().replace(" ", "") == text.lower().replace(" ", "")[::-1]


print(is_palindrome("Alus ari   ira sula"))
print(is_palindrome("aBBa"))
print(is_palindrome("aaBBa"))
