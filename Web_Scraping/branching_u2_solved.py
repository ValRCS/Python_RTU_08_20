monthly_salary = float(input("Lūdzu, ievadiet savu mēnešalgu: "))
employment_years = int(input("Lūdzu, ievadiet savu darba stāžu uzņēmumā: "))
years_before_bonus = 2 # years before bonus is given
bonus_rate = 0.15 # 15% bonus rate
 
if employment_years <= years_before_bonus:
    bonus = 0
else:
    bonus = bonus_rate * monthly_salary * (employment_years - years_before_bonus)
 
total_salary = monthly_salary + bonus
# using :.2f to round to 2 decimal places but display only 2 decimal places
# data is not changed, only displayed
# 15 will be total width of the number including the decimal point and 2 decimal places
print(f"Tavs bonus ir € {bonus:15.2f} un kopējā alga ir € {total_salary:.2f}.")
# without rounding
print(f"Tavs bonus ir € {bonus} un kopējā alga ir € {total_salary}.")
# i could also round the data and then display it
bonus = round(bonus, 2)
total_salary = round(total_salary, 2)
print(f"Tavs bonus noapaļots ir € {bonus} un kopējā alga ir € {total_salary}.")