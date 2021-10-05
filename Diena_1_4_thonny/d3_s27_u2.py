#Uzdevums. Noprasiet lietotājam mēneša algas apjomu un nostrādāto gadu skaitu.
#Izvadiet bonusu.
#Piemērs 5 gadu stāžs, 1000 Eiro alga, bonuss būs 450 Eiro.
 
salary = float(input("what is your salary "))
 
years = float(input("How long do you work here "))
 
bonuss = (years-2)*0.15*salary
bonuss = round(bonuss, 2) # so two digits after comma
            
if years <= 2:
    print("In this year you don't have a bonuss")
else: # over 2
    print(f"Your bonuss will be {bonuss}")