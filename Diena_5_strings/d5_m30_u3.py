#3
#programma teksta pārveidošanai
# text = input("Ievadi tekstu: ")
# text = "Alus nav nemaz tik slikts vai ne?"
# text = "Auto nav jauns"
text = "Auto bija slikts , man nav vārdu..."
 
nav = "nav"
ir ="ir"
slikts = "slikts"
labs = "labs"
 
# we needed to add an extra check to see if nav is before slikts
if nav in text and slikts in text and text.find(nav) < text.find(slikts):
    print(text[:text.find(nav)] + ir + ' ' + labs + text[text.find(slikts) + len(slikts):])
else:
    print(text)