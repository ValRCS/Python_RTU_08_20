word = input("Izdomā vārdu vai vārdu savienojumu ")
wordWithAsterisk = ""
for c in word:
    if c == " ":
        wordWithAsterisk += " "
    else:
        wordWithAsterisk += "*"
print(wordWithAsterisk)
 
 
guessWord = ""
while guessWord != word:
    guessWord = ""
    guessLetter = input("ievadi burtu ")
    for c in word:
        if c in [" ", guessLetter]:
            guessWord += c
            print("Malacis!")
        else:
            guessWord += "*"
    print(guessWord)