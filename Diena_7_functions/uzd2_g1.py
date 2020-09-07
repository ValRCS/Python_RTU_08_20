def is_palindrome(text):
    cleantext = text.lower().replace(" ", "")
    return cleantext == cleantext[::-1]


print(is_palindrome("Alus ari ira sula"))
print(is_palindrome("Alus   ari iRa   sula"))
