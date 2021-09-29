# one liner
# def is_palindrome(text):
#       return text.lower().replace(" ","") == text.lower().replace(" ","")[::-1]

def is_palindrome(usr_text: str):
 
    usr_text = usr_text.lower().replace(' ', '') # we cache the value
    # Anti - pattern : avoid with booleans
    # if usr_text == usr_text[::-1]:
    #     result = True
    # else:
    #     result = False
    result = usr_text == usr_text[::-1] # right side is bool already!
    return result # i could have returned the above line immediately

# text = input("lūdzu ievadiet tekstu.")
text = "AAbbC     BB aa"
result = is_palindrome(text)
print(f"{text} is palinrome: {result}")