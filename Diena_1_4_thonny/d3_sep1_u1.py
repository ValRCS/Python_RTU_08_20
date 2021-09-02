# 1. Uzrakstiet programmu, kas pārbauda lietotāja temperatūru.
#Ja lietotājs ievada zem 35, tad prasiet vai "nav par aukstu"
#Ja no 35 līdz 37 (ieskaitot), izvadiet "viss kārtībā"
#Ja ir pāri 37, tad izvadiet "iespējams drudzis"
 
my_temperature = float(input("Temperature is "))
print(f"My temperature is {my_temperature}")
if (my_temperature < 35):
    print("Is it too cold?")
# elif my_temperature >= 35 and my_temperature <= 37:
elif 35 <= my_temperature <= 37:
    print("It is ok")
else:
    print("Maybe fever")