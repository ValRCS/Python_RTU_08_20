# Uzdevums Nr.2
def is_palindrome(word):
    # cleaned = word.lower().replace(" ", "") # upper() would work as well
    cleaned = "".join(word.lower().split())
    # drow=word[::-1]
    print(cleaned)
    return cleaned == cleaned[::-1]

# this part is not needed
    # if word==drow:
    #     return True
    # else:
    #     return False

print(is_palindrome("alus ari ir a sula"))
print(is_palindrome("Alus ari ira    sula"))
print(is_palindrome("ABbA"))
print(is_palindrome("Nevajadzetu but palindroma"))