yearsForBonus = 2
bonusPercentage = 15
yearsAsSlave = float(input("Cik gadus Jūs strādājat kompānijā?"))
 
if yearsAsSlave > 2:
    salaryAmount = float(input("Kāda ir Jūsu mēnešalga?"))
 
 
if yearsAsSlave > 2:
    bonuss = int(salaryAmount * bonusPercentage / 100 * int(yearsAsSlave))
    print(f"Lieliski, Jūsu bonuss šogad ir {bonuss} naudiņas.")
else:
    print("Pffff, bonusi jānopelna! Pienāciet nākamgad!")