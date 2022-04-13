#2.uzdevums
salary = float(input("Cik ir Jūsu mēneša alga? EUR:"))
years = float(input("Cik gadus Jūs strādājat uzņēmumā?"))
percent = 0.15
minimum_years = 2

if years > minimum_years:
    bonuss = salary*percent*(years - minimum_years)
    bonuss = round(bonuss, 2)
    print(f"Jūsu bonus ir {bonuss} EUR")
else:
    print(f"Diemžel, šogad Jums nepienākas bonus.")