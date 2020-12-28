# stazs = int(float(input("Sakiet, cik pilnus gadus jau šeit strādājat? ")))
# alga = float(input("Sakiet, kāda ir Jūsu mēnešalga? "))
# if stazs >= 2:
#     bonuss = 0.15 * (stazs - 2) * alga
#     bonuss = round(bonuss,2) # grāmatveži gan nebūtu priecīgi par apaļošanu! Bez "round" izdod 449.(9)
#     print(f"Jūsu bonuss ir {bonuss} eiro")
# else:
#     print("Sorry no bonus")


#Task 2:
salary = float(input("Please enter your monthly salary: "))
years = int(input("How many years are you working for a company: "))
bonuss = 0.15
difference = years - 2
if years <= 2:
    print("No bonuss this year")
else:
    pay_out = round(difference*bonuss*salary, 0)
    print("This year bonuss is ", pay_out, "EUR.")
