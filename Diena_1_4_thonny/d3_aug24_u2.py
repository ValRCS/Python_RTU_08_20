#Firma apsolījusi Ziemassvētku bonusu 15% apjomā no mēneša algas par KATRU nostrādāto gadu virs 2 gadiem.
years_before_bonus = 2
bonus_rate = 0.15
salary = input("Kāda jums ir alga?")
salary = float(salary)
years = input("Cik gadus šeit strādājāt?")
years = float(years)
if years >= years_before_bonus:
    bonuss = bonus_rate*(years-years_before_bonus)*salary
#     bonuss = round(bonuss, 2)
    # we can skip round if we want to
    print(f"Jūsu prēmija ir {bonuss:.2f}") # this means show 2 digits after comma
else:
    print("Piedodiet, premijas nebus")