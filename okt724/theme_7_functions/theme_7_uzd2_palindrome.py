# 2. Palindroms
# let's create a function that returns only letters from the text
def only_letters(text: str) -> str:
    # we can use list comprehension to create a list of letters
    # we can use isalpha() method to check if the character is a letter
    # we can use lower() method to convert the letter to lower case
    # return "".join([letter.lower() for letter in text if letter.isalpha()])
    # we can use regular lists
    letters = []
    for letter in text:
        if letter.isalpha():
            letters.append(letter)
    # i have a list but I need a string with no spaces
    # I can use join method of the string to join the list of letters
    # in order for join to work
    #  I need to provide a string that will be used to join the list
    # also list should contain only strings
    return "".join(letters).lower()


def is_palindrome(text: str) -> bool:
    # list = []
    # for item in text:
    # #rev_item = item[::-1]
    #     if item != ' ':
    #         list.append(item.capitalize())
    # we can normalize the text by removing spaces and converting to lower case
    normalized_text = only_letters(text)
    normalized_text = normalized_text.lower()
    # above we did two operations in one line first we removed spaces and then converted to lower case
    reversed_text = normalized_text[::-1]
    # if normalized_text == reversed_text:
    #     result = True
    # else:
    #     result = False
    # # print(result)
    return normalized_text == reversed_text
is_palindrome("Alus ari ira      sula")
result = is_palindrome("Alus ari ira      sula")

print("Result", result)
print(is_palindrome("abracabra dfee")) # False
panama = "A man, a plan, a canal – Panama"
print(is_palindrome(panama)) # True

# let's try with Latvian
print(is_palindrome("Āri irā!    ....")) # True

