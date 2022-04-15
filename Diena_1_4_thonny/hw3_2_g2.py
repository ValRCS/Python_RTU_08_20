years = int(input("ievadiet nostrādāto gadu skaitu: "))
salary = float(input("ievadiet savu mēneša algu: "))
if years > 2:
    bonus = (salary * 0.15) * (years - 2)
    print(str(years) + " gadu stāžs, " + str(salary) + " Eiro alga, bonuss būs " + str(bonus) + " Eiro.")
    print(f"{years} gadu stāžs {salary} Eiro alga, bonus {bonus} Eiro")