# 6. Pirmskaitlis
# TODO add while try except for input
skaitlis = int(input("Ievadiet veselu pozitīvu skaitli: "))
 
if skaitlis < 2:
    print("Nav pirmskaitlis")
else:
    ir_pirmskaitlis = True
    for dalitajs in range(2, int(skaitlis ** 0.5) + 1):
        if skaitlis % dalitajs == 0:
            print(f"Not prime {skaitlis} divides with {dalitajs} with no reminder")
            ir_pirmskaitlis = False
            break
    else: # no need for flag
        print(f"normal exit Ievadītais skaitlis {skaitlis} ir pirmskaitlis")
        
    if ir_pirmskaitlis:
        print(f"Ievadītais skaitlis {skaitlis} ir pirmskaitlis")
    else:
        print(f"Ievadītais skaitlis {skaitlis} nav pirmskaitlis")
 