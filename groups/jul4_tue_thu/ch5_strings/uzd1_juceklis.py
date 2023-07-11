# Juceklis
 
vards = input("Ievadiet savu vārdu: ")
apgriezts_vards = vards[::-1]
apgriezts_vards = apgriezts_vards.capitalize()
 
pirmais_burts = vards[0].upper() # also title or capitalize would work
# pirmais_burts == apgriezts_vards[0].upper()
juceklis = "pamatigs juceklis vai ne"

# solution with concatenation
print(apgriezts_vards + ", " + juceklis + " " + pirmais_burts + "?")
# solution with f-string
print(f"{apgriezts_vards}, {juceklis} {pirmais_burts}?")