#2. uzd func
# i can have type hints that are not enforced
# but they are useful for documentation
def is_palindrome(text: str) -> bool:
    """
    Arguments:
    text -- string
    Returns 
    True if text is a palindrome, 
    False otherwise"""	
    text = text.replace(" ", "").lower()
    reversed_text = text[::-1]
    return text == reversed_text

 
print(is_palindrome("Alus ari ira      sula"))
# cruciall Python does not enforce type hints!!
# linters will warn you if you do not follow type hints