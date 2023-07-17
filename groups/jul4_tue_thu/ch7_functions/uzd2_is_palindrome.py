###############################################
#uzdevums #2
 
 
text = input("Ievadi tekstu palindroma parbaudei: ")
 
def is_palindrome(text:str) -> bool:
    """Returns True if text is palindrome
    Args:
        text (str): text to check
    Returns:
        bool: True if text is palindrome
    """
    text = text.lower().replace(' ', '')
    return text == text[::-1]

print(f"Teksts '{text}' is palindroms? {is_palindrome(text)}")  
