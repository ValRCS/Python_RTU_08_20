salary = float(input("Lūdzu, ievadiet savu mēneša algas apjomu (eiro)!"))
standing = float(input("Lūdzu, ievadiet nostrādāto gadu skaitu!"))
years = standing - 2
bonuss = round(salary/100*15*years, 2)
if standing <=2:
    print("Atvainojiet, Jūsu stāžam šogad nav paredzēts bonuss.")
else:
    print(f" Jūsu paredzamais Ziemassvētku bonuss ir {bonuss} eiro pēc {standing} gadu darba")