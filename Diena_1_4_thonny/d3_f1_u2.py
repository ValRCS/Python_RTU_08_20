salary = int(input("What is your salary?"))
years = float(input("How many years have you been working here?"))
 
if years < 2:
    print("No bonus for you!")
else:
    bonus = salary * 0.15 * (years - 2)
    bonus = round(bonus, 2)
    print(f'This is your bonus: {bonus}')

# alga = int(input("Kāda ir Jūsu alga? "))
# stazhs = float(input("Un kāds ir Jūsu darba stāžs? "))
# bonuss = alga * 0.15
# bonuss2 = round(alga * (stazhs - 2) * 0.15, 2)
# if stazhs > 2 and stazhs < 3:
#     print (f"Jūsu bonuss ir {bonuss} EUR")
# elif stazhs >= 3:
#     print (f"Jūsu bonuss ir {bonuss2} EUR")
# else:
#     print ("Jūsu stāžs nav pietiekošs bonusa saņemšanai.")