# 2. Palindroms
 
def is_palindrome(sentence, remove_punctuation=False) -> bool:
    if remove_punctuation:
        for char in sentence:
            if not char.isalnum():
                sentence = sentence.replace(char,"")
    sentence_original = sentence.replace(" ","").lower()
    sentence_reversed = sentence_original[::-1]
    return sentence_reversed == sentence_original

print(is_palindrome("Alus ari ira sula"))
print(is_palindrome("Alus     ari ira     sula"))
print(is_palindrome("Alus ari ira sula!"))
print(is_palindrome("Alus ari ira sula!", remove_punctuation=True))

# we could also do one liner
def is_palindrome_one_liner(sentence) -> bool:
    return sentence.replace(" ","").lower() == sentence.replace(" ","").lower()[::-1]

print(is_palindrome_one_liner("Alus ari ira sula"))