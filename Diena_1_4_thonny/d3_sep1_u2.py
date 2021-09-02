#2. Firma apsolījusi Ziemassvētku bonusu 15% apjomā no mēneša algas par KATRU nostrādāto gadu virs 2 gadiem.
#Uzdevums. Noprasiet lietotājam mēneša algas apjomu un nostrādāto gadu skaitu.
#Izvadiet bonusu.
    
bonus_rate = 0.15
years_to_get_bonus = 2
pay = float(input("What is your salary?"))
experience = int(input("How many years have you worked here?"))
if experience >= years_to_get_bonus:
    bonus = (pay*bonus_rate)*(experience-years_to_get_bonus)
#     bonus = round(bonus, 2)
    print(f"Your earned bonus is {bonus:.2f} €")
else:
    print("Not enough work experience, still need to work to show your loyalty")


# # 2. Firma apsolījusi Ziemassvētku bonusu 15% apjomā no mēneša algas par KATRU nostrādāto gadu virs 2 gadiem.
#  
# # Uzdevums. Noprasiet lietotājam mēneša algas apjomu un nostrādāto gadu skaitu.
#  
# # Izvadiet bonusu.
#  
# # Piemērs 5 gadu stāžs, 1000 Eiro alga, bonuss būs 450 Eiro.
# your_salary = input("What is your salary?")
# print (f"My sallary is {your_salary} euros")
# your_work_experience = input("how long is your work experience?")
# print (f"My work experience is {your_work_experience} years")
# your_salary = int(your_salary)
# your_work_experience = int(your_work_experience)
# if your_work_experience > 2:
#     bonuss = (your_salary * 0.15) * (your_work_experience - 2)
#     print (f"you will receive {bonuss} eur bonuss")