def is_palindrome(text="Alus ari ira      sula"):
    prepared_text = text.lower().replace(" ", "")
    return prepared_text == prepared_text[::-1]
    # text = text.lower()
    # text = text.replace(" ", "")
    # result = text[::-1]
    # return result == text
    # if result == text:
    #     r=True
    # else:
    #     r=False

    # print(r)


print(is_palindrome("Alus ari ira      sula"))
print(is_palindrome("Alus nav ari ira      sula"))
