src="alus ari ira sula"
 
def is_palindrome(teikums:str):
    """ nosakla vai teikums ir palindroms
 
    Args:
        teikums (String): teikums kuram vajag noteikt vai tas ir palindroms
 
    Returns:
        bool: True - ja ir palindroms, False - ja nav
    """
    clean_text=teikums.strip().replace(" ", "").lower()
    reversed_clean_text=clean_text[::-1]
    return clean_text == reversed_clean_text # no if needed as this is a boolean expression
    # one liner of the above - eight operations in one line
    # return teikums.strip().replace(" ", "").lower() == teikums.strip().replace(" ", "").lower()[::-1]

    
print( "Ir palindroms!" if is_palindrome(src) else "nav palindroms")

# some more tests - so no Errors are thrown means all is good
assert is_palindrome("Alus ari ira      sula") == True
assert is_palindrome("alus ari ira sula") == True
assert is_palindrome("ABBBA") == True
assert is_palindrome("ABBA") == True
assert is_palindrome("") == True
assert is_palindrome("a") == True
assert is_palindrome("ab") == False