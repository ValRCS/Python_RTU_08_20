# def is_palindrome(text,debug=False):# debug is just a name of the argument, you can use any name you want
#     text = text.lower()
#     text = text.replace(" ","") # strings are not mutable, so you need to assign it back to text
#     if debug:
#         print("Pārbaudu...", text,"Lasu atpakaļ...", text[::-1])
#     return text == text[::-1]
 
# # if is_palindrome(input("ievadiet tekstu: ")) == False:
# #     print("Jūsu teksts nav palindroms")
# # else:
# #     print("ir palindroms")

# 2.uzd

def format_text(text):
    return text.lower().replace(" ", "")

# we can use type hints to indicate what type of data we expect
# however this is not enforced!
# only linters will complain if you do not follow the type hints
def is_palindrome(text:str) -> bool:
    reverse_text = text[::-1]
    return format_text(reverse_text) == format_text(text)
# again if we return a Boolean value
# we do not need if else
# def is_palindrome(text):
#     reverse_text = text[::-1]
#     if format_text(reverse_text) == format_text(text):
#         return True
#     else:
#         return False
# ABOVE IS ANTI PATTERN !!

original_text = "Alus ari ira sula"
print(f"Original text: {original_text}")
print(f"Is palindrome: {is_palindrome(original_text)}")

# lets make some assertions
# again these will run silently if the condition is met
assert is_palindrome("alus") == False
assert is_palindrome("alus ari ira sula") == True
assert is_palindrome("Abba") == True
assert is_palindrome("") == True