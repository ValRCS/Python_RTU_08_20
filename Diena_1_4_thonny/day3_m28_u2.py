#2. Firma apsolījusi Ziemassvētku bonusu 15% apjomā no mēneša algas par KATRU nostrādāto gadu virs 2 gadiem.
#Uzdevums. Noprasiet lietotājam mēneša algas apjomu un nostrādāto gadu skaitu.
#Izvadiet bonusu.
#Piemērs 5 gadu stāžs, 1000 Eiro alga, bonuss būs 450 Eiro.
 
years = int(input("Cik pilnus gadus jūs esat nostrādājuši šajā uzņēmumā? "))
bonus_treshold = 4
bonus_percentage=0.15
if years <= bonus_treshold:
    print(f"Jūs nekvalificējaties bonusam, jo nav sasniegts vismaz 1 pilns gads virs {bonus_treshold} gadu stāža!")
elif years > bonus_treshold:
    salary=round(float(input("Cik liela ir jūsu mēneša bruto alga EUR? ")),2)
    years_for_bonus=years-bonus_treshold
    bonus_size=salary*bonus_percentage*years_for_bonus
    bonus_size=round(bonus_size,2)
    print(f"Jūsu bonuss ir {bonus_size} EUR") 