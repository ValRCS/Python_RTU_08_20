## ----- Uzdevums-2 -----
"""
Uzrakstiet funkciju is_palindrome(text)
kas atgriež bool True vai False atkarībā vai vārds vai teikums ir lasāms vienādi no abām pusēm.
PS no sākuma varat sākt ar viena vārda risinājumu, bet pilns risinājums ignorēs atstarpes(whitespace) un lielos/mazos burtus
is_palindrome("Alus ari ira      sula") -> True
"""
 
# def is_palindrome(text: str) -> bool:
#     text_neat = text.lower().replace(' ', '') # could use upper()
#     text_neat_reversed = text_neat[::-1]
#     return text_neat == text_neat_reversed
#     # return text_neat in text_neat_reversed and text_neat_reversed in text_neat

def is_palindrome(text):
    return text.replace(" ", "").lower() == text[::-1].replace(" ", "").lower() # twice the work compare to upper

print(is_palindrome("AbBA"))
print(is_palindrome("Alus ari ira sula"))
print(is_palindrome("Alus ari ir a      sula    "))
print(is_palindrome("nav palindroms"))
