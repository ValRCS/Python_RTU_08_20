# def is_palindrome(text="some text"):
#     # text = input("Input text:")
#     text = text.replace(" ","")
#     text = text.casefold() # more precise than lower or upper
#     # in latvia upper or lower would work just fine
#     return text == text[::-1]


def is_palindrome(text="badab"):
    lst = text.split() # sadala tekstu elementos un ieliek sarakstā
    # print(lst)
    # lst = [el for el in lst if len(el.strip()) > 0]
    # print(lst)
    # for i in range(len(lst)): # iziet cauri visiem saraksta elementiem
    #     if lst[i].lower() != lst[-(i+1)][::-1].lower(): # salīdzina pirmo un apgrieztu pēdējo elementu, otro ar apgrieztu pirmspēdējo utt.
    for asc,desc in zip(lst, lst[::-1]):
        if asc.lower() != desc[::-1].lower():
            return False
    return True
 
print(is_palindrome())
print(is_palindrome("abba"))
print(is_palindrome("Abba"))
print(is_palindrome("Alus ari ira     sula"))
print(is_palindrome("Alus ari i ra     sula"))