#Bonuss
print("Bonus time")
print("")
bonus_yearly_share = 0.15
min_years_for_bonus = 2
user_salary = float(input("Kāda ir Tava alga?"))
user_exp = float(input("Cik ilgi Tu jau strādā kompānijā?"))
if user_exp > min_years_for_bonus:
    bonuss = float(user_salary * (user_exp-min_years_for_bonus) * bonus_yearly_share)
#     bonuss = round(bonuss, 2) # up to cents or maybe just to euros
    # we can format numbers with f-strings to specific precision
    print(f"Tavs Ziemassvētku bonuss būs {bonuss:.4f} Eiro!")
else:
    print("Tad diemžēl šogad bonusa nebūs...")
print("")