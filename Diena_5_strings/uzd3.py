# text = input("Kas nav slikts?")
# text = str(text)
# print(f"{text.replace('nav slikts', 'ir labs')}, ja tā labi padomā")

inputText = input("Lūdzu, ievadi tekstu! ")

word1 = "nav"
word2 = "slikt"

word1Find = inputText.find(word1)
word2Find = inputText.rfind(word2) + len(word2)
# could add another if to check if word2 is before word1

positiveText = inputText[:word1Find] + "ir lab" + inputText[word2Find:]

if word1Find != -1 and word2Find != -1:
    print(positiveText)
else:
    print(inputText)
