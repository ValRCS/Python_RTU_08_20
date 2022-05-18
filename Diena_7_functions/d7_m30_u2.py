## Task No.2
def is_palindrome(text: str) -> bool:
    """
    Returns True if text is a palindrome, False otherwise
    ignores spaces and capitalization
    """
    # clean_text = text.lower().replace(" ", "")
    # if we tabs removed too much, we can use:
    clean_text = "".join(text.lower().split()) # removes all whitespaces and joins the rest
    print(clean_text)
    # notice no if is needed! == gives us bool
    # anti-pattern would be 
    # if clean_text == clean_text[::-1]:
    #     return True
    # else:
    #     return False
    return clean_text == clean_text[::-1]

print(is_palindrome("kakak"))
print(is_palindrome("Alus ari ira   sula"))
print(is_palindrome("Alus ari ira \t \n  sula"))