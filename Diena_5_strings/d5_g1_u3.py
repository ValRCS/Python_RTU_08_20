text = input("Please enter some text: ")
nav = text.find("nav")
slikts = text.rfind("slikts") # rfind is from right side
 
if nav >= 0 and slikts >= 0 and nav < slikts:
    newText = text[:nav] + "ir labs " + text[slikts+6:]
    print(newText)