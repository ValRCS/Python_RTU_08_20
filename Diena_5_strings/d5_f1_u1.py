# Strings - Klases Uzdevumi
# Juceklis
 
# Lietotājs ievada vārdu.
 
# Tiek atgriezts lietotāja vārds apgriezts un sākas ar lielo burtu un papildu teksu pamatīgs juceklis vai ne pirmais lietotāja burts?
 
# Valdis -> Sidlav, pamatigs juceklis vai ne V?
 
# name = input("Print your name: ")
# reverse_name=name.lower()[::-1]   #KĀPĒC NEDARBOJAS?
# print(reverse_name)
 
# name = input("Print your name: ")
# lower_name=name.lower()
# reverse_name=lower_name[::-1]
# title_name=reverse_name.title()
# print(title_name+" pamatīgs juceklis vai ne "+name[0])

name = input("Jūsu vārds: ")
# reverse  = name[::-1]
# capitalized_reverse = reverse.capitalize()
# print(f"{capitalized_reverse}, pamatīgs juceklis, vai ne {name[:-1]}!?")
# print(f"{capitalized_reverse}, pamatīgs juceklis, vai ne {name[0]}!?")
print(f"{name[::-1].capitalize()}, pamatīgs juceklis, vai ne {name[0]}!?")