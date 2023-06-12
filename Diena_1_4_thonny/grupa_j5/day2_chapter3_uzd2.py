# 2. uzdevums
 
years = int(input("Cik pilnu gadu ir nostradars: "))
salary = float(input("Cik liels ir menesalgas apjoms: "))
bonuss_procent = 15 # procentu bonuss par gadu
min_years_for_bonus = 2
 
bonuss_money = salary*bonuss_procent/100*(years- min_years_for_bonus)
# optional to round
bonuss_money = round(bonuss_money,2) # maybe 0 if we only want Euros
if years < min_years_for_bonus:
    print("Sogad bez bonusa")
else:
    print (f"Stāžs ir {years} Alga ir: {salary}  Bonus bus : {bonuss_money}")