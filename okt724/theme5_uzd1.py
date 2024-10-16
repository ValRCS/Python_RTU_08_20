vards = input("Kā tevi sauc?: ")
apgriezts_vards = vards[::-1].capitalize()
pirmais_burts = vards[0].upper()
print(f"{apgriezts_vards}, pamatīgs juceklis vai ne, {pirmais_burts}?")
# below is same but arguably harder to read, so above approach is preferred
print(f"{vards[::-1].capitalize()}, pamatīgs juceklis vai ne, {vards[0].upper()}?")
