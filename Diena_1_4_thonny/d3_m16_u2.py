##2.uzdevums
# minExperience = 2
# bonusPercent = 0.15
# salary = float(input("Ievadiet savu mēneša algu: "))
# experience = int(input("Ievadiet savu stažu: "))
# bonusAmount = 0
# if experience > minExperience:
#     bonusAmount = (experience - minExperience) * (salary * bonusPercent)
#     bonusAmount = round(bonusAmount, 2)
# print(f"sagaidamais bonus: {bonusAmount}")

year = float(input("Ievadiet nostrādāto gadu skaitu "))
if year <= 2:
    print("Priecīgus Ziemassvētkus!")

else:
    salary = float(input("Ievadiet mēneša algas apjomu "))
    print(f"Jums pienākas prēmija {(year - 2) * (salary * 0.15)} € apmērā")
