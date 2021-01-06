s = input("3rd task. Enter the phrase: ")
nav = s.find("nav")
slikts = s.find("slikts")
if slikts == -1:
    slikts = s.find("slikta") 
if nav >= 0 and slikts >= 0 and nav < slikts:
    s = s[:nav] + "ir lab" + s[slikts+5:]
print(s)