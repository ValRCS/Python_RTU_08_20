#2. UZDEVUMS
percentage_of_bonus = 0.15
salary = float(input("Please enter your monthly salary: "))
year = int(input("Please enter years working: "))
min_year_for_bonus = 2

bonus_formula = (year - min_year_for_bonus) * salary * percentage_of_bonus
bonus_formula = round(bonus_formula, 2) # maybe 0 if want euros only

if year <= min_year_for_bonus:
    print(f"Sorry no bonus, you need at least {min_year_for_bonus} years here")
    print(f"Your bonus, unfortunatelly, is: {bonus_formula}")
else:
    print(f"Your bonus is: {bonus_formula}")