teksts = input("Ievadi tekstu: ")
# if teksts.find("nav") != -1 and teksts.find("slikt") != -1:
if "nav" in teksts and "slikts" in teksts and teksts.find("nav") < teksts.find("slikt"):
    nav = teksts.find("nav")
    slikts = teksts.find("slikt")+5
    print(teksts + " -> " + teksts[:nav]+"ir lab"+teksts[slikts:])
else:
    print(teksts)