# 3nod. 1.uzd.
#  
# temp = float(input ("Ievadiet savu temperatūru: "))
#  
# if temp < 35:
#     print("Vai nav par aukstu?")
# elif 35 <= temp <= 37:
#     print("Viss ir kārtībā")
# else:
#     print("Iespējams drudzis")

# 1. Uzrakstiet programmu, kas pārbauda lietotāja temperatūru.
# 
# Ja lietotājs ievada zem 35, tad prasiet vai "nav par aukstu"
# Ja no 35 līdz 37 (ieskaitot), izvadiet "viss kārtībā"
# Ja ir pāri 37, tad izvadiet "iespējams drudzis"
 
print("1. uzdevums", "="*50, "\n", sep="\n")
while True:
    try:
        user_temp = float(input("Tava temperatūra: "))
 
        if user_temp < 35:
            print("Vai nav par aukstu?")
            
        if 35 <= user_temp <= 37:
            print("viss kārtībā")
        
        if user_temp >37:
            print("Iespējams drudzis")
        
        option = input("Vai vēlies ievadīt vēlreiz? [y/N] ")
        if option == "N" or option == "n" or option == "":
            break
        
    except ValueError:
        print("Lūdzu ievadi skaitlisku vērtību")