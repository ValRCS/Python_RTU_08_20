#2.uzdevums
years_before_bonus = 2
Xmas_bonus_rate = 0.15

salary = int(input("What is your salary?"))
record_of_service = float(input("How long are you working in the company?"))
bonus_period = record_of_service - years_before_bonus

# if bonus_period > 0: # alternative
if record_of_service > years_before_bonus:
    total_bonus = round(salary*bonus_period*Xmas_bonus_rate, 2)
    print(f"Your Xmas bonus this year will be {total_bonus}")
else:
    print(f"Sorry, you are not entitled to Xmas bonus!")