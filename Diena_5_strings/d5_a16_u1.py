# Juceklis
# Lietotājs ievada vārdu.
# Tiek atgriezts lietotāja vārds apgriezts un sākas ar lielo burtu un papildu 
# teksu pamatīgs juceklis vai ne pirmais lietotāja burts?
# Valdis -> Sidlav, pamatigs juceklis vai ne V?
 
user_input = input("Lietotāj, ievadi savu vārdu: ")
print(f"{user_input[::-1].title()}, pamatīgs juceklis, vai ne {user_input[0]}")