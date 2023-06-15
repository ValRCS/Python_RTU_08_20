#1.uzdevums Juceklis
 
#Lietotājs ievada vārdu.
#Tiek atgriezts lietotāja vārds apgriezts un sākas ar lielo burtu un papildu teksu pamatīgs juceklis 
# vai ne pirmais lietotāja burts?
 
#Valdis -> Sidlav, pamatigs juceklis vai ne V?
 
# user_input = input("Lūdzu ieraksti vārdu ")
# i = len(user_input)
# print(f"{str.upper(user_input[-1])}",end="")
# print(user_input[-2:0:-1],end="")
# print(f"{str.lower(user_input[0])}, pamatigs juceklis vai ne {str.upper(user_input[0])}?",end="")

name = input("Lūdzu ievadi savu vārdu: ")
reverse_name = name[::-1]
 
print(reverse_name.capitalize(), f", pamatīgs juceklis vai ne {name[0].capitalize()}?", sep="")
# same as following without any new variables
print(f"{name[::-1].capitalize()}, pamatīgs juceklis vai ne {name[0].capitalize()}?")
print(f"{name[::-1].capitalize()}, pamatīgs juceklis vai ne {name[0].upper()}?")