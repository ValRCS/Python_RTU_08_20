# 2. Firma apsolījusi Ziemassvētku bonusu 15% apjomā no mēneša algas par KATRU nostrādāto gadu virs 2 gadiem.
 
# salary = int(input("Lūdzu ievadiet savu mēneša algu: "))
# years_worked = int(input("Lūdzu ievadiet savu stāžu: "))
# 
# # so called ternary expression
# # https://mail.python.org/pipermail/python-dev/2005-September/056846.html
# # bonus = 0 if years_worked <= 2 else (0.15 * salary) * (years_worked - 2)
#  
# print(f"Jūsu bonuss: {bonus:.2f} Eiro")
while True:
    try:
        salary = float(input("what is your salary - in EUR?"))
        years = int(input("how many full years have you worked?"))
        break
    except ValueError:
        print("Either salary is not floating point or years is not integer")


bonus_percentage = 0.15
bonus = salary * bonus_percentage
base = 2
your_bonus = (years - base)*bonus
your_salary = salary + (years - base)*bonus
if years <= base:
    print("Sorry no bonus this year")
else: # """ let us write multiline strings without \n 
    print(f"""your bonus is {your_bonus:.2f},
and your new salary for December only is {your_salary}
""")