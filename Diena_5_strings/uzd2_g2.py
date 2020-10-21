mināmais_vārds = input("ievadi mināmo vārdu")
zvaigznītes = ""
for c in mināmais_vārds:
    if c == " ":
        zvaigznītes += " " # zvaigznītes = zvaigznītes + " "
    else:
        zvaigznītes += "*" # zvaigznītes = zvaigznītes + "*"
print(zvaigznītes)
burts = input("Ievadi simbolu: ")
 
šifrēts = ""
for c in mināmais_vārds:
    if c in [" ", burts.lower(), burts.upper()]:
        šifrēts += c
    else:
        c = "*"
        šifrēts += c
print(šifrēts)