#1 Uzdevums
# temper = float(input("What is your temperature? "))
# if temper < 35:
#     print('nav par aukstu')
# elif 35 <= temper <= 37:
#     print('viss kārtībā')
# else:
#     print('iespējams drudzis')

temp=float(input("Nelabi izskaties, negribi pamērīt temperatūru!"))
low_temp=35
high_temp=36.9
if temp < low_temp:
    print ("nav par aukstu?")
elif temp >= low_temp and temp <= high_temp:
    print ("Dzīvo mierā! Viss ir kārtībā!")
else: # atliek temp > high_temp
    print ("iespējāms drudzis")