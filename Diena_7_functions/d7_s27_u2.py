def is_palindrome(usr_text: str = "AbbA") -> bool:
    print("Testing", usr_text)
    usr_text = usr_text.lower().replace(' ', '')
    # result = usr_text == usr_text[::-1]
    # return result
    return usr_text == usr_text[::-1]
    # return 42
 
# text = input("Lūdzu ievadiet tekstu vai vārdu.")



def are_two_words_palindromes(vards1, vards2):
    return vards1 == vards2[::-1]



def main():
    """
    Main program entry point
    """
    print(are_two_words_palindromes("alus", "sula"))

    print(is_palindrome())  #i do not need any arguments anymore since I have default
    print(is_palindrome("TENET"))  
    print(is_palindrome(""))  
    text = "Alus ari ira   sula"
    result = is_palindrome(text)
    print(f"{text} is palindrome: {result}")

    print(is_palindrome("Abba"))
    print(is_palindrome("Nevar but palindroms"))


if __name__ == "__main__": # this means this file was run directly not imported
    main()
