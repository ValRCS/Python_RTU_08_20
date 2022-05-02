# 2 Taska palindrome
# my_text = input("Enter yor text here: ")
 
def is_palindrome(text: str) -> bool:
    """
    atgriež bool True vai False atkarībā vai vārds vai teikums ir lasāms vienādi no abām pusēm
    """
    text = "".join(text.lower().split()) # get rid of all whitespace and make lowercase
    # text = text.lower().replace(" ", "")	# izņemt tukšus simbolus
    return text == text[::-1]


print(is_palindrome("Alus ari ira      sula"))
print(is_palindrome("Alus ari\n ira     \t sula"))
print(is_palindrome("not a palindrome lus ari ira      sula"))
my_text = "Abbb    \t a"
print(is_palindrome(my_text))
print(my_text)

# 2.uzd. Palindroms. NAV SKAIDRS, KĀPĒC NEIET.
# word=str(input("Enter a palindrome: "))
word="Alus ari ira      sula"
def is_palindrom(word: str)-> bool:
    word=word.lower().replace (" ", "")
    rev_word=word[::-1]
    if rev_word==word:
        print(f"{word} is a palindrome")
        return True
    else:
        print (f"{word} is NOT a palindrome")
        return False

print(is_palindrom(word))


