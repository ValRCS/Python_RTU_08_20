alga = float(input("Ievadiet mēneša algu (EUR): "))
gadi = float(input("Ievadiet nostrādātu gadu skaitu: "))
if int(gadi)>2:
    print("Bonuss ir EUR", round(((int(gadi)-2)*alga*0.15),2))
else:
    print("Bonusu vēl neesi pelnījis :(")

# bonusa_stazhs=2
# print("Aprēķiniet savu Ziemassvētku bonusu!")
# stazhs=float(input("Ievadiet nostrādāto gadu skaitu: "))
# if stazhs > bonusa_stazhs:
#     print("Jums pienākas bonuss!")
#     alga=float(input("Ievadiet mēneša aplgas apjomu: "))
#     bonuss=round (((stazhs-bonusa_stazhs)*0.15*alga), 2)
#     print ("Ziemassvētku bonusa apjoms=",bonuss)
# else:
#     print("Vēl neesat pelnījis bonusu.")