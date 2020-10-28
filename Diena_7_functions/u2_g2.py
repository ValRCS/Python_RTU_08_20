import string
print(string.punctuation) # built in property/constant

def is_palindrome(text, badchars=string.punctuation):
    text = text.lower()
    text = text.replace(" ", "")
    for c in badchars:
        text = text.replace(c, "")
    # alternative to the above
    # text = "".join([c for c in text if c not in badchars])

    answer = text[::-1]
    return answer == text

    
print(is_palindrome("Alus ari ira  sula"))
print(is_palindrome("Alus ari: ira  sula!!!"))
print(is_palindrome("Valdis"))