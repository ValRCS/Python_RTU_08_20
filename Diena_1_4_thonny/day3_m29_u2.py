# gadi = int(input(f"ievadiet nostrādātos gadus!"))
# alga = float(input(f"ievadiet savu algu!"))
# print(gadi)
# print(alga)
# if gadi>2:
#     bonuss = (gadi-2)*0.15*alga
# else:
#     bonuss = 0
# bonuss = round(bonuss, 2
# print("bonuss ir", bonuss)

salary = float(input("What is you salary Eur? "))
years_work = int(input("How many year you work? "))
if years_work > 2:
    years = years_work - 2
    bonuss = salary * 0.15 * years
print(f"Your bonuss is {bonuss}")