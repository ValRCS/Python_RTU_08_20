def is_pangram(text):
    """
    Checks if a string is a pangram.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    for letter in alphabet:
        if letter not in text:
            return False
    return True

print(is_pangram('The quick brown fox jumps over the lazy dog.'))

def needle_in_haystack(needle, haystack):
    """
    Checks if a string is in another string.
    """
    return needle in haystack