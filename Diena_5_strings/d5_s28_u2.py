# # Uzd. Nr.2
string_a = input("Enter any word or phrase: ")
word = ""
for c in string_a:
    if c != " ":
        word += "□"
    else:
        word += " "
print (f"String to be guessed is: {word}")
 
player_a = input("Input character to guess: ")
for c in string_a:
    if player_a == c:
        print(c, end="")
    elif c == " ":  
        print(c, end="")
    else:
        print("□", end="")