def is_palindrome(text):
    my_text = text.lower().replace(" ", "")
    return my_text == my_text[::-1]
 
 
print(is_palindrome("Alus ari   IRa    sula"))
print(is_palindrome("Abba"))
print(is_palindrome("Valdis"))