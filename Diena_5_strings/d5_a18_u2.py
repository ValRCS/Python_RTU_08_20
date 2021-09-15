# my_text = (input(f"Tell me some word "))
# lenght_text = len(my_text)
# # my_text_length = my_text.replace((my_text), lenght_text*'*')
# my_text_length = lenght_text*'*' # same simpler than above 
# print(my_text_length)

word = input("Please enter word to guess: ")
space = " "
hide = ""
symbol = "*"
 
for n in word:
    if n == space:
        hide += n  # also hide += space would work since here n is equal to space...
    else:
        hide += symbol
        
print(hide)

letter = input("Enter letter you think might be in word: ")
result = ""
for n in word:
    if n == letter:
        print(letter, end="")
        result += letter
    elif n == " ":
        print(" ", end="")
        result += n
    else:
        print("*", end="")
        result += "*"

print()
print(result)

# if we want a hangman game we need to continue processing result until it matches original word